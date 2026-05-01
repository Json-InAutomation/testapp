# #!/usr/bin/python3
# # *****************************************
# # PiTender Control Python script
# # *****************************************
# #
# # Description: This script will dispense beverages.
# #
# # This script runs as a separate process from the Flask / Gunicorn
# # implementation which handles the web interface.
# #
# # *****************************************

# # Set this to False on Raspberry Pi Host ()
# prototype_mode = False
# prototype_mode = True # Comment out for normal operation
# # *****************************************
# # Imported Libraries
# # *****************************************

# #from __future__ import division
# import time
# import os
# import json
# import datetime
# from common import *
# import threading

# if(prototype_mode == True):
#     # Prototype Modules for Test Host (i.e. PC based testing)
#     from platform_prototype import PumpControl # Library for reading the ADC device
# else:
#     # Actual Modules for RasPi
#     from platform_raspi import PumpControl # Library for reading the ADC device

# stop_threads = False # Allows cancelling of drink pour threads 
# pause_threads = False  # Allows pausing and resuming of drink pour threads

# # *****************************************
# # Supporting Functions
# # *****************************************

# # def Pour(pump_number, waitTime, platform):
# #     print(f' * Thread: {pump_number} Started for {waitTime} seconds.')
# #     platform.ActivatePump(pump_number)
# #     for x in range(waitTime): 
# #         time.sleep(1)
# #         global stop_threads 
# #         if(stop_threads): 
# #             print(f' * Thread: {pump_number} cancelling.')
# #             break
# #         while pause_threads:
# #             time.sleep(0.5)  # Pause while `pause_threads` is True
# #         time.sleep(1)
# #     platform.DeActivatePump(pump_number)
# #     print(f' * Thread: {pump_number} finished.')
# def Pour(pump_number, waitTime, platform):
#     print(f' * Thread: {pump_number} Started for {waitTime} seconds.')
#     platform.ActivatePump(pump_number)
#     for x in range(waitTime): 
#         time.sleep(1)
#         if pause_threads:  # Check global pause state
#             while pause_threads:
#                 time.sleep(1)  # Wait until pause_threads is reset
#         global stop_threads 
#         if stop_threads: 
#             print(f' * Thread: {pump_number} cancelling.')
#             break
#     platform.DeActivatePump(pump_number)
#     print(f' * Thread: {pump_number} finished.')

# def DelayedPour(pump_number, runtime, platform, delay):
#     time.sleep(delay)
#     Pour(pump_number, runtime, platform)


# def PourDrink(drink_name):
#     drink_db = ReadDrinkDB()
#     if drink_name in drink_db['drinks']:
#         # Set Active Status
#         status = ReadStatus()
#         status['status']['active'] = 1
#         WriteStatus(status)

#         total_runtime = 0
#         percent_progress = 0
#         current_count = 0
#         global stop_threads, pause_threads

#         pause_threads = False  # Initialize pause flag

#         # Initialize Platform Object
#         settings = ReadSettings()
#         platform = PumpControl(settings)
#         if 'percentage' not in settings:
#             settings['percentage'] = {}

#         print(f'Starting to prepare {drink_name}')

#         # Calculate total runtime
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             total_runtime = max(total_runtime, int(pump_runtime * (settings['flowrate'] / 100)))

#         print(f'Total Runtime: {total_runtime}')

#         # Create and start threads to dispense each ingredient
#         pumpThreads = []
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             pump_number = 'none'
#             for index, value in settings['inventory'].items():
#                 if value == drink_ingredient:
#                     pump_number = index
#                     break  

            
#             calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
#             if pump_number == 'pump_16':  # Mixture pump
#                 delay = 4 #mixture pump pause for 4 seconds
#                 pump_t = threading.Thread(target=DelayedPour, args=(pump_number, calculated_pump_runtime, platform, delay))
#             else:
#                 pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
            
#             pumpThreads.append(pump_t)
            
#             consumed_quantity = int(pump_runtime * (settings['flowrate'] / 100))
#             if pump_number in settings['quantity']:
                
#                 standard_quantity = settings['quantity'][pump_number]
#                 settings['in_quantity'][pump_number] = max(0, standard_quantity - consumed_quantity)
                
#                 # calculation related to find how much % availaible drink 
#                 # settings['percentage'][pump_number] = (settings['in_quantity'][pump_number] * 100)/standard_quantity
                
                
        

#         # Start the pump threads
#         for thread in pumpThreads:
#             thread.start()

