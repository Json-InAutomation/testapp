from flask import Flask, flash, url_for, request, render_template, make_response, jsonify, redirect
from flask_cors import CORS
import subprocess
import time
import os
import json
from datetime import datetime
from common import *
from werkzeug.utils import secure_filename
import re
import platform
import random,string
if platform.system() == "Windows":
    print(platform.system())
    from platform_prototype import SensorSignal  
else:
    from platform_raspi import SensorSignal  
from version import __system_name__,__system_id__
import threading
from network import find_server
from socket_client import start_socket_client
# import socketio
# import socket
# SERVER_PORT = 5500
# CLIENT_PORT =  5000

# def get_my_ip():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     try:
#         s.connect(("192.168.31.1", 80))
#         ip = s.getsockname()[0]
#     finally:
#         s.close()
#     return ip


# def get_subnet(ip):
#     parts = ip.split(".")
#     return f"{parts[0]}.{parts[1]}.{parts[2]}."

# def find_server(port=SERVER_PORT):
#     my_ip = get_my_ip()
#     subnet = get_subnet(my_ip)

#     print(f"My IP     : {my_ip}")
#     print(f"Subnet    : {subnet}0/24")
#     print("Scanning for server...")
    
#     for i in range(1, 255):
#         ip = subnet + str(i)
#         print(ip)
#         try:
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             s.settimeout(0.15)
#             s.connect((ip, port))
#             s.close()
#             print(f"✅ Server found at: {ip}")
#             return ip
#         except:
#             pass

#     print("❌ Server not found")
#     return None

# # networkIpAddress = find_server()

# DEVICE_ID = networkIpAddress
# SERVER_URL = f"http://{networkIpAddress}:{SERVER_PORT}"

# POLLING_FALLBACK = os.getenv('POLLING_FALLBACK', 'true').lower() == 'true'  

app = Flask(__name__)
CORS(app)

# sio = socketio.Client(
#     logger=True,
#     engineio_logger=True,
#     reconnection=True,
#     reconnection_attempts=5,
#     reconnection_delay=1,
#     reconnection_delay_max=5
# )

# CONSUMPTION_FILE = "moniter_db.json"

# last_modification_file = 0

moniterData = MoniterDB()
@app.route('/', methods=['POST','GET'])
def index():
    print(platform.system())
    settings = ReadSettings()
    drink_db = ReadDrinkDB()
    show_navbar = False  # Hide the navbar on this page
    drinklist = {}
    num_drinks = 0
    moniterDB = MoniterDB()
    moniterDB.write()

    for drink_name, drink_details in drink_db['drinks'].items():
        # Cycle through each ingredient in the drink recipe
        for drink_ingredients in drink_details['ingredients'].items():
            matched_ingredient = False

            # Cycle through each ingredient in the inventory and check against the recipe
            for ingredients_available in settings['inventory'].items():
                if (ingredients_available[1] == drink_ingredients[0]):
                    matched_ingredient = True
                    
            if(matched_ingredient == False):
                # If even one ingredient is missing from current inventory, then break from loop
                break

        if(matched_ingredient == True):
            drinklist[drink_name] = drink_db['drinks'][drink_name]
            num_drinks += 1
        # else:
            # - Missing ingredients, not storing in drinklist.
    for pump_number in settings['quantity'].keys():
        moniterDB.ingridients(pump_number,settings['in_quantity'][pump_number],settings['quantity'][pump_number])
    
    if (drinklist != {}):
        errorcode = 0
    else:
        drinklist['empty'] = {
            "empty": {
                "name": "No Drink Options",
                "description": "Sorry, it looks like you don't have any drink options with current ingredients.",
                "image": "empty.jpg",
                "ingredients": {
                    "none": 0,
                }
            }
        }
        num_drinks = 1
        errorcode = 1
    moniterDB.update_total_drink(num_drinks)
    return render_template('index.html', show_navbar = True  , drinklist=drinklist, num_drinks=num_drinks, errorcode=errorcode)

