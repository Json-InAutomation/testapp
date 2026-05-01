from flask import Flask, flash, url_for, request, render_template, make_response, jsonify, redirect
from flask_cors import CORS
import subprocess
import time
import os
import json
import datetime
from common import *
from werkzeug.utils import secure_filename
import re
import platform
import random,string
if platform.system() == "Windows":
    from platform_prototype import SensorSignal  
else:
    from platform_raspi import SensorSignal  
from version import __system_name__,__system_id__
from flask_socketio import SocketIO
import threading
import shutil

UPLOAD_DIR = 'static/img/drinks'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','json',"mp4"}
BACKUP_DIR = 'archived'
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')

pause_threads = False
stop_threads = False

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR
socketio = SocketIO(app)
CORS(app)
ledStripControl = LEDStripControl('OneStripNeopixel.py')

moniterData = MoniterDB()
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST','GET'])
def index():
    print(platform.system())
    global pause_threads,stop_threads
    settings = ReadSettings()
    drink_db = ReadDrinkDB()
    moniterDB = MoniterDB()
    moniterDB.write()
    status = ReadStatus()
    drink_list = []
    
    # Collect all possible drinks
    for d_name, d_details in drink_db['drinks'].items():
        matched = True
        for ing_name in d_details['ingredients']:
            if ing_name not in settings['inventory'].values():
                matched = False
                break
        if matched:
            drink_list.append(d_name)
            
    if not drink_list:
        return render_template('index.html', show_navbar=True, drink_name='', action='default', workmode='dispense', infinite_mode=0)

    print(drink_list)
    drink_name = drink_list[0]
    print(drink_name)
    status['status']['active'] = 0
    status['status']['progress'] = 0
    status['status']['waiting'] = 1
    status['status']['wait_time'] = 30
    status['status']['active_pumps'] = []
    status['control']['start'] = 0
    status['control']['pause'] = 0
    status['control']['stop'] = 0
    status['control']['clean'] = ''
    status['control']['drink_name'] =   drink_name
    status['control']['infinite_mode'] = 1
    status['control']['infinite_drinks'] = drink_list
    status['control']['infinite_index'] = 0
    WriteStatus(status)
    return render_template('index.html', show_navbar=True, drink_name=drink_name, action='default', workmode='dispense', infinite_mode=1)