#         # Monitor and report progress to WebUI
#         # for x in range(total_runtime):
#         #     current_count += 1
#         #     status = ReadStatus()
#         #     if status['control']['stop'] == 1:
#         #         stop_threads = True
#         #         time.sleep(2)
#         #         stop_threads = False
#         #         break
#         #     percent_progress = int((current_count / total_runtime) * 100)
#         #     status['status']['progress'] = percent_progress
#         #     WriteStatus(status)
#         #     time.sleep(1)
#         for x in range(total_runtime):
#             global stop_threads, pause_threads
#             if stop_threads:
#                 break
#             while pause_threads:
#                 time.sleep(0.5)  # Pause while `pause_threads` is True
#             current_count += 1
#             percent_progress = int((current_count / total_runtime) * 100)
#             status = ReadStatus()
#             status['status']['progress'] = percent_progress
#             print(status['status']['progress'])
#             WriteStatus(status)
#             time.sleep(1)

#         # Wait for threads to finish
#         for thread in pumpThreads:
#             thread.join()

#         print('Finished dispensing drink.')
#         # Write updated settings to file after updating quantities for all pumps
#         WriteSettings(settings)

#         print('Finished. Cleaning up status file.')
#         status['status']['active'] = 0
#         status['control']['start'] = 0
#         status['control']['stop'] = 0
#         WriteStatus(status)
#     else:
#         print('Error, no drinks match that name.')

      
# def CleanPump(pump_selected):
#     print(f"The selected pump is {pump_selected} for cleaning")
#     settings = ReadSettings()
#     status = ReadStatus()
#     status['status']['active'] = 1
#     WriteStatus(status)

#     # Initialize Platform Object
#     platform = PumpControl(settings)

#     if pump_selected == "all":
#         total_runtime = 0
#         progress = 0

#         for pump_number, pin_number in settings['assignments'].items():
#             if pin_number != 0:
#                 total_runtime += 20

#         for pump_number, pin_number in settings['assignments'].items():

#             if (pin_number != 0) and (status['control']['stop'] == 0):
#                 platform.ActivatePump(pump_number)
#                 for index in range(20):
#                     status = ReadStatus()
#                     if (status['control']['stop'] == 0):
#                         progress += 1
#                         status['status']['progress'] = int(100 * (progress / total_runtime))
#                         WriteStatus(status)
#                         time.sleep(1) # Run for X seconds
#                     else:
#                         break
#                 platform.DeActivatePump(pump_number)
#     else:
#         for pump_number, pin_number in settings['assignments'].items():
#             if (pump_selected == pump_number):
#                 platform.ActivatePump(pump_number)
#                 for index in range(21):
#                     status = ReadStatus()
#                     if (status['control']['stop'] == 0):
#                         status['status']['progress'] = index*5
#                         WriteStatus(status)
#                         time.sleep(1) # Run for X seconds
#                     else:
#                         break
#                 platform.DeActivatePump(pump_number)


#     status['status']['active'] = 0
#     status['control']['stop'] = 0
#     status['control']['clean'] = ""
#     WriteStatus(status)


# # *****************************************
# # Main Program Loop
# # *****************************************
# def main():
#     # Clear all status bits on start up
#     status = {}

#     status['status'] = {
#         "active": 0,
#         "progress": 0
#         }

#     status['control'] = {
#         "start": 0,
#         "pause": 0,
#         "stop": 0,
#         "clean": "",
#         "drink_name": ""
#         }
#     WriteStatus(status)

#     try:
#         while True:
#             status = ReadStatus()
#             if status['status']['active'] == 0:
#                 if status['control']['start'] == 1:
#                     event = 'Drink requested: ' + status['control']['drink_name']
#                     WriteLog(event)
#                     PourDrink(status['control']['drink_name'])
#                 elif status['control']['clean'] != "":
#                     event = 'Clean requested for pump: ' + str(status['control']['clean'])
#                     WriteLog(event)
#                     CleanPump(status['control']['clean'])

#             time.sleep(1)

#     except:
#         raise
#         print("Cleaning Up & Exiting...")
#         quit()

# if __name__ == "__main__":
#     main()


# #!/usr/bin/python3
# # *****************************************
# # PiTender Control Python script
# # *****************************************
# #
# # Description: This script will dispense beverages.
# #
# # This script runs as a separate process from the Flask / Gunicorn
# # implementation which handles the web interface.
# #
# # *****************************************

# # Set this to False on Raspberry Pi Host ()
# prototype_mode = False
# #prototype_mode = True # Comment out for normal operation
# # *****************************************
# # Imported Libraries
# # *****************************************

