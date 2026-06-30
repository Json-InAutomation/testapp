#!/usr/bin/python3
# *****************************************
# PiTender Control Python script
# *****************************************
#
# Description: This script will dispense beverages.
#
# This script runs as a separate process from the Flask / Gunicorn
# implementation which handles the web interface.
#
# *****************************************

# Set this to False on Raspberry Pi Host ()
# prototype_mode = True
prototype_mode = True # Comment out for normal operation
# *****************************************
# Imported Libraries
# *****************************************

#from __future__ import division
import time
import os
import json
import datetime
from common import *
import threading
import logging
if(prototype_mode == True):
    # Prototype Modules for Test Host (i.e. PC based testing)
    from platform_prototype import PumpControl # Library for reading the ADC device
else:
    # Actual Modules for RasPi
    from platform_raspi import PumpControl # Library for reading the ADC device
control_logger = CustomLogger(
                    name="CONTROL",
                    out_file="control.out.log",
                    err_file="control.err.log"
                )

stop_threads = False
pause_threads = False
pourStripControl = LEDStripControl('OneStripNeopixel.py')

def Pour(pump_number, waitTime, platform):
    print(f' * Thread: {pump_number} Started for {waitTime} seconds.')
    control_logger.info(f' * Thread: {pump_number} Started for {waitTime} seconds.')
    platform.ActivatePump(pump_number)
    
    for x in range(waitTime): 
        time.sleep(1)
        global stop_threads 
        status = ReadStatus()
        
        if (status['control']['stop']==1):
            print(f' * Thread: {pump_number} cancelling. Threads is {stop_threads}') 
            control_logger.info(' * Thread: {pump_number} cancelling. Threads is {stop_threads}')
            platform.DeActivatePump(pump_number)
            return

        if status['control']['pause'] == 1:
            print(f' * Thread: {pump_number} paused.')
            control_logger.info(f' * Thread: {pump_number} paused.')
            platform.DeActivatePump(pump_number)
            while status['control']['pause'] == 1:
                time.sleep(1)  
                status = ReadStatus() 
            print(f' * Thread: {pump_number} resuming.')
            control_logger.info(f' * Thread: {pump_number} resuming.')
            platform.ActivatePump(pump_number) 
        
        # platform.ActivatePump(pump_number)  
        if (stop_threads == True): 
            print(f' * Thread: {pump_number} cancelling. Threads is {stop_threads}') 
            control_logger.info(f' * Thread: {pump_number} cancelling. Threads is {stop_threads}') 
            platform.DeActivatePump(pump_number)
            return
        
    platform.DeActivatePump(pump_number)
    print(f' * Thread: {pump_number} finished.')
    control_logger.info(f' * Thread: {pump_number} finished.')

# def DelayedPour(pump_number, runtime, platform, delay):
#     time.sleep(delay)
#     Pour(pump_number, runtime, platform)