@app.route('/workstatus')
def workstatus(action=None):
    status = ReadStatus()
    drink_db = ReadDrinkDB()
    percent_done = status['status']['progress']
    active_pumps = status['status'].get('active_pumps', [])
    waiting = status['status'].get('waiting', 0)
    wait_time = status['status'].get('wait_time', 0)
    drink_name = status['control'].get('drink_name', '')
    
        
    return jsonify({
        'percent_done' : percent_done,
        'active_pumps': active_pumps,
        'waiting': waiting,
        'wait_time': wait_time,
        'drink_name': drink_name
    })

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
@app.route('/inventory/settings/<action>', methods=['POST', 'GET'])
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
        print(response)
        for pump_number, pin_number in settings['assignments'].items():
            index = 'inv_' + pump_number
            if index in response:
                settings['inventory'][pump_number] = response[index]

        for pump_number, inv_name in settings['inventory'].items():
            index = 'ass_' + pump_number
            if index in response:
                settings['assignments'][pump_number] = int(response[index])

        # for pump_number in settings['quantity'].keys():
        #     quantity_index = 'qty_' + pump_number 
        #     if quantity_index in response:      
        #         # settings['quantity'][pump_number] = int(response[quantity_index])
        #         # settings['in_quantity'][pump_number] = int(response[quantity_index])
        #         moniterDB.ingridients(pump_number,int(response[quantity_index]),int(response[quantity_index]))

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
        
        metadata = ReadMetadata()

        non_alcoholic_pumps = {
            'pump_01', 'pump_02', 'pump_03',
            'pump_04', 'pump_05', 'pump_06', 'pump_07'
        }

        if pump_number_clean in non_alcoholic_pumps:
            metadata['machine']['non_alcoholic_last_refilled'][pump_number_clean] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            WriteMetadata(metadata)
        
        if (action == "cancel"):
            status['control']['stop'] = 1 
            WriteStatus(status)
            return jsonify({'status': 'success', 'message': 'Pump re-fill deactivated'})

        if (status['status']['active']==1):
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
    
    if request.method == 'POST' and action == 'quantity':
        response = request.get_json()
        for pump_number in settings['quantity'].keys():
            if response.get('pump_number') == pump_number:      
                settings['quantity'][pump_number] = int(response.get("quantity"))
                settings['in_quantity'][pump_number] = int(response.get("quantity"))
                moniterDB.ingridients(pump_number,int(response.get("quantity")),int(response.get("quantity")))
        WriteSettings(settings)
        return jsonify({'status': 'success', 'message': f'The quantity is updated successfully.'})
    return render_template('inventory.html', show_navbar=False,  action=action,errorcode=errorcode, errormessage=errormessage, settings=settings, drink_db=drink_db, available_GPIOs=available_GPIOs)

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
        clean_group = response.get('clean_group') 
        drink_name = 'clean'
        metadata = ReadMetadata() 
        metadata['machine']['last_cleaned_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        WriteMetadata(metadata)
      
        
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
        print(f"Sensor Result: {settings['ir_sensor']['isDetected']}")
        
        return jsonify({"sensor_results":settings['ir_sensor']['isDetected'],"detection":settings['ir_sensor']['detection']})
    
    except Exception as e:
        errorcode = 500
        errormessage.append(str(e))
        return jsonify({"errorcode":errorcode, "errormessage":errormessage})
        
@app.route('/deployment/upload',methods=["POST","GET"])
def upload():
    if request.method == "POST":

        if 'file' not in request.files:
                return jsonify({'status':'error','message':f"file does not contains"})
        
        files = request.files.getlist('file')
        print(files)
        uploaded = []
        failed = []
        new_backup_dir = os.path.join(BACKUP_DIR, f'asset_{timestamp}', 'drinks')
        archived_dir = os.path.join(BACKUP_DIR,  f'asset_{timestamp}')

        if not os.path.exists(os.path.join(os.getcwd(), BACKUP_DIR)):
            os.makedirs(BACKUP_DIR, exist_ok=True)

        shutil.copytree(UPLOAD_DIR, new_backup_dir,dirs_exist_ok=True)
        print(f"Backup created at: {new_backup_dir}")

        for file in files:
            #Get File Size
            file.seek(0, os.SEEK_END)
            size = file.tell()
            file.seek(0)

            if file.filename.strip() == "":
                failed.append({
                     "file": "unknown",
                    "reason": "Empty filename",
                    'status':'failed'
                })
                continue

            if not allowed_file(file.filename):
                failed.append({
                     "file": file.filename,
                    "reason": "Invalid file type",
                    'status':'failed'
                })
                continue

            filename = secure_filename(file.filename)
            print(filename)
            if filename == 'settings.json':
                shutil.copy(
    os.path.join(os.getcwd(), filename),
    os.path.join(archived_dir, f'settings_{timestamp}.json')
)
            elif filename == 'drink_db.json':
                shutil.copy(
                  os.path.join(os.getcwd(), filename),
                    os.path.join(archived_dir, f'drink_db_{timestamp}.json')
                )

            try:
                filename = secure_filename(file.filename)
                if filename == 'settings.json' or filename == 'drink_db.json':
                    file.save(os.path.join(os.getcwd(),filename))
                else:
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                    uploaded.append({
                        'file':file.filename,
                        'size':round(size / 1024, 2),
                        'status':'uploaded'
                    })

            except Exception as e:
                failed.append({
                    "file": file.filename,
                    "reason": str(e)
            })
                
        status = 'uploaded' if not failed else('partially uploaded' if uploaded else "failed")
                    
        return jsonify({
        "status": status,
        "uploaded": uploaded,
        "failed": failed
    })
    return jsonify({"stutus":"error","message":"Invalid input"})

@app.route('/manifest')
def manifest():
    res = make_response(render_template('manifest.json'), 200)
    res.headers["Content-Type"] = "text/cache-manifest"
    return res

if os.environ.get("RUN_BACKGROUND") == "true":
    if os.environ.get("WERKZEUG_RUN_MAIN") != "false":  
        print("Starting LED strip from systemd...")
        ledStripControl.startStrip()