# #from __future__ import division
# import time
# import os
# import json
# import datetime
# from common import *
# import threading

# if(prototype_mode == True):
#     # Prototype Modules for Test Host (i.e. PC based testing)
#     from platform_prototype import PumpControl # Library for reading the ADC device
# else:
#     # Actual Modules for RasPi
#     from platform_raspi import PumpControl # Library for reading the ADC device

# stop_threads = False
# pause_threads = False

# def Pour(pump_number, waitTime, platform):
#     print(f' * Thread: {pump_number} Started for {waitTime} seconds.')
#     platform.ActivatePump(pump_number)
#     for x in range(waitTime): 
#         time.sleep(1)
#         global stop_threads 
#         status = ReadStatus()
#         if status['control']['pause'] == 1:
#             print(f' * Thread: {pump_number} paused.')
#             platform.DeActivatePump(pump_number)
#             while status['control']['pause'] == 1:
#                 time.sleep(1)  
#                 status = ReadStatus()
#         platform.ActivatePump(pump_number)  
#         if (stop_threads): 
#             print(f' * Thread: {pump_number} cancelling. Threads is {stop_threads}')
#             print(f' * Thread: {pump_number} cancelling.')
#             break
#     platform.DeActivatePump(pump_number)
#     print(f' * Thread: {pump_number} finished.')

# # def DelayedPour(pump_number, runtime, platform, delay):
# #     time.sleep(delay)
# #     Pour(pump_number, runtime, platform)

# def MixerControl(platform, delay=5):
#     global stop_threads, pause_threads
#     print("* MixerControl: Activating pump_16 (GPIO 21).")
#     platform.ActivatePump("pump_16")  # Activates GPIO 21
#     while True:
#         status = ReadStatus()
#         progress = status['status']['progress']
#         if progress >= 100 or stop_threads:  
#             break
#         if pause_threads:
#             platform.DeActivatePump("pump_16") 
#             while pause_threads:  
#                 print("* MixerControl: Paused. Waiting to resume...")
#                 time.sleep(1)
#             platform.ActivatePump("pump_16") 
#             print("* MixerControl: Resuming...")
#         time.sleep(1)  
#     print(" * MixerControl: Continuing for additional seconds after 100% progress.")
#     time.sleep(delay) 
#     platform.DeActivatePump("pump_16") 
#     print(" * MixerControl: Finished.")
    
# def PourDrink(drink_name):
#     drink_db = ReadDrinkDB()
#     if drink_name in drink_db['drinks']:
#         status = ReadStatus()
#         status['status']['active'] = 1
#         WriteStatus(status)

#         total_runtime = 0
#         current_count = 0
#         global stop_threads, pause_threads

#         # Initialize Platform Object
#         settings = ReadSettings()
#         platform = PumpControl(settings)
#         if 'percentage' not in settings:
#             settings['percentage'] = {}

#         print(f"Starting to prepare {drink_name}")

#         # Calculate total runtime
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             total_runtime = max(total_runtime, int(pump_runtime * (settings['flowrate'] / 100)))

#         print(f"Total Runtime: {total_runtime}") 
#         # Create and start threads to dispense each ingredient
#         pumpThreads = []
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             pump_number = 'none'
#             for index, value in settings['inventory'].items():
#                 if value == drink_ingredient:
#                     pump_number = index
#                     break  

#             calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
#             pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
#             pumpThreads.append(pump_t)

#             consumed_quantity = int(pump_runtime * (settings['flowrate'] / 100))
#             if pump_number in settings['quantity']:
#                 standard_quantity = settings['quantity'][pump_number]
#                 settings['in_quantity'][pump_number] = max(0, standard_quantity - consumed_quantity)

#         # Start the pump threads
#         for thread in pumpThreads:
#             thread.start()

#         # Monitor progress and start MixerControl at 50% progress
#         mixer_started = False
#         mixer_thread = None

#         for x in range(total_runtime):
#             current_count += 1
#             status = ReadStatus()

#             # Stop condition
#             if status['control']['stop'] == 1:
#                 stop_threads = True
#                 time.sleep(2)
#                 stop_threads = False
#                 break

#             # Pause condition
#             if status['control']['pause'] == 1:
#                 percent_progress = int((current_count / total_runtime) * 100)
#                 status['status']['progress'] = percent_progress
#                 WriteStatus(status)
#                 while status['control']['pause'] == 1:
#                     time.sleep(1)
#                     status = ReadStatus()