def PourDrink(drink_name):
    drink_db = ReadDrinkDB()
    moniterDB = MoniterDB()
    if drink_name in drink_db['drinks']:
        status = ReadStatus()
        status['status']['active'] = 1
        WriteStatus(status)

        total_runtime = 0
        current_count = 0
        global stop_threads, pause_threads

        # Initialize Platform Object
        settings = ReadSettings()
        platform = PumpControl(settings)
        if 'percentage' not in settings:
            settings['percentage'] = {}

        print(f"Starting to prepare {drink_name}")
        control_logger.info(f"Starting to prepare {drink_name}")

        # Calculate total runtime
        for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
            total_runtime = max(total_runtime, int(pump_runtime * (settings['flowrate'] / 100)))

        print(f"Total Runtime: {total_runtime}") 
        control_logger.info(f"Total Runtime: {total_runtime}") 
        # Create and start threads to dispense each ingredient
        pumpThreads = []
        updated_quantities = {}
        pump_runtimes = {}
        for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
            pump_number = 'none'
            for index, value in settings['inventory'].items():
                if value == drink_ingredient:
                    pump_number = index
                    break  
            
            print(f"The mixer pump is a : {pump_number} ",pump_number == 'pump_16') 
            if pump_number == 'pump_16':
                continue 
            
            calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
            pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
            pumpThreads.append(pump_t)

            pump_runtimes[pump_number] = calculated_pump_runtime

            consumed_quantity = int(pump_runtime * (settings['flowrate'] / 100))
            if pump_number in settings['quantity']:
                settings['in_quantity'][pump_number] = max(0, settings['in_quantity'][pump_number] - consumed_quantity)
                updated_quantities[pump_number] = settings['in_quantity'][pump_number]
        
        # Start the pump threads
        for thread in pumpThreads:
            thread.start()
            
        mixer_started = False 
        def update_monitor_db():
            for pump_number, actual_quantity in updated_quantities.items():
                std_quantity = settings['quantity'][pump_number]
                moniterDB.ingridients(pump_number, actual_quantity, std_quantity)

        for x in range(total_runtime):
            current_count += 1
            status = ReadStatus()
           
            if (status['control']['stop']==1):
                stop_threads = True
                time.sleep(2)
                stop_threads = False
                moniterDB.consumpation(drink_name,1)
                break
            
            # Pause condition
            if status['control']['pause'] == 1:
                percent_progress = int((current_count / total_runtime) * 100)
                status['status']['progress'] = percent_progress
                WriteStatus(status)
                while status['control']['pause'] == 1:
                    time.sleep(1)
                    status = ReadStatus()

            # if stop_threads:
            #     break  

            # Update progress
            percent_progress = int((current_count / total_runtime) * 100)
            status['status']['progress'] = percent_progress
            WriteStatus(status)


            active_pumps = []
            for p_num, p_time in pump_runtimes.items():
                if current_count <= p_time:
                    p_name = settings['inventory'].get(p_num, "Unknown")
                    active_pumps.append(f"{p_num}")
            
            if mixer_started:
                if current_count <= mixer_start_count + pump_16_runtime:
                     active_pumps.append(f"pump_16")

            status['status']['active_pumps'] = active_pumps
            WriteStatus(status)
            
            if (percent_progress >= 50 and not mixer_started):
                pump_number = "pump_16"
                pump_16_runtime = max(1, int(total_runtime * 0.5)) 
                pump_t = threading.Thread(target=Pour, args=(pump_number, pump_16_runtime, platform))
                pump_t.start()  
                pumpThreads.append(pump_t)  
                mixer_started = True
                mixer_start_count = current_count

            time.sleep(1)

        # Wait for all pump threads to finish
        for thread in pumpThreads:
            thread.join()
        
        for pump_number,actual_quantity in updated_quantities.items():
            std_quantity = settings['quantity'][pump_number]
            moniterDB.ingridients(pump_number, actual_quantity, std_quantity)
            
        if (status['status']['progress'] == 100):
            moniterDB.consumpation(drink_name,1)
            update_monitor_db()
            
        print("Finished dispensing drink.")
        pourStripControl.stopStrip()
        WriteSettings(settings)

        print("Finished. Cleaning up status file.")
        control_logger.info("Finished. Cleaning up status file.")
        status['status']['active'] = 0
        status['control']['start'] = 0
        status['control']['stop'] = 0
        WriteStatus(status) 
    else:
        print("Error, no drinks match that name.")
 

def run_pump(platform,pump_number,total_runtime,progress):
    for index in range(20):
        status = ReadStatus()
        if status['control']['stop'] != 0:
            platform.DeActivatePump(pump_number)
            return progress, True
        progress += 1
        if total_runtime > 0:
            status['status']['progress'] = int(100 * (progress / total_runtime))
        else:
            status['status']['progress'] = 0
        WriteStatus(status)
        time.sleep(1) # Run for X seconds
       
    platform.DeActivatePump(pump_number)
    return progress,False

