#!/usr/bin/env python3
import time
import datetime
import os
import json
from version import __system_name__,__system_id__,__version__
import subprocess
import sys
import logging
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
def ReadStatus(retries=10):
    for i in range(retries):
        if not os.path.exists("status.json"): 
            if i < retries - 1:
                time.sleep(0.1)
                continue
            print("Error: status.json file not found. Creating a new one.")
            return create_default_status()

        try:
            with open("status.json", "r") as json_data_file:
                json_data_string = json_data_file.read().strip()

            if not json_data_string:
                print("Error: status.json is empty. Creating default.")
                return create_default_status()

            status = json.loads(json_data_string)
            return status

        except (IOError, OSError):
            if i < retries - 1:
                time.sleep(0.1)
                continue
            print("Error: Unable to read status.json file. Creating a new one.")
            return create_default_status()

        except (ValueError, json.JSONDecodeError) as e:
            print(f"Error: Invalid JSON in status.json. Creating a new one. Details: {e}")
            return create_default_status()
    return create_default_status()


def create_default_status():
    status = {
        "status": {
            "active": 0,
            "progress": 0,
            "active_pumps": []
        },
        "control": {
            "start": 0,
            "pause": 0,
            "stop": 0,
            "clean": "",
            "drink_name": "",
            "infinite_mode": 0,
            "infinite_drinks": [],
            "infinite_index": 0
        },
    }
    with open("status.json", "w") as json_data_file:
        json.dump(status, json_data_file, indent=4)
    
    return status

# def WriteStatus(status):
#     # *****************************************
#     # Write State Values to File
#     # *****************************************
#     json_data_string = json.dumps(status)
#     with open("status.json", 'w') as status_file:
#         status_file.write(json_data_string)
def WriteStatus(status, retries=10):
    tmp_file = "status_tmp.json"

    with open(tmp_file, 'w') as f:
        json.dump(status, f)

    for i in range(retries):
        try:
            os.replace(tmp_file, "status.json")  # atomic swap
            break
        except (IOError, OSError):
            if i < retries - 1:
                time.sleep(0.1)
            else:
                pass

def ReadSettings():
    """
    Read settings from 'settings.json'. If the file does not exist or cannot
    be read, a default settings object is created and written to the file.
    """
    settings_path = "settings.json"

    try:
        with open(settings_path, "r") as json_data_file:
            settings = json.load(json_data_file)
         
    except (IOError, OSError, json.JSONDecodeError):
        # Handle the case where the file does not exist or contains invalid JSON
        settings = {
            'inventory': {
                "pump_01": "rum",
                "pump_02": "vodka",
                "pump_03": "whiskey",
                "pump_04": "coke",
                "pump_05": "oj",
                "pump_06": "tequila",
                "pump_07": "marg_mix",
                "pump_08": "iced_tea"
            },
            'assignments': {
                "pump_01": 17,
                "pump_02": 27,
                "pump_03": 22,
                "pump_04": 23,
                "pump_05": 24,
                "pump_06": 25,
                "pump_07": 2,
                "pump_08": 3
            },
            'flowrate': 85
        }
        WriteSettings(settings)
    return settings

def WriteSettings(settings):
    """
    Write settings to 'settings.json'.
    """
    settings_path = "settings.json"
    with open(settings_path, 'w') as settings_file:
        json.dump(settings, settings_file, indent=4)

def ReadDrinkDB():
    # *****************************************
    # Read Settings from File
    # *****************************************

    # Read all lines of settings.json into an list(array)
    try:
        json_data_file = open("drink_db.json", "r",encoding='utf-8')
        json_data_string = json_data_file.read()
        drink_db = json.loads(json_data_string)
        json_data_file.close()
    except(IOError, OSError):
        # Issue with reading states JSON, so create one/write new one

        drink_db = {}

        drink_db['drinks'] = {
            "empty": "Empty"
            }

        drink_db['ingredients'] = {
            "empty": "Empty",
            }

    return(drink_db)

def WriteDrinkDB(drink_db):
    # *****************************************
    # Write drink_db to JSON file
    # *****************************************
    json_data_string = json.dumps(drink_db)
    with open("drink_db.json", 'w') as drinkdb_file:
        drinkdb_file.write(json_data_string)

def WriteLog(event):
    # *****************************************
    # Function: WriteLog
    # Input: str event
    # Description: Write event to event.log
    #  Event should be a string.
    # *****************************************
    now = str(datetime.datetime.now())
    now = now[0:19] # Truncate the microseconds

    logfile = open("./logs/events.log", "a")
    logfile.write(now + ' ' + event + '\n')
    logfile.close()

def ReadMetadata():
    metadata_path = "metadata.json"

    try:
        with open(metadata_path, "r") as metadata_file:
            metadata = json.load(metadata_file)

    except (IOError, OSError, json.JSONDecodeError):
        metadata = {
             "machine": {
        "last_cleaned_at": " ",
        "non_alcoholic_last_refilled": {
            "pump_01": " ",
            "pump_02": " ",
            "pump_03": " ",
            "pump_04": " ",
            "pump_05": " ",
            "pump_06": " ",
            "pump_07": " "
        }
    },
            "software": {
                "version": __version__
            },
            "system": {
                "id": __system_id__,
                "name": __system_name__
            },
            "server-config": {
                "ip": " ",
                "last_connected_at": " "
            }
        }

        WriteMetadata(metadata)

    return metadata