#             # Update progress
#             percent_progress = int((current_count / total_runtime) * 100)
#             status['status']['progress'] = percent_progress
#             WriteStatus(status)

#             # Start MixerControl at 50% progress
#             print(f"The percentage is {percent_progress}")
#             if percent_progress >= 50 and not mixer_started:
#                 mixer_thread = threading.Thread(target=MixerControl, args=(platform,))
#                 mixer_thread.start()
#                 mixer_started = True

#             time.sleep(1)

#         # Wait for all pump threads to finish
#         for thread in pumpThreads:
#             thread.join()

#         # Wait for MixerControl thread to finish if started
#         if mixer_thread:
#             mixer_thread.join()

#         print("Finished dispensing drink.")
#         WriteSettings(settings)

#         print("Finished. Cleaning up status file.")
#         status['status']['active'] = 0
#         status['control']['start'] = 0
#         status['control']['stop'] = 0
#         WriteStatus(status)
#     else:
#         print("Error, no drinks match that name.")
        
# def CleanPump(pump_selected):
#     print(f"The selected pump is {pump_selected} for cleaning")
#     settings = ReadSettings()
#     status = ReadStatus()
#     status['status']['active'] = 1
#     WriteStatus(status)

#     # Initialize Platform Object
#     platform = PumpControl(settings)

#     if pump_selected == "all":
#         total_runtime = 0
#         progress = 0

#         for pump_number, pin_number in settings['assignments'].items():
#             if pin_number != 0:
#                 total_runtime += 20

#         for pump_number, pin_number in settings['assignments'].items():

#             if (pin_number != 0) and (status['control']['stop'] == 0):
#                 platform.ActivatePump(pump_number)
#                 for index in range(20):
#                     status = ReadStatus()
#                     if (status['control']['stop'] == 0):
#                         progress += 1
#                         status['status']['progress'] = int(100 * (progress / total_runtime))
#                         WriteStatus(status)
#                         time.sleep(1) # Run for X seconds
#                     else:
#                         break
#                 platform.DeActivatePump(pump_number)
#     else:
#         for pump_number, pin_number in settings['assignments'].items():
#             if (pump_selected == pump_number):
#                 platform.ActivatePump(pump_number)
#                 for index in range(21):
#                     status = ReadStatus()
#                     if (status['control']['stop'] == 0):
#                         status['status']['progress'] = index*5
#                         WriteStatus(status)
#                         time.sleep(1) # Run for X seconds
#                     else:
#                         break
#                 platform.DeActivatePump(pump_number)


#     status['status']['active'] = 0
#     status['control']['stop'] = 0
#     status['control']['clean'] = ""
#     WriteStatus(status)


# # *****************************************
# # Main Program Loop
# # *****************************************
# def main():
#     # Clear all status bits on start up
#     status = {}

#     status['status'] = {
#         "active": 0,
#         "progress": 0
#         }

#     status['control'] = {
#         "start": 0,
#         "pause": 0,
#         "stop": 0,
#         "clean": "",
#         "drink_name": ""
#         }
#     WriteStatus(status)

#     try:
#         while True:
#             status = ReadStatus()
#             if status['status']['active'] == 0:
#                 if status['control']['start'] == 1:
#                     event = 'Drink requested: ' + status['control']['drink_name']
#                     WriteLog(event)
#                     PourDrink(status['control']['drink_name'])
#                 elif status['control']['clean'] != "":
#                     event = 'Clean requested for pump: ' + str(status['control']['clean'])
#                     WriteLog(event)
#                     CleanPump(status['control']['clean'])

#             time.sleep(1)

#     except:
#         raise
#         print("Cleaning Up & Exiting...")
#         quit()

# if __name__ == "__main__":
#     main()

# #!/usr/bin/python3
# # *****************************************
# # PiTender Control Python script
# # *****************************************
# #
# # Description: This script will dispense beverages.
# #
# # This script runs as a separate process from the Flask / Gunicorn
# # implementation which handles the web interface.
# #
# # *****************************************

# # Set this to False on Raspberry Pi Host ()
# prototype_mode = False
# #prototype_mode = True # Comment out for normal operation
# # *****************************************
# # Imported Libraries
# # *****************************************

# #from __future__ import division
# import time
# import os
# import json
# import datetime
# from common import *
# import threading

# if(prototype_mode == True):
#     # Prototype Modules for Test Host (i.e. PC based testing)
#     from platform_prototype import PumpControl # Library for reading the ADC device
# else:
#     # Actual Modules for RasPi
#     from platform_raspi import PumpControl # Library for reading the ADC device

# stop_threads = False
# pause_threads = False