@app.route('/work/<action>', methods=['POST','GET'])
@app.route('/work', methods=['POST','GET'])
def do_work(action=None):
    global pause_threads,stop_threads
    status = ReadStatus()
    drink_db = ReadDrinkDB()
    moniterDB = MoniterDB()

    if action == "pause":
        status = ReadStatus()
        if status['status']['active'] == 1:
            pause_threads = True
            status['control']['pause'] = 1  
            WriteStatus(status)
            print("Pouring paused.")
        return render_template('work.html', action=action, workmode='pause')

    if action == "resume":
        status = ReadStatus()
        if status['status']['active'] == 1 and pause_threads:
            pause_threads = False
            status['control']['pause'] = 0  
            WriteStatus(status)
            print("Pouring resumed.")
        return render_template('work.html', action=action, workmode='dispense')
    
    if action == 'cancel':
        stop_threads = True
        status['control']['pause'] = 0
        status['control']['stop'] = 1
        WriteStatus(status) 
        return render_template('work.html', action=action, workmode='cancel')
    
    if (request.method == 'POST') and (status['status']['active'] == 0):
        response = request.form
        if(response['makedrink'] in drink_db.get('drinks', {})):
            drink_name = response['makedrink']
            drink_info = drink_db['drinks'][drink_name]
            drinkDespenseImage = drink_info['image']['drinkDespenseImage']
            status['status']['active'] = 0
            status['status']['progress'] = 0
            status['control']['start'] = 1
            status['control']['pause'] = 0
            status['control']['stop'] = 0
            status['control']['clean'] = ""
            status['control']['drink_name'] = drink_name
            WriteStatus(status)
            
            return render_template('work.html', drink_name=drink_name, action="default", workmode='dispense',drinkDespenseImage=drinkDespenseImage)
    return redirect('/')

@app.route('/workstatus')
def workstatus(action=None):
    status = ReadStatus()
    percent_done = status['status']['progress']
    return jsonify({ 'percent_done' : percent_done})