def CleanPump(pump_selected):
    print(f"The selected pump is {pump_selected} for cleaning")
    control_logger.info(f"The selected pump is {pump_selected} for cleaning")
    settings = ReadSettings()
    status = ReadStatus()
    status['status']['active'] = 1
    WriteStatus(status)

    # Initialize Platform Object
    platform = PumpControl(settings)
    total_runtime = 0
    progress = 0
    
    def is_valid_pump(pump_number, pin_number):
        if pump_number == 'pump_16' or pin_number == 5 or pin_number == 0:
            return False

        pump_index = int(pump_number.split('_')[1])

        if pump_selected == "all":
            return True
        elif pump_selected == "non_alcoholic":
            return 1 <= pump_index <= 7
        else:
            return 8 <= pump_index <= 15
        
    for pump_number, pin_number in settings['assignments'].items():
        if is_valid_pump(pump_number, pin_number):
            total_runtime += 20

    for pump_number, pin_number in settings['assignments'].items():
        status = ReadStatus()
        if status['control']['stop'] != 0:
            break

        if is_valid_pump(pump_number, pin_number):
            platform.ActivatePump(pump_number)
            progress, stopped = run_pump(platform, pump_number, total_runtime, progress)
            if stopped:
                print(f"The pump is {pump_selected} for cleaning stopped")
                control_logger.info(f"The pump is {pump_selected} for cleaning stopped")
                break
            
    status = ReadStatus()
    status['status']['active'] = 0
    status['control']['stop'] = 0
    status['control']['clean'] = ""
    WriteStatus(status)

# *****************************************
# Main Program Loop
# *****************************************
def main():
    # Clear all status bits on start up
    status = {}

    status['status'] = {
        "active": 0,
        "progress": 0
        }

    status['control'] = {
        "start": 0,
        "pause": 0,
        "stop": 0,
        "clean": "",
        "drink_name": ""
        }
    WriteStatus(status)

    try:
        while True:
            status = ReadStatus()
            if status['status']['active'] == 0:
                if status['status'].get('waiting') == 1:
                    wait_time = status['status'].get('wait_time', 0)

                    if wait_time > 0:
                        status['status']['wait_time'] -= 1
                        WriteStatus(status)
                    else:
                        status['status']['waiting'] = 0
                        status['control']['start'] = 1
                        idx = status['control'].get('infinite_index', 0)
                        print("The index is : ", idx)
                        control_logger.info(f'The index is : {idx}')
                        drink_list = status['control'].get('infinite_drinks', [])
                        print("The drink list is : ", drink_list)
                        control_logger.info(f'The drink list is :{drink_list}')
                        if len(drink_list) > 0:
                            print("The drink name is : ", drink_list[idx],)
                            status['control']['drink_name'] = drink_list[idx]
                            status['control']['infinite_index'] = (idx + 1) % len(drink_list)
                        WriteStatus(status)
                        
                elif status['control']['start'] == 1:
                    pourStripControl.startStrip()
                    event = 'Drink requested: ' + status['control']['drink_name']
                    control_logger.info(event)
                    print(f"event: {event}")
                    WriteLog(event)
                    PourDrink(status['control']['drink_name'])
                    
                    # After PourDrink, check infinite mode
                    status = ReadStatus()
                    if status['control'].get('infinite_mode') == 1 and not stop_threads:
                        status['status']['waiting'] = 1
                        status['status']['wait_time'] = 15
                        status['status']['progress'] = 0
                        status['status']['active'] = 0
                        status['status']['active_pumps'] = []
                        WriteStatus(status)
                        
                elif status['control']['clean'] != "":
                    event = 'Clean requested for pump: ' + str(status['control']['clean'])
                    control_logger.info(event)
                    WriteLog(event)
                    CleanPump(status['control']['clean'])

            time.sleep(1)

    except:
        raise
        print("Cleaning Up & Exiting...")
        quit()

if __name__ == "__main__":
    main()