# def Pour(pump_number, waitTime, platform):
#     print(f' * Thread: {pump_number} Started for {waitTime} seconds.')
#     platform.ActivatePump(pump_number)
#     for x in range(waitTime): 
#         time.sleep(1)
#         global stop_threads 
#         status = ReadStatus()
#         if status['control']['pause'] == 1:
#             print(f' * Thread: {pump_number} paused.')
#             platform.DeActivatePump(pump_number)
#             while status['control']['pause'] == 1:
#                 time.sleep(1)  
#                 status = ReadStatus()
#         platform.ActivatePump(pump_number)  
#         if (stop_threads): 
#             print(f' * Thread: {pump_number} cancelling. Threads is {stop_threads}')
#             print(f' * Thread: {pump_number} cancelling.')
#             break
#     platform.DeActivatePump(pump_number)
#     print(f' * Thread: {pump_number} finished.')

# # def DelayedPour(pump_number, runtime, platform, delay):
# #     time.sleep(delay)
# #     Pour(pump_number, runtime, platform)

# # def MixerControl(platform, delay=5):
# #     global stop_threads, pause_threads
# #     print("* MixerControl: Activating pump_16 (GPIO 21).")
# #     platform.ActivatePump("pump_16")  # Activates GPIO 21
# #     while True:
# #         status = ReadStatus()
# #         progress = status['status']['progress']
# #         if progress >= 100 or stop_threads:  
# #             break
# #         if pause_threads:
# #             platform.DeActivatePump("pump_16") 
# #             while pause_threads:  
# #                 print("* MixerControl: Paused. Waiting to resume...")
# #                 time.sleep(1)
# #             platform.ActivatePump("pump_16") 
# #             print("* MixerControl: Resuming...")
# #         time.sleep(1)  
# #     print(" * MixerControl: Continuing for additional seconds after 100% progress.")
# #     time.sleep(delay) 
# #     platform.DeActivatePump("pump_16") 
# #     print(" * MixerControl: Finished.")
  
# def PourDrink(drink_name):
#     drink_db = ReadDrinkDB()
#     if drink_name in drink_db['drinks']:
#         status = ReadStatus()
#         status['status']['active'] = 1
#         WriteStatus(status)

#         total_runtime = 0
#         current_count = 0
#         global stop_threads, pause_threads

#         # Initialize Platform Object
#         settings = ReadSettings()
#         platform = PumpControl(settings)
#         if 'percentage' not in settings:
#             settings['percentage'] = {}

#         print(f"Starting to prepare {drink_name}")

#         # Calculate total runtime
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             total_runtime = max(total_runtime, int(pump_runtime * (settings['flowrate'] / 100)))

#         print(f"Total Runtime: {total_runtime}") 
#         # Create and start threads to dispense each ingredient
#         pumpThreads = []
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             pump_number = 'none'
#             for index, value in settings['inventory'].items():
#                 if value == drink_ingredient:
#                     pump_number = index
#                     break  
#             if pump_number == 'pump_16':
#                 continue  # Skip creating the thread for pump_16
#             calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
#             pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
#             pumpThreads.append(pump_t)

#             consumed_quantity = int(pump_runtime * (settings['flowrate'] / 100))
#             if pump_number in settings['quantity']:
#                 standard_quantity = settings['quantity'][pump_number]
#                 settings['in_quantity'][pump_number] = max(0, standard_quantity - consumed_quantity)

#         # Start the pump threads
#         for thread in pumpThreads:
#             thread.start()

#         # # Monitor progress and start MixerControl at 50% progress
#         # mixer_started = False
#         # mixer_thread = None

#         for x in range(total_runtime):
#             current_count += 1
#             status = ReadStatus()

#             # Stop condition
#             if status['control']['stop'] == 1:
#                 stop_threads = True
#                 time.sleep(2)
#                 stop_threads = False
#                 break

#             # Pause condition
#             if status['control']['pause'] == 1:
#                 percent_progress = int((current_count / total_runtime) * 100)
#                 status['status']['progress'] = percent_progress
#                 WriteStatus(status)
#                 while status['control']['pause'] == 1:
#                     time.sleep(1)
#                     status = ReadStatus()

#             # Update progress
#             percent_progress = int((current_count / total_runtime) * 100)
#             status['status']['progress'] = percent_progress
#             WriteStatus(status)

#             # # Start MixerControl at 50% progress
#             # print(f"The percentage is {percent_progress}")
#             # if percent_progress >= 50 and not mixer_started:
#             #     mixer_thread = threading.Thread(target=MixerControl, args=(platform,))
#             #     mixer_thread.start()
#             #     mixer_started = True