def generate_system_info(length=25):
    key_file = 'system_key.txt'
    all_characters = (string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    if not os.path.exists(key_file):
        system_key = ''.join(random.choice(all_characters) for _ in range(length))
        with open(key_file, 'w') as file:
            file.write(system_key)
        time.sleep(0.5) 
    else:
        time.sleep(0.5)   
        with open(key_file, 'r') as file:
            system_key = file.read().strip()

    return {"system_key": system_key, "system_machine_name": __system_name__}

def get_wifi_networks():
    try:
        if platform.system() == 'Linux':
            result = subprocess.run(['sudo', 'iwlist', 'wlan0', 'scan'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            networks_output = result.stdout.decode('utf-8')

            # Extract SSIDs from the iwlist output
            ssid_list = re.findall(r'ESSID:"([^"]*)"', networks_output)
            
            # Get the currently connected SSID
            connected_ssid_result = subprocess.run(['iwgetid', '-r'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            connected_ssid_output = connected_ssid_result.stdout.decode('utf-8').strip()
            connected_ssid = connected_ssid_output if connected_ssid_output else None
            
            print(connected_ssid)
            return {"available_networks": ssid_list, "connected_ssid": connected_ssid}
        
        elif platform.system() == 'Windows':
            result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            networks_output = result.stdout.decode('utf-8')

            # Extract SSIDs from the network scan output
            ssid_list = re.findall(r'SSID \d+ : (.+)', networks_output)

            # Get the currently connected SSID using netsh wlan show interfaces
            connected_result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            connected_output = connected_result.stdout.decode('utf-8')

            # Extract the connected SSID from the interface output
            connected_ssid_match = re.search(r'SSID\s*:\s*(.+)', connected_output)
            connected_ssid = connected_ssid_match.group(1).strip() if connected_ssid_match else None
            return {"available_networks": ssid_list, "connected_ssid": connected_ssid}
        
    except Exception as e:
        return {"available_networks": [], "connected_ssid": None}

@app.route('/get-available-networks', methods=['GET'])
def get_available_networks():
    networks = get_wifi_networks()  
    available_networks = networks.get('available_networks', [],)
    return jsonify({'networks': available_networks,"message": f"We are trying fatching wifi network"}) 

def sanitize_ssid(ssid):
    print(ssid.strip())
    return ssid.strip()

def create_wifi_profile(ssid, password):
    """Create and configure a WiFi profile based on the platform."""
    ssid = sanitize_ssid(ssid)
    
    # try:
    if platform.system() == 'Windows':
            # Create an XML profile for Windows
            profile = f"""<?xml version="1.0"?>
            <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
                <name>{ssid}</name>
                <SSIDConfig>
                    <SSID>
                        <name>{ssid}</name>
                    </SSID>
                </SSIDConfig>
                <connectionType>ESS</connectionType>
                <connectionMode>auto</connectionMode>
                <MSM>
                    <security>
                        <authEncryption>
                            <authentication>WPA2PSK</authentication>
                            <encryption>AES</encryption>
                            <useOneX>false</useOneX>
                        </authEncryption>
                        <sharedKey>
                            <keyType>passPhrase</keyType>
                            <protected>false</protected>
                            <keyMaterial>{password}</keyMaterial>
                        </sharedKey>
                    </security>
                </MSM>
            </WLANProfile>
            """

            profile_filename = f'{ssid}.xml'
            try:
                with open(profile_filename, 'w') as file:
                    file.write(profile)

                # Add the Wi-Fi profile using netsh
                result = subprocess.run(['netsh', 'wlan', 'add', 'profile', f'filename={profile_filename}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode != 0:
                    error_message = result.stderr.decode('utf-8').strip()
                    return {"status": "500", "message": f"Failed to add profile for {ssid}: {error_message}"}
                
                return {"status": "200", "message": "Profile created successfully."}
            
            finally:
                # Remove the profile file after use
                if os.path.exists(profile_filename):
                    os.remove(profile_filename)
        
    elif platform.system() == 'Linux':
            config_entry = f"""
                network={{
                    ssid="{ssid}"
                    psk="{password}"
                    }}
            """
            print(config_entry)
            config_file = '/etc/wpa_supplicant/wpa_supplicant.conf'
            try:
                # Use 'sudo tee' to write to the file with superuser permissions
                process = subprocess.Popen(['sudo', 'tee', '-a', config_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate(input=config_entry.encode('utf-8'))
                print(process)
                    
                if process.returncode != 0:
                    return {"status": "500", "message": f"Failed to write to configuration file: {stderr.decode('utf-8').strip()}"}
                
                # Reconfigure wpa_supplicant
                result = subprocess.run(['sudo', 'wpa_cli', '-i', 'wlan0', 'reconfigure'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               
                if result.returncode != 0:
                    return {"status": "500", "message": f"Failed to configure WiFi for {ssid}: {result.stderr.decode('utf-8').strip()}"}
                return {"status": "200", "message": "Profile created successfully."}
            
            except subprocess.CalledProcessError as e:
                return {"status": "500", "message": f"Subprocess error: {str(e)}"}
            except PermissionError:
                return {"status": "403", "message": "Permission denied. You need to run this as a superuser."}
            except Exception as e:
                return {"status": "500", "message": f"An unexpected error occurred: {str(e)}"}
    else:
                return {"status": "501", "message": "WiFi profile creation not implemented for this platform."}

def connect_to_wifi(ssid):
    """Connect to a WiFi network based on the platform."""
    ssid = sanitize_ssid(ssid)
    
    try:
        if platform.system() == 'Windows':
            # Attempt to connect to the Wi-Fi network
            command = ['netsh', 'wlan', 'connect', f'name={ssid}']
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.returncode != 0:
                return {"status": "500", "message": f"Failed to connect to {ssid}."}
            
            # Wait for the connection to establish
            time.sleep(6)
            
            # Check the connection status
            status_command = ['netsh', 'wlan', 'show', 'interfaces']
            status_result = subprocess.run(status_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if status_result.returncode == 0:
                output = status_result.stdout.decode('utf-8')
                if "connected" in output:
                    return {'status': "200", "message": f"Successfully connected to {ssid}"}
                else:
                    return {"status": "500", "message": f"Failed to connect to {ssid}."}
            else:
                return {"status": "500", "message": "Failed to verify connection."}
        
        elif platform.system() == 'Linux':
            # Linux assumes the WiFi profile was created; connect via `wpa_cli`
            result = subprocess.run(['sudo', 'iwconfig', 'wlan0', 'essid', ssid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   
            time.sleep(6)

            if (result.returncode == 0):
               return {"status": "200", "message": f"Successfully connected to {ssid}"}
            else:
               return {"status": "500", "message": f"Failed to connect to {ssid}."}
            
        
        else:
            return {"status": "501", "message": "Connection not implemented for this platform."}
    
    except Exception as e:
        return {"status": "500", "message": f"An unexpected error occurred: {str(e)}"}
    
@app.route('/connect-via-wifi', methods=['GET', 'POST'])
@app.route('/admin', methods=['GET', 'POST'])
def connect_wifi():
    if request.method == 'POST':
        ssid = request.form['ssid'] 
        password = request.form['password']
        profile_status = create_wifi_profile(ssid, password)
        if profile_status['status'] != "200":
            return jsonify({'response': profile_status})

        connection_status = connect_to_wifi(ssid)
        print(connection_status)
        return jsonify({'response': connection_status})

    networks = get_wifi_networks()
    system_generate_info = generate_system_info()
    return render_template('connect_wifi.html', networks=networks,show_navbar = True,system_access_key = system_generate_info['system_key'],system_name = system_generate_info['system_machine_name'])
    
@app.route('/disconnect-wifi', methods=['POST'])
def disconnect_wifi():
    """Disconnect from the current WiFi network and prevent automatic reconnection."""
    try:
        if platform.system() == 'Windows':
            # Attempt to disconnect using Windows command
            result = subprocess.run(['netsh', 'wlan', 'disconnect'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                scan_result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return jsonify({"status": "200", "message": "Disconnected successfully.", "available_networks": scan_result.stdout.decode('utf-8')})
            else:
                error_message = result.stderr.decode('utf-8').strip()
                return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})

        elif platform.system() == 'Linux':
            # Disconnect using Linux command
            disconnect_result = subprocess.run(['sudo', 'ip', 'link', 'set', 'wlan0', 'down'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if disconnect_result.returncode == 0:
                config_file = '/etc/wpa_supplicant/wpa_supplicant.conf'
                
                networks = get_wifi_networks()
                ssid_to_remove = networks['connected_ssid']
                remove_network_config(ssid_to_remove, config_file)

                # Re-enable wlan0 if needed
                subprocess.run(['sudo', 'ip', 'link', 'set', 'wlan0', 'up'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                return jsonify({"status": "200", "message": "Disconnected and auto-reconnection prevented."})
            else:
                error_message = disconnect_result.stderr.decode('utf-8').strip()
                return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})

    except Exception as e:
        return jsonify({"status": "500", "message": f"An unexpected error occurred: {str(e)}"})

def remove_network_config(ssid, config_file):
    print('{ssid} want to remove profile')
    try:
        with open(config_file, 'r') as file:
            lines = file.readlines()

        # Prepare the updated content, excluding the SSID block
        updated_lines = []
        skip = False
        for line in lines:
            if f'ssid="{ssid}"' in line:
                skip = True
            elif '}' in line and skip:
                skip = False
                continue  # Skip the closing brace
            if not skip:
                updated_lines.append(line)

        # Join updated lines into a string
        updated_config = ''.join(updated_lines)

        # Use subprocess with 'sudo' to write the updated content to the config file
        process = subprocess.Popen(['sudo', 'tee', config_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=updated_config.encode('utf-8'))

        if process.returncode != 0:
            print(f"Failed to modify {config_file}: {stderr.decode('utf-8')}")
        else:
            print(f"{ssid} network configuration removed successfully.")

    except Exception as e:
        print(f"Failed to modify {config_file}: {str(e)}")
    
def clean_pumps(pump_group, status):
    for pump_number in pump_group:
        status['status']['active'] = 0
        status['status']['progress'] = 0
        status['control']['start'] = 0
        status['control']['pause'] = 0
        status['control']['stop'] = 0
        status['control']['clean'] = pump_number
        status['control']['drink_name'] = 'empty'
        WriteStatus(status)

@app.route('/inventory/<action>', methods=['POST', 'GET'])
@app.route('/inventory/pump/<action>', methods=['POST', 'GET'])
@app.route('/inventory', methods=['POST', 'GET'])
def inventory(action=None):
    settings = ReadSettings()   
    drink_db = ReadDrinkDB()
    status = ReadStatus()
    moniterDB = MoniterDB()
    available_GPIOs = [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    errorcode = 0
    errormessage = []

    if request.method == 'POST' and action == 'settings':
        response = request.form
        for pump_number, pin_number in settings['assignments'].items():
            index = 'inv_' + pump_number
            if index in response:
                settings['inventory'][pump_number] = response[index]

        for pump_number, inv_name in settings['inventory'].items():
            index = 'ass_' + pump_number
            if index in response:
                settings['assignments'][pump_number] = int(response[index])

        for pump_number in settings['quantity'].keys():
            quantity_index = 'qty_' + pump_number 
            if quantity_index in response:             
                settings['quantity'][pump_number] = int(response[quantity_index])
                settings['in_quantity'][pump_number] = int(response[quantity_index])
                moniterDB.ingridients(pump_number,int(response[quantity_index]),int(response[quantity_index]))

        duplicated_pin = []
        for pump_number, pin_number in settings['assignments'].items():
            for pump_number_inside, pin_number_inside in settings['assignments'].items():
                if (pin_number != 0) and (pin_number == pin_number_inside) and (pump_number != pump_number_inside):
                    errorcode = 1
                    if pin_number not in duplicated_pin:
                        duplicated_pin.append(pin_number)
                        errormessage.append('Pin ' + str(pin_number) + ' is assigned to more than one pump. ')

        used_drinks = {}
        for pump_number, drink_name in settings['inventory'].items():
            if drink_name == "Default":
                continue
            elif drink_name in used_drinks:
                errorcode = 1
                errormessage.append(f'Drink "{drink_name}" is already assigned to pump {used_drinks[drink_name]} and cannot be assigned to pump {pump_number}.')
            else:
                used_drinks[drink_name] = pump_number  

        if 'flow_rate' in response:
            settings['flowrate'] = int(response['flow_rate'])

        if errorcode > 0:
            settings = ReadSettings()
            errormessage.append('Settings NOT saved. Please check your settings and try again. ')
        else:
            WriteSettings(settings)

    if request.method == 'POST' and action == 'refill':
        response = request.get_json()
        pump_number_clean = response.get('pump_number')
        action = response.get('action')
        drink_name = 'clean'
        
        if (action == "cancel"):
                    status['control']['stop'] = 1 
                    WriteStatus(status)
                    return jsonify({'status': 'success', 'message': 'Pump re-fill deactivated'})

        if (status['status']['active']==1):
            print(status['status']['active']==1)
            return jsonify({'status': 'error', 'message': 'Another refill process is in progress. Please wait.'})

        # Verify pump number and activate refill
        for pump_numbers, pin_number in settings['assignments'].items():
            if pump_numbers == pump_number_clean:
                status['status']['active'] = 0
                status['status']['progress'] = 0
                status['control']['start'] = 0
                status['control']['pause'] = 0
                status['control']['stop'] = 0
                status['control']['clean'] = pump_number_clean
                status['control']['drink_name'] = 'empty'
                WriteStatus(status)
                return jsonify({'status': 'success', 'message': f'{pump_number_clean} is re-fill activated. Please wait a minute.'})

        return jsonify({'status': 'error', 'message': 'Pump not found'})

    return render_template('inventory.html', show_navbar=False,  action=action,errorcode=errorcode, errormessage=errormessage, settings=settings, drink_db=drink_db, available_GPIOs=available_GPIOs)

@app.route('/quantity-status', methods=['POST', 'GET'])
def quantityStatus():
    settings = ReadSettings()   
    errormessage = []
    
    for pump_number, quantity in settings['quantity'].items():
        if pump_number == 'pump_16':
            continue
        percentage = (settings['in_quantity'].get(pump_number, 0)/1000) * 100
        inQuantity = settings['in_quantity'].get(pump_number, 0)

        if inQuantity <= 200:
            errormessage.append({
                'pump_number': pump_number,
                'available_quantity': inQuantity,
                'status': 'Alert: Below 200 Threshold'
            })
        
        elif inQuantity <= 100:
            errormessage.append({
                'pump_number': pump_number,
                'available_quantity': inQuantity,
                'status': 'Alert: Below 100 Threshold'
            })
            print(errormessage)
       
    return jsonify({
        'status': 'error',
        'errormessage': errormessage
    })

@app.route('/cleaning/pump/<action>', methods=['POST', 'GET'])
@app.route('/cleaning',methods = ['POST','GET'])
def cleaning(action=None):
    settings = ReadSettings()   
    drink_db = ReadDrinkDB()
    status = ReadStatus()
    available_GPIOs = [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    errorcode = 0
    errormessage = []    
    
    if request.method == 'POST' and action == 'clean':
        response = request.form
        clean_group = response.get('clean_group')  # Accessing the form data safely
        print(f"Clean group selected: {clean_group} ")  
        drink_name = 'clean'
        
        # Define pump two groups dynamically from settings.json
        non_alcoholic_pumps = [pump for pump in settings['inventory'].keys() if pump in ['pump_01', 'pump_02', 'pump_03', 'pump_04', 'pump_05', 'pump_06', 'pump_07']]
        alcoholic_pumps = [pump for pump in settings['inventory'].keys() if pump in ['pump_08', 'pump_09', 'pump_10', 'pump_11', 'pump_12', 'pump_13', 'pump_14', 'pump_15']]

        if clean_group == 'all':
            status['status']['active'] = 0
            status['status']['progress'] = 0
            status['control']['start'] = 0
            status['control']['pause'] = 0
            status['control']['stop'] = 0
            status['control']['clean'] = "all"
            status['control']['drink_name'] = 'empty'
            WriteStatus(status)
            return render_template('work.html', drink_name=drink_name, action="default", workmode='clean',clean_pump_group = 'all')

        elif clean_group == 'non_alcoholic':
            clean_pumps(non_alcoholic_pumps, status)
            return render_template('work.html', drink_name=drink_name, action="default", workmode='clean', clean_pump_group='non alcoholic')

        elif clean_group == 'alcoholic':
            clean_pumps(alcoholic_pumps, status)
            return render_template('work.html', drink_name=drink_name, action="default", workmode='clean', clean_pump_group='alcoholic')

        else:
            return "Error: Invalid selection", 400  
    return render_template('cleaning.html',show_navbar = True, action=action, errorcode=errorcode, errormessage=errormessage, settings=settings, drink_db=drink_db,available_GPIOs=available_GPIOs)

@app.route('/ir-sensor-detection',methods=["POST","GET"])
def irSensorDetection():
    try:
        settings = ReadSettings()
        errorcode = 0
        errormessage = []
        
        sensor = SensorSignal(settings) 
        
        sensor_result = sensor.detectObject(settings)
        
        return jsonify({"sensor_results":sensor_result,"detection":settings["ir_sensor"]["detection"]})
    
    except Exception as e:
        errorcode = 500
        errormessage.append(str(e))
        return jsonify({"errorcode":errorcode, "errormessage":errormessage})
        
        
@app.route('/manifest')
def manifest():
    res = make_response(render_template('manifest.json'), 200)
    res.headers["Content-Type"] = "text/cache-manifest"
    return res

# def watch_consumption_file(interval = 2):
#         global last_modification_file
#         while True:
#             try:
#                 current_mtime = os.path.getmtime(CONSUMPTION_FILE)
#                 if current_mtime != last_modification_file:
#                     last_modification_file = current_mtime
#                     print("[INFO] Detected JSON change, emitting data...")
#                     data = MoniterDB()
#                     sio.emit('consumption_update', data.read())
#             except FileNotFoundError:
#                 print("[WARN] consumption file not found")
#             except Exception as e:
#                 print(f"[ERROR] Watching file: {e}")
#             time.sleep(interval)    
            

# @sio.event
# def connect():
#     print(f"[{DEVICE_ID}] Connected to dashboard at {SERVER_URL}")
   
#     print(moniterData.read())
#     sio.emit('register', {
#         'machine_id': __system_id__,
#         'machine_name': __system_name__,
#         'server_url': SERVER_URL,
#         'port': CLIENT_PORT,
#         'drink_consumed':moniterData.read() 
#     })
    
# @sio.event
# def disconnect():
#     print(f"[{DEVICE_ID}] Disconnected from server")

# @sio.event
# def reconnect():
#     print(f"[{DEVICE_ID}] Reconnected to server")

# def start_socket_client():
#     """Improved connection handler with multiple fallback options"""
#     transports = ['websocket']
#     if POLLING_FALLBACK:
#         transports.append('polling')

#     while True:
#         try:

#             print(f"[{DEVICE_ID}] Connecting to {SERVER_URL} (transports: {', '.join(transports)})")
#             sio.connect(
#                 SERVER_URL,
#                 transports=transports,
#                 headers={'X-Device-ID': DEVICE_ID},
#                 namespaces=['/'],
#                 wait_timeout=10
#             )
#             sio.wait()

#         except (socketio.exceptions.ConnectionError, Exception) as e:
#             print(f"[{DEVICE_ID}] Connection failed: {str(e)}")
#             print(f"Retrying in 5 seconds...")
#             time.sleep(5)

# @sio.on('sendNotification')
# def send_consumption(drinks):
#     sio.emit('sendNotification', drinks)

# if __name__ == '__main__':
#     threading.Thread(target=socket_client, daemon=True).start()
#     app.run(host='0.0.0.0') # Use this for Production Mode
#  or os.environ.get("WERKZEUG_RUN_MAIN") == "true"

if __name__ == '__main__':
    # threading.Thread(
    #     target=start_socket_client,
    #     daemon=True,
    #     name=f"{DEVICE_ID}-connector"
    # ).start()
    # threading.Thread(
    #     target=watch_consumption_file,
    #     daemon=True,
    #     name=f"JSON-watcher"
    # ).start()
   
    app.run(host='0.0.0.0',  port=5000,
        threaded=True,
        use_reloader=False) 