def WriteMetadata(metadata):
    metadata_path = "metadata.json"

    with open(metadata_path, "w") as metafile:
        json.dump(metadata, metafile, indent=4)
    
class MoniterDB:
    def __init__(self,filepath='moniter_db.json'):
        self.filepath = filepath
        self.data = self.read()
    
    def read(self):
        print(f'The moniter_db.json file path {os.path.exists(self.filepath)}')
        if not os.path.exists(self.filepath):
            print(f'The file not found {self.filepath}. Create new one')
            return self.create_default_moniterDB()
        try:
            with open(self.filepath, 'r', encoding='utf-8') as moniterDB_file:
                return json.load(moniterDB_file)
        except (IOError, OSError, json.JSONDecodeError):
            print(f'The file not found {self.filepath}. Create new one')
            return self.create_default_moniterDB()
    
    def write(self):
        try:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(self.data,f,indent=4)
        except (IOError, OSError, json.JSONDecodeError):
            print(f"Error while creating {self.filepath}")
    
    def create_default_moniterDB(self):
        self.data = {
            "insight": {
                "totalDrink": 0,
                "totalConsumed": 0,
                "consumeDrink": {},
                "mostConsumedDrink": ""
            },
            "ingridient":{}
        }
        self.write()
        return self.data
    
    def update_total_drink(self,new_total):
        self.data['insight']["totalDrink"] = new_total
        self.write()
    
    def update_total_consume_drink(self):
        return self.data['insight']["totalConsumed"]
    
    def consumpation(self,drinkName,count):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date =  datetime.datetime.now().strftime("%Y-%m-%d")
        
        consumeDrink = self.data["insight"]["consumeDrink"]

        if drinkName not in consumeDrink:
            consumeDrink[drinkName]={
                "consumeCount":count,
                "lastConsumedOn":now,
                "consumptionHistory":[{
                    "count": count,
                    "timestamp": date}
                ]
            }
        else:
            consumeDrink[drinkName]['consumeCount'] += count
            consumeDrink[drinkName]['lastConsumedOn'] = now
            consumeDrink[drinkName]['consumptionHistory'].append({
                    "count": count,
                    "timestamp": date})
           
            
        self.data['insight']["totalDrink"] += count 
        self.data['insight']["totalConsumed"] += count 
        
        self.data['insight']['mostConsumedDrink']=max(
            consumeDrink.items(),
            key=lambda x:x[1]['consumeCount']
        )[0]
        
        self.write()
    
    def ingridients(self, pump_number, actual_quantity, std_quantity):
        if 'ingridient' not in self.data:
            self.data['ingridient'] = {}
        
        ingridients = self.data['ingridient']

        if pump_number not in ingridients:
            ingridients[pump_number] = {
                "actualQty": actual_quantity,
                "stdQty": std_quantity
            }
        else:
            ingridients[pump_number]['actualQty'] = actual_quantity
            ingridients[pump_number]['stdQty'] = std_quantity

        self.write()

class LEDStripControl:
    def __init__(self,fileName):
        self.led_process = None
        self.filename = fileName
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.led_file_path = os.path.join(self.base_dir, "ws2812b", self.filename)
    
    def startStrip(self):
        if not os.path.exists(self.led_file_path):
            print(f"Error: LED control file {self.led_file_path} not found.")
            return
       
        if self.led_process is None:
            try:
                self.led_process = subprocess.Popen(
    ["/usr/local/bin/cb/venv/bin/python", self.led_file_path],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)
                print(f"LED STRP: {self.filename} Started")
            except Exception as e:
                print(f"Start Error: {e}")
        else:
            print(f"LED process for {self.filename} is already running.")

    def stopStrip(self):
        if self.led_process is not None:
            try:
                    self.led_process.terminate()
                    self.led_process.wait()
                    self.led_process = None
                    print(f"LED STRP : {self.filename} Stopped")

            except Exception as e:
                print(f"Stop Error: {e}")
                self.led_process.kill()
                self.led_process = None
                print(f"LED STRP: {self.filename} Stopped")
        else:
            print(f"LED Strip for {self.filename} is already stopped.")


class CustomLogger:
    def __init__(self,name,out_file,err_file):
        self.name=name
        self.out_file = out_file
        self.err_file=err_file
        
        os.makedirs("logs", exist_ok=True)
        
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        if not self.logger.handlers:

            formatter = logging.Formatter(
                "[%(asctime)s] "
                "[%(levelname)s] "
                "[%(name)s] "
                "%(message)s"
            )

            dir = os.getcwd() + "/logs/"
            out_handler = logging.FileHandler(
                os.path.join(dir, self.out_file),
              mode='a', encoding="utf-8"
            )

            out_handler.setLevel(logging.INFO)
            out_handler.setFormatter(formatter)

            err_handler = logging.FileHandler(
                os.path.join(dir, self.err_file),
              mode='a', encoding="utf-8"
            )

            err_handler.setLevel(logging.ERROR)
            err_handler.setFormatter(formatter)


            self.logger.addHandler(out_handler)
            self.logger.addHandler(err_handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message, exc_info=True)

    def critical(self, message):
        self.logger.critical(message, exc_info=True)