#             time.sleep(1)

#         # Wait for all pump threads to finish
#         for thread in pumpThreads:
#             thread.join()

#         # Wait for MixerControl thread to finish if started
#         # if mixer_thread:
#         #     mixer_thread.join()

#         print("Finished dispensing drink.")
#         WriteSettings(settings)

#         print("Finished. Cleaning up status file.")
#         status['status']['active'] = 0
#         status['control']['start'] = 0
#         status['control']['stop'] = 0
#         WriteStatus(status)
#     else:
#         print("Error, no drinks match that name.")
        
# def CleanPump(pump_selected):
#     print(f"The selected pump is {pump_selected} for cleaning")
#     settings = ReadSettings()
#     status = ReadStatus()
#     status['status']['active'] = 1
#     WriteStatus(status)

#     # Initialize Platform Object
#     platform = PumpControl(settings)

#     if pump_selected == "all":
#         total_runtime = 0
#         progress = 0

#         for pump_number, pin_number in settings['assignments'].items():
#             if pin_number != 0:
#                 total_runtime += 20

#         for pump_number, pin_number in settings['assignments'].items():

#             if (pin_number != 0) and (status['control']['stop'] == 0):
#                 platform.ActivatePump(pump_number)
#                 for index in range(20):
#                     status = ReadStatus()
#                     if (status['control']['stop'] == 0):
#                         progress += 1
#                         status['status']['progress'] = int(100 * (progress / total_runtime))
#                         WriteStatus(status)
#                         time.sleep(1) # Run for X seconds
#                     else:
#                         break
#                 platform.DeActivatePump(pump_number)
#     else:
#         for pump_number, pin_number in settings['assignments'].items():
#             if (pump_selected == pump_number):
#                 platform.ActivatePump(pump_number)
#                 for index in range(21):
#                     status = ReadStatus()
#                     if (status['control']['stop'] == 0):
#                         status['status']['progress'] = index*5
#                         WriteStatus(status)
#                         time.sleep(1) # Run for X seconds
#                     else:
#                         break
#                 platform.DeActivatePump(pump_number)


#     status['status']['active'] = 0
#     status['control']['stop'] = 0
#     status['control']['clean'] = ""
#     WriteStatus(status)


# # *****************************************
# # Main Program Loop
# # *****************************************
# def main():
#     # Clear all status bits on start up
#     status = {}

#     status['status'] = {
#         "active": 0,
#         "progress": 0
#         }

#     status['control'] = {
#         "start": 0,
#         "pause": 0,
#         "stop": 0,
#         "clean": "",
#         "drink_name": ""
#         }
#     WriteStatus(status)

#     try:
#         while True:
#             status = ReadStatus()
#             if status['status']['active'] == 0:
#                 if status['control']['start'] == 1:
#                     event = 'Drink requested: ' + status['control']['drink_name']
#                     WriteLog(event)
#                     PourDrink(status['control']['drink_name'])
#                 elif status['control']['clean'] != "":
#                     event = 'Clean requested for pump: ' + str(status['control']['clean'])
#                     WriteLog(event)
#                     CleanPump(status['control']['clean'])

#             time.sleep(1)

#     except:
#         raise
#         print("Cleaning Up & Exiting...")
#         quit()

# if __name__ == "__main__":
#     main()



# def PourDrink(drink_name):
#     drink_db = ReadDrinkDB()
#     if drink_name in drink_db['drinks']:
#         status = ReadStatus()
#         status['status']['active'] = 1
#         WriteStatus(status)

#         total_runtime = 0
#         current_count = 0
#         global stop_threads, pause_threads

#         # Initialize Platform Object
#         settings = ReadSettings()
#         platform = PumpControl(settings)
#         if 'percentage' not in settings:
#             settings['percentage'] = {}

#         print(f"Starting to prepare {drink_name}")

#         # Calculate total runtime
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             total_runtime = max(total_runtime, int(pump_runtime * (settings['flowrate'] / 100)))

#         print(f"Total Runtime: {total_runtime}") 
#         # Create and start threads to dispense each ingredient
#         pumpThreads = []
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             pump_number = 'none'
#             for index, value in settings['inventory'].items():
#                 if value == drink_ingredient:
#                     pump_number = index
#                     break  
#             print(f"The mixer pump is a : {pump_number} ",pump_number == 'pump_16') 
#             if pump_number == 'pump_16':
#                 continue  # Skip creating the thread for pump_16
            
#             calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
#             pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
#             pumpThreads.append(pump_t)

#             consumed_quantity = int(pump_runtime * (settings['flowrate'] / 100))
#             if pump_number in settings['quantity']:
#                 standard_quantity = settings['quantity'][pump_number]
#                 settings['in_quantity'][pump_number] = max(0, standard_quantity - consumed_quantity)

#         # Start the pump threads
#         for thread in pumpThreads:
#             thread.start()
            
#         mixer_started = False = False

#         for x in range(total_runtime):
#             current_count += 1
#             status = ReadStatus()

#             # Stop condition
#             if status['control']['stop'] == 1:
#                 stop_threads = True
#                 time.sleep(2)
#                 stop_threads = False
#                 break

#             # Pause condition
#             if status['control']['pause'] == 1:
#                 percent_progress = int((current_count / total_runtime) * 100)
#                 status['status']['progress'] = percent_progress
#                 WriteStatus(status)
#                 while status['control']['pause'] == 1:
#                     time.sleep(1)
#                     status = ReadStatus()

#             # Update progress
#             percent_progress = int((current_count / total_runtime) * 100)
#             status['status']['progress'] = percent_progress
#             WriteStatus(status)
            
#             if percent_progress >= 50 and not  mixer_started:
#                 # Create and start the pump_16 thread
#                 pump_number = 'pump_16'  # Assign pump_16
#                 calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
#                 pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
#                 pumpThreads.append(pump_t)
#                 pump_t.start()
#                 mixer_started = True
#             time.sleep(1)

#         # Wait for all pump threads to finish
#         for thread in pumpThreads:
#             thread.join()



#         print("Finished dispensing drink.")
#         WriteSettings(settings)

#         print("Finished. Cleaning up status file.")
#         status['status']['active'] = 0
#         status['control']['start'] = 0
#         status['control']['stop'] = 0
#         WriteStatus(status)
#     else:
#         print("Error, no drinks match that name.")
        
# def ReadStatus():
#     # *****************************************
#     # Read State Values from File
#     # *****************************************
#     try:
#         with open("status.json", "r") as json_data_file:
#             json_data_string = json_data_file.read().strip()  # Strip whitespace
#             # Check if the file is empty or contains only whitespace
#             if not json_data_string:
#                 raise ValueError("status.json is empty.")

#             # Attempt to parse the JSON data
#             status = json.loads(json_data_string)
            

#     except (IOError, OSError):
#         print("Error: Unable to read status.json file. Creating a new one.")
#         status = {
#             "status": {
#                 "active": 0,
#                 "progress": 0,
#             },
#             "control": {
#                 "start": 0,
#                 "pause": 0,
#                 "stop": 0,
#                 "clean": "",
#                 "drink_name": "",
#             },
#         }
#         with open("status.json", "w") as json_data_file:
#             json.dump(status, json_data_file, indent=4)

#     except (ValueError, json.JSONDecodeError) as e:
#         print(f"Error: Invalid JSON in status.json. Creating a new one. Details: {e}")
#         status = {
#             "status": {
#                 "active": 0,
#                 "progress": 0,
#             },
#             "control": {
#                 "start": 0,
#                 "pause": 0,
#                 "stop": 0,
#                 "clean": "",
#                 "drink_name": "",
#             },
#         }
#         with open("status.json", "w") as json_data_file:
#             json.dump(status, json_data_file, indent=4)

#     return status


# def ReadStatus():
#     # *****************************************
#     # Read State Values from File
#     # *****************************************
#     try:

#         json_data_file = open("status.json", "r")
#         json_data_string = json_data_file.read()
#         status = json.loads(json_data_string)
#         json_data_file.close()
  
#     except(IOError, OSError):
#         # Issue with reading states JSON, so create one/write new one
#         status = {}

#         status['status'] = {
#             "active": 0,
#             "progress": 0
#             }
#         status['control'] = {
#             "start": 0,
#             "pause": 0,
#             "stop": 0,
#             "clean": "",
#             "drink_name": ""
#             }

#         WriteStatus(status)
        
#     except (ValueError, json.JSONDecodeError) as e:
#         print(f"Error: Invalid JSON in status.json. Creating a new one. Details: {e}")
        
#     return(status)

# def ReadStatus():
#     # *****************************************
#     # Read State Values from File
#     # *****************************************
#     try:

#         json_data_file = open("status.json", "r")
#         json_data_string = json_data_file.read()
#         status = json.loads(json_data_string)
#         json_data_file.close()
  
#     except(IOError, OSError):
#         # Issue with reading states JSON, so create one/write new one
#         status = {}

#         status['status'] = {
#             "active": 0,
#             "progress": 0
#             }
#         status['control'] = {
#             "start": 0,
#             "pause": 0,
#             "stop": 0,
#             "clean": "",
#             "drink_name": ""
#             }

#         WriteStatus(status)
        
#     except (ValueError, json.JSONDecodeError) as e:
#         print(f"Error: Invalid JSON in status.json. Creating a new one. Details: {e}")
        
#     return(status)

   # Stop condition
            # if (status['control']['stop'] == 1):
            #     stop_threads = True
            #     time.sleep(2)
            #     stop_threads = False
            #     break
            
            #############Working code #####################################33
            # def Pour(pump_number, waitTime, platform):
#     print(f' * Thread: {pump_number} Started for {waitTime} seconds.')
#     platform.ActivatePump(pump_number)
#     for x in range(waitTime): 
#         time.sleep(1)
#         global stop_threads 
#         status = ReadStatus()
#         if status['control']['pause'] == 1:
#             print(f' * Thread: {pump_number} paused.')
#             platform.DeActivatePump(pump_number)
#             while status['control']['pause'] == 1:
#                 time.sleep(1)  
#                 status = ReadStatus()
#             print(f' * Thread: {pump_number} was paused. Stopping pouring completely.')
#             break 
#         # platform.ActivatePump(pump_number)  
#         if (stop_threads): 
#             print(f' * Thread: {pump_number} cancelling. Threads is {stop_threads}')
#             break 
        
#     platform.DeActivatePump(pump_number)
#     print(f' * Thread: {pump_number} finished.')

####################Common.py code ###############
# def ReadStatus():
#     if not os.path.exists("status.json"): 
#         print("Error: status.json file not found. Creating a new one.")
#         return create_default_status()

#     try:
#         with open("status.json", "r") as json_data_file:
#             json_data_string = json_data_file.read().strip()

#         status = json.loads(json_data_string)
    
#     except (IOError, OSError):
#         print("Error: Unable to read status.json file. Creating a new one.")
#         status = create_default_status()

#     except (ValueError, json.JSONDecodeError) as e:
#         print(f"Error: Invalid JSON in status.json. Creating a new one. Details: {e}")

#     return status  
 
####################Common.py code ###############
# def Pour(pump_number, waitTime, platform):
#     print(f' * Thread: {pump_number} Started for {waitTime} seconds.')
#     platform.ActivatePump(pump_number)
#     for x in range(waitTime): 
#         time.sleep(1)
#         global stop_threads 
#         status = ReadStatus()


#         if status['control']['pause'] == 1:
#             print(f' * Thread: {pump_number} paused.')
#             platform.DeActivatePump(pump_number)
#             while status['control']['pause'] == 1:
#                 time.sleep(1)  
#                 status = ReadStatus() 
#             print(f' * Thread: {pump_number} resuming.')
#             platform.ActivatePump(pump_number) 
        
#         # platform.ActivatePump(pump_number)  
#         if (stop_threads == True): 
#             print(f' * Thread: {pump_number} cancelling. Threads is {stop_threads}') 
#             platform.DeActivatePump(pump_number)
#             return
        
#     platform.DeActivatePump(pump_number)
#     print(f' * Thread: {pump_number} finished.')



# def Pour(pump_number, waitTime, platform):
#     print(f' * Thread: {pump_number} Started for {waitTime} seconds.')
#     platform.ActivatePump(pump_number)
#     for x in range(waitTime): 
#         time.sleep(1)
#         global stop_threads 
#         status = ReadStatus()

#         if (status['control']['stop']==1):
#             print(f' * Thread: {pump_number} cancelling. Threads is {stop_threads}') 
#             platform.DeActivatePump(pump_number)
#             return

#         if status['control']['pause'] == 1:
#             print(f' * Thread: {pump_number} paused.')
#             platform.DeActivatePump(pump_number)
#             while status['control']['pause'] == 1:
#                 time.sleep(1)  
#                 status = ReadStatus() 
#             print(f' * Thread: {pump_number} resuming.')
#             platform.ActivatePump(pump_number) 
        
#         # platform.ActivatePump(pump_number)  
#         if (stop_threads): 
#             print(f' * Thread: {pump_number} cancelling. Threads is {stop_threads}') 
#             platform.DeActivatePump(pump_number)
#             return
        
#     platform.DeActivatePump(pump_number)
#     print(f' * Thread: {pump_number} finished.')