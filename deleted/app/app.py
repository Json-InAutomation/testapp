
# def system_machine_info(key_length=25, name_length=10):
#     """
#     Generates and stores a system access key and a system name in separate files.
    
#     Args:
#     key_length (int): The length of the system access key to be generated. Default is 25.
#     name_length (int): The length of the system name to be generated. Default is 10.

#     Returns:
#     tuple: A tuple containing the system access key and system name.
#     """
#     if name_length != 10:
#         raise ValueError("System name length must be exactly 10 characters with specified format.")

#     key_file = 'system_key.txt'
#     name_file = 'system_name.txt'

#     # Generate system access key
#     if os.path.exists(key_file):
#         if (os.path.exists(name_file)):
#             try:
#                 with open(name_file, 'r') as files:
#                     system_name = files.read().strip()
#                     print("Using existing system key:", system_name)
#             except IOError as e:
#                     print(f"Error reading the key file: {e}")
#                     system_name = None
#         try:
#             with open(key_file, 'r') as file:
#                 system_key = file.read().strip()
#             print("Using existing system key:", system_key)
#         except IOError as e:
#             print(f"Error reading the key file: {e}")
#             system_key = None
#     else:
#         system_access_key = string.ascii_uppercase + string.digits
#         system_key = ''.join(random.choice(system_access_key) for _ in range(key_length))
#         try:
#             with open(key_file, 'w') as file:
#                 file.write(system_key)
#         except IOError as e:
#             print(f"Error writing to the key file: {e}")
#             system_key = None

#         # Generate system name
#         first_char = random.choice(string.ascii_uppercase)
#         middle_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
#         last_chars = ''.join(random.choice(string.digits) for _ in range(3))
#         system_name = first_char + middle_chars + last_chars

#         try:
#             with open(name_file, 'w') as file:
#                 file.write(system_name)
#         except IOError as e:
#             print(f"Error writing to the name file: {e}")
#             system_name = None

#     return system_key, system_name
# UPLOAD_FOLDER = 'static/img/drinks'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def fixup_string(broken):
#     fixed = ''.join(e for e in broken if e.isalnum())
#     fixed = fixed.lower()
#     return(fixed)

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/uploadfile', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             return redirect('/recipe')
#         else:
#             file = request.files['file']
#             # If the user does not select a file, the browser submits an
#             # empty file without a filename.
#             if file.filename == '':
#                 #flash('No selected file')
#                 return redirect('/recipe')
#             if file and allowed_file(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#                 return redirect('/recipe')
#     return redirect('/recipe')


# def fixup_string(broken):
#     fixed = ''.join(e for e in broken if e.isalnum())
#     fixed = fixed.lower()
#     return(fixed)

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# @app.route('/uploadfile', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             return redirect('/recipe')
#         else:
#             file = request.files['file']
#             # If the user does not select a file, the browser submits an
#             # empty file without a filename.
#             if file.filename == '':
#                 #flash('No selected file')
#                 return redirect('/recipe')
#             if file and allowed_file(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#                 return redirect('/recipe')
#     return redirect('/recipe')


# @app.route('/uploadfile', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             return redirect('/recipe')
#         else:
#             file = request.files['file']
#             if file.filename == '':
#                 return redirect('/recipe')
#             if file and allowed_file(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#                 return redirect('/recipe')
#     return redirect('/recipe')
# @app.route('/recipe/<action>', methods=['POST'])
# @app.route('/recipe', methods=['POST','GET'])
# def recipe(action=None):
# 	drink_db = ReadDrinkDB()

# 	UPLOAD_DIR = 'static/img/drinks'

# 	if (request.method == 'POST'):
# 		response = request.form
# 		#print(response)
# 		# Drink Recipe Edit Functions
# 		if('drink_edit' in response):
# 			if (response['drink_edit'] == 'true'):
# 				#print('drink_edit')
# 				# Get Selected Drink Recipe
# 				drink_id = response['drink_id']
# 				#print(drink_id)
# 				# Build Image List
# 				img_list = []
# 				for root, dirs, files in os.walk(UPLOAD_DIR):
# 					for file in files:
# 						if file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".jpeg") or file.endswith(".JPEG") or file.endswith(".png"):
# 							filename = (os.path.join(root, file)).replace('static/','')
							
# 							#print(filename)
# 							img_list.append(filename)
# 				#print(img_list)
# 				num_imgs = len(img_list)
# 				return render_template('recipe_drink_edit.html', drink_db=drink_db, drink_id=drink_id, img_list=img_list, num_imgs=num_imgs)
# 		elif('drink_add' in response):
# 			if (response['drink_add'] == 'true'):
# 				#print('drink_add')
# 				drink_id = 'enter_new_drink_id'
# 				if (drink_id in drink_db['drinks']):
# 					# If there was another record with the same name, delete it
# 					drink_db['drinks'].pop(drink_id)
# 				drink_db['drinks'][drink_id] = {}
# 				drink_db['drinks'][drink_id]['name'] = 'DEFAULT Drink Name'  
# 				drink_db['drinks'][drink_id]['description'] = 'Enter Description.'
# 				drink_db['drinks'][drink_id]['image'] = 'img/drinks/default.jpg'
# 				drink_db['drinks'][drink_id]['ingredients'] = {}
# 				WriteDrinkDB(drink_db)
# 				# Build Image List
# 				img_list = []
# 				for root, dirs, files in os.walk(UPLOAD_DIR):
# 					for file in files:
# 						if file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".jpeg") or file.endswith(".JPEG") or file.endswith(".png"):
# 							filename = (os.path.join(root, file)).replace('static/','')
							
# 							#print(filename)
# 							img_list.append(filename)
# 				#print(img_list)
# 				num_imgs = len(img_list)
# 				return render_template('recipe_drink_edit.html', drink_db=drink_db, drink_id=drink_id, img_list=img_list, num_imgs=num_imgs)
# 		elif('drink_del' in response):
# 			if (response['drink_del'] == 'true'):
# 				#print('drink_del')
# 				drink_id = response['drink_id']
# 				#print(drink_id)
# 				drink_db['drinks'].pop(drink_id)
# 				WriteDrinkDB(drink_db)
# 				return ('{ "result" : "success" }')
# 		elif('drink_edid' in response):
# 			if (response['drink_edid'] == 'true'):
# 				#print('drink_edid')
# 				drink_id = response['drink_id']
# 				new_drink_id = response['new_drink_id']
# 				#print(drink_id)
# 				if(new_drink_id.isalnum() != True): 
# 					new_drink_id = fixup_string(new_drink_id)
# 				drink_db['drinks'][new_drink_id] = drink_db['drinks'].pop(drink_id)
# 				WriteDrinkDB(drink_db)
# 				return render_template('recipe_drink_edit.html', drink_db=drink_db, drink_id=new_drink_id)
# 		elif('drink_dn' in response):
# 			if (response['drink_dn'] == 'true'):
# 				#print('drink_dn')
# 				drink_id = response['drink_id']
# 				new_drink_dn = response['new_drink_dn']
# 				#print(drink_id)
# 				drink_db['drinks'][drink_id]['name'] = new_drink_dn
# 				WriteDrinkDB(drink_db)
# 				return ('{ "result" : "success" }')
# 		elif('drink_desc' in response):
# 			if (response['drink_desc'] == 'true'):
# 				#print('drink_desc')
# 				drink_id = response['drink_id']
# 				new_drink_desc = response['new_drink_desc']
# 				#print(drink_id)
# 				drink_db['drinks'][drink_id]['description'] = new_drink_desc
# 				WriteDrinkDB(drink_db)
# 				return ('{ "result" : "success" }')
# 		elif('drink_ing_edit' in response):
# 			if (response['drink_ing_edit'] == 'true'):
# 				#print('drink_ing_edit')
# 				drink_id = response['drink_id']
# 				ing_id = response['ing_id']
# 				return render_template('recipe_drink_ing_edit.html', ingdisplayname=drink_db['ingredients'][ing_id], pumptime=drink_db['drinks'][drink_id]['ingredients'][ing_id], ing_id=ing_id, drink_id=drink_id)
# 		elif('drink_ing_del' in response):
# 			if (response['drink_ing_del'] == 'true'):
# 				#print('drink_ing_del')
# 				drink_id = response['drink_id']
# 				ing_id = response['ing_id']
# 				drink_db['drinks'][drink_id]['ingredients'].pop(ing_id)
# 				WriteDrinkDB(drink_db)
# 				return ('{ "result" : "success" }')
# 		elif('drink_ing_save' in response):
# 			if (response['drink_ing_save'] == 'true'):
# 				#print('drink_ing_save')
# 				drink_id = response['drink_id']
# 				ing_id = response['ing_id']
# 				new_pumptime = response['new_pumptime']
# 				drink_db['drinks'][drink_id]['ingredients'][ing_id] = int(new_pumptime)
# 				WriteDrinkDB(drink_db)
# 				return render_template('recipe_drink_ing_saved.html', ing_dn=drink_db['ingredients'][ing_id], pumptime=new_pumptime, ing_id=ing_id, drink_id=drink_id)
# 		elif('drink_ing_add' in response):
# 			if (response['drink_ing_add'] == 'true'):
# 				#print('drink_ing_add')
# 				drink_id = response['drink_id']
# 				new_ing_id = response['new_ing_id']
# 				new_pumptime = response['new_pumptime']
# 				if (new_ing_id in drink_db['ingredients']):
# 					drink_db['drinks'][drink_id]['ingredients'][new_ing_id] = int(new_pumptime)
# 					WriteDrinkDB(drink_db)
# 				return render_template('recipe_drink_ing_saved.html', ing_dn=drink_db['ingredients'][new_ing_id], pumptime=new_pumptime, ing_id=new_ing_id, drink_id=drink_id)
# 		elif('drink_ing_add_init' in response):
# 			if (response['drink_ing_add_init'] == 'true'):
# 				drink_id = response['drink_id']
# 				return render_template('recipe_drink_ing_add.html', drink_id=drink_id, drink_db=drink_db)
# 		elif('drink_img_sel' in response):
# 			if (response['drink_img_sel'] == 'true'):
# 				drink_id = response['drink_id']
# 				imagefilename = response['image_id']
# 				drink_db['drinks'][drink_id]['image'] = imagefilename
# 				WriteDrinkDB(drink_db)

# 		# Ingredient Edit Functions
# 		elif('ing_edit' in response):
# 			if (response['ing_edit'] == 'true'):
# 				#print ('Edit Selected.')
# 				id = response['ing_id']
# 				return render_template('recipe_ing_edit.html', id=id, displayname=drink_db['ingredients'][id])
# 		elif('ing_del' in response):
# 			if (response['ing_del'] == 'true'):
# 				#print ('Delete Selected.')
# 				id = response['ing_id']
# 				if(id in drink_db['ingredients']):
# 					drink_db['ingredients'].pop(id)
# 					WriteDrinkDB(drink_db)
# 				return ('Deleting...')
# 		elif('ing_save' in response):
# 			if (response['ing_save'] == 'true'):
# 				#print ('Save Selected.')
# 				id = response['ing_id']
# 				new_id = response['ing_new_id']
# 				new_dn = response['ing_new_dn']
# 				if new_dn != drink_db['ingredients'][id]:
# 					drink_db['ingredients'][id] = new_dn
# 				if new_id != id: 
# 					if(new_id.isalnum() != True): 
# 						new_id = fixup_string(new_id)
# 					drink_db['ingredients'][new_id] = drink_db['ingredients'].pop(id)
# 				WriteDrinkDB(drink_db)
# 				return render_template('recipe_ing_save.html', old_id=id, id=new_id, displayname=new_dn)
# 		elif('ing_add' in response):
# 			if (response['ing_add'] == 'true'):
# 				#print ('Add Selected.')
# 				new_id = response['ing_new_id']
# 				new_dn = response['ing_new_dn']
# 				if(new_id.isalnum() != True): 
# 					new_id = fixup_string(new_id)
# 				drink_db['ingredients'][new_id] = new_dn
# 				WriteDrinkDB(drink_db)
# 				return render_template('recipe_ing_save.html', old_id='ing_row_add', id=new_id, displayname=new_dn)
# 	return render_template('recipe.html', drink_db=drink_db, selected_drink='none')

# def create_wifi_profile(ssid, password):
#     ssid = sanitize_ssid(ssid)
#     profile = f"""<?xml version="1.0"?>
#     <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
#         <name>{ssid}</name>
#         <SSIDConfig>
#             <SSID>
#                 <name>{ssid}</name>
#             </SSID>
#         </SSIDConfig>
#         <connectionType>ESS</connectionType>
#         <connectionMode>auto</connectionMode>
#         <MSM>
#             <security>
#                 <authEncryption>
#                     <authentication>WPA2PSK</authentication>
#                     <encryption>AES</encryption>
#                     <useOneX>false</useOneX>
#                 </authEncryption>
#                 <sharedKey>
#                     <keyType>passPhrase</keyType>
#                     <protected>false</protected>
#                     <keyMaterial>{password}</keyMaterial>
#                 </sharedKey>
#             </security>
#         </MSM>
#     </WLANProfile>
#     """

#     profile_filename = f'{ssid}.xml'
#     with open(profile_filename, 'w') as file:
#         file.write(profile)

#     result = subprocess.run(['netsh', 'wlan', 'add', 'profile', f'filename={profile_filename}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     os.remove(profile_filename)  # Clean up the profile file after adding
#     print("the results",result)
#     print("Response check",result.returncode)
#     print("Validate Response",result.returncode == 0)
#     if result.returncode != 0:
#         error_message = result.stderr.decode('utf-8')
#         return {"status": "500", "message": f"Failed to add profile for {ssid}. Error: {error_message}"}
#     else:   
#         return {"status": "200", "message": f"Profile {ssid} added successfully."}



#admin code 
# @app.route('/admin/<action>', methods=['POST','GET'])
# @app.route('/admin', methods=['POST','GET'])
# def admin(action=None):
#     settings = ReadSettings()
#     drink_db = ReadDrinkDB()
#     status = ReadStatus()
#     # List of available BCM.GPIO assignments where 0 is unassigned
#     available_GPIOs = [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#     errorcode = 0
#     errormessage = []

#     if (request.method == 'POST') and (action == 'settings'):
#         response = request.form
#         #DEBUGprint('Settings Change Requested.')
#         #DEBUGprint(response)
#         for pump_number, pin_number in settings['assignments'].items():
#             index = 'inv_' + pump_number
#             if(index in response):
#                 #DEBUGprint(response[index])
#                 settings['inventory'][pump_number] = response[index]

#         for pump_number, inv_name in settings['inventory'].items():
#             index = 'ass_' + pump_number
#             if(index in response):
#                 #DEBUGprint(response[index])
#                 settings['assignments'][pump_number] = int(response[index])

#         duplicated_pin = []
#         for pump_number, pin_number in settings['assignments'].items():
#             for pump_number_inside, pin_number_inside in settings['assignments'].items():
#                 if (pin_number != 0) and (pin_number == pin_number_inside) and (pump_number != pump_number_inside):
#                     errorcode = 1
#                     if (pin_number not in duplicated_pin):
#                         duplicated_pin.append(pin_number)
#                         errormessage.append('Pin ' + str(pin_number) + ' is assigned to more than one pump. ')

#         if ('flow_rate' in response):
#             print(response['flow_rate'])
#             settings['flowrate'] = int(response['flow_rate'])

#         if (errorcode > 0):
#             settings = ReadSettings()
#             errormessage.append('Settings NOT saved. Please check your settings and try again. ')
#         else:
#             WriteSettings(settings)

#     if (request.method == 'POST') and (action == 'clean'):
#         response = request.form
#         drink_name = 'clean'

#         #print('Clean Requested.')
#         #print(response['clean'])
#         if 'pump_42' in response['clean']:
#             #print('Clean ALL pumps for 20 seconds.')
#             status['status']['active'] = 0
#             status['status']['progress'] = 0
#             status['control']['start'] = 0
#             status['control']['pause'] = 0
#             status['control']['stop'] = 0
#             status['control']['clean'] = "all"
#             status['control']['drink_name'] = 'empty'
#             WriteStatus(status)
#             return render_template('work.html', drink_name=drink_name, action="default", workmode='clean')
#         else:
#             for pump_number, pin_number in settings['assignments'].items():
#                 if(pump_number in response['clean']):
#                     #print('Clean ' + pump_number + ' for 20 seconds.')
#                     status['status']['active'] = 0
#                     status['status']['progress'] = 0
#                     status['control']['start'] = 0
#                     status['control']['pause'] = 0
#                     status['control']['stop'] = 0
#                     status['control']['clean'] = pump_number
#                     status['control']['drink_name'] = 'empty'
#                     WriteStatus(status)
#             return render_template('work.html', drink_name=drink_name, action="default", workmode='clean',clean_pump_group = pump_number)

#     # if action == 'reboot':
#     #     event = "Admin: Reboot"
#     #     os.system("sleep 3 && sudo reboot &")
#     #     return render_template('shutdown.html', action=action)

#     # elif action == 'shutdown':
#     #     event = "Admin: Shutdown"
#     #     os.system("sleep 3 && sudo shutdown -h now &")
#     #     return render_template('shutdown.html', action=action)

#     # uptime = os.popen('uptime').readline()

#     # cpuinfo = os.popen('cat /proc/cpuinfo').readlines()

#     # ifconfig = os.popen('ifconfig').readlines()

#     # temp = checkcputemp()

#     return render_template('admin.html', action=action, errorcode=errorcode, errormessage=errormessage, uptime=uptime, cpuinfo=cpuinfo, temp=temp, ifconfig=ifconfig, settings=settings, drink_db=drink_db, available_GPIOs=available_GPIOs)

#corrected code

# @app.route('/admin/<action>', methods=['POST','GET'])
# @app.route('/admin', methods=['POST','GET'])
# def admin(action=None):
#     settings = ReadSettings()
#     drink_db = ReadDrinkDB()
#     status = ReadStatus()
#     # List of available BCM.GPIO assignments where 0 is unassigned
#     available_GPIOs = [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#     errorcode = 0
#     errormessage = []

#     if (request.method == 'POST') and (action == 'settings'):
#         response = request.form
#         #DEBUGprint('Settings Change Requested.')
#         #DEBUGprint(response)
#         for pump_number, pin_number in settings['assignments'].items():
#             index = 'inv_' + pump_number
#             if(index in response):
#                 #DEBUGprint(response[index])
#                 settings['inventory'][pump_number] = response[index]

#         for pump_number, inv_name in settings['inventory'].items():
#             index = 'ass_' + pump_number
#             if(index in response):
#                 #DEBUGprint(response[index])
#                 settings['assignments'][pump_number] = int(response[index])

#         duplicated_pin = []
#         for pump_number, pin_number in settings['assignments'].items():
#             for pump_number_inside, pin_number_inside in settings['assignments'].items():
#                 if (pin_number != 0) and (pin_number == pin_number_inside) and (pump_number != pump_number_inside):
#                     errorcode = 1
#                     if (pin_number not in duplicated_pin):
#                         duplicated_pin.append(pin_number)
#                         errormessage.append('Pin ' + str(pin_number) + ' is assigned to more than one pump. ')

#         if ('flow_rate' in response):
#             print(response['flow_rate'])
#             settings['flowrate'] = int(response['flow_rate'])

#         if (errorcode > 0):
#             settings = ReadSettings()
#             errormessage.append('Settings NOT saved. Please check your settings and try again. ')
#         else:
#             WriteSettings(settings)
    
   
#     if (request.method == 'POST') and (action == 'pump_clean'):
#         response = request.get_json()
#         pump_number = response.get('pump_number')
#         action = response.get('action')
#         drink_name = 'clean'
        
      
#         for pump_numbers, pin_number in settings['assignments'].items():
#             print(pump_numbers)
#             if(pump_numbers == pump_number):
#                 print(pump_numbers == pump_number)
#                 #print('Clean ' + pump_number + ' for 20 seconds.')
#                 status['status']['active'] = 0
#                 status['status']['progress'] = 0
#                 status['control']['start'] = 0
#                 status['control']['pause'] = 0
#                 status['control']['stop'] = 0
#                 status['control']['clean'] = pump_number
#                 status['control']['drink_name'] = 'empty'
#                 WriteStatus(status)
#         return render_template('work.html', drink_name=drink_name, action="default", workmode='clean',clean_pump_group = pump_number)
    
#     if (request.method == 'POST') and (action == 'clean'):
#         response = request.form
#         drink_name = 'clean'
     
#         #print('Clean Requested.')
#         #print(response['clean'])
#         if 'pump_42' in response['clean']:
#             #print('Clean ALL pumps for 20 seconds.')
#             status['status']['active'] = 0
#             status['status']['progress'] = 0
#             status['control']['start'] = 0
#             status['control']['pause'] = 0
#             status['control']['stop'] = 0
#             status['control']['clean'] = "all"
#             status['control']['drink_name'] = 'empty'
#             WriteStatus(status)
#             return render_template('work.html', drink_name=drink_name, action="default", workmode='clean')
#         else:
#             for pump_number, pin_number in settings['assignments'].items():
#                 if(pump_number in response['clean']):
#                     #print('Clean ' + pump_number + ' for 20 seconds.')
#                     status['status']['active'] = 0
#                     status['status']['progress'] = 0
#                     status['control']['start'] = 0
#                     status['control']['pause'] = 0
#                     status['control']['stop'] = 0
#                     status['control']['clean'] = pump_number
#                     status['control']['drink_name'] = 'empty'
#                     WriteStatus(status)    
#             return render_template('work.html', drink_name=drink_name, action="default", workmode='clean',clean_pump_group = pump_number)

#     return render_template('admin.html', action=action, errorcode=errorcode, errormessage=errormessage, settings=settings, drink_db=drink_db, available_GPIOs=available_GPIOs)

    # if request.method == 'POST' and action == 'clean':
    #     response = request.form
    #     drink_name = 'clean'
    #     print(response)
    #     print(response)
    #     if 'pump_42' in response['clean']:
    #         status['status']['active'] = 0
    #         status['status']['progress'] = 0
    #         status['control']['start'] = 0
    #         status['control']['pause'] = 0
    #         status['control']['stop'] = 0
    #         status['control']['clean'] = "all"
    #         status['control']['drink_name'] = 'empty'
    #         WriteStatus(status)
    #         return render_template('work.html', drink_name=drink_name, action="default", workmode='clean')
        
    #     else:
    #         for pump_number, pin_number in settings['assignments'].items():
    #             if pump_number in response['clean']:
    #                 status['status']['active'] = 0
    #                 status['status']['progress'] = 0
    #                 status['control']['start'] = 0
    #                 status['control']['pause'] = 0
    #                 status['control']['stop'] = 0
    #                 status['control']['clean'] = pump_number
    #                 status['control']['drink_name'] = 'empty'
    #                 WriteStatus(status)
    #         return render_template('work.html', drink_name=drink_name, action="default", workmode='clean', clean_pump_group=pump_number)
    # if request.method == 'POST' and action == 'clean':
    #     response = request.form
    #     clean_group = response['clean_group']
    #     print(clean_group)
    #     drink_name = 'clean'
    #     # Define pump groups dynamically from settings.json
    #     non_alcoholic_pumps = [pump for pump, drink in settings['inventory'].items() if pump in ['pump_01', 'pump_07']]
    #     alcoholic_pumps = [pump for pump, drink in settings['inventory'].items() if pump in ['pump_08', 'pump_15']]

    #     if ('all' in response['clean_group']):
    #         status['status']['active'] = 0
    #         status['status']['progress'] = 0
    #         status['control']['start'] = 0
    #         status['control']['pause'] = 0
    #         status['control']['stop'] = 0
    #         status['control']['clean'] = "all"
    #         status['control']['drink_name'] = 'empty'
    #         WriteStatus(status)
    #         return render_template('work.html', drink_name=drink_name, action="default", workmode='clean')

    #     elif ('non_alcoholic' in response['clean_group']):
    #         clean_pumps(non_alcoholic_pumps, status)
    #         return render_template('work.html', drink_name=drink_name, action="default", workmode='clean', clean_pump_group='non_alcoholic')

    #     elif ('alcoholic' in response['clean_group']):
    #         clean_pumps(alcoholic_pumps, status)
    #         return render_template('work.html', drink_name=drink_name, action="default", workmode='clean', clean_pump_group='alcoholic')
    
# @app.route('/', methods=['POST','GET'])
# def index():
#     settings = ReadSettings()
#     drink_db = ReadDrinkDB()

#     drinklist = {}
#     num_drinks = 0

#     # Cycle through each drink recipe
#     for drink_name, drink_details in drink_db['drinks'].items():
#         print(drink_name)
#         # Cycle through each ingredient in the drink recipe
#         for drink_ingredients in drink_details['ingredients'].items():
#             matched_ingredient = False

#             # Cycle through each ingredient in the inventory and check against the recipe
#             for ingredients_available in settings['inventory'].items():
#                 if (ingredients_available[1] == drink_ingredients[0]):
#                     matched_ingredient = True
                    
#             if(matched_ingredient == False):
#                 # If even one ingredient is missing from current inventory, then break from loop
#                 break

#         if(matched_ingredient == True):
#             drinklist[drink_name] = drink_db['drinks'][drink_name]
#             num_drinks += 1
#         # else:
#             # - Missing ingredients, not storing in drinklist.

#     if (drinklist != {}):
#         # Viable drink recipes were found and the list has been created.
#         errorcode = 0
#     else:
#         # No viable drink recipes were found and the list has been created as below.
#         drinklist['empty'] = {
#             "empty": {
#                 "name": "No Drink Options",
#                 "description": "Sorry, it looks like you don't have any drink options with current ingredients.",
#                 "image": "empty.jpg",
#                 "ingredients": {
#                     "none": 0,
#                 }
#             }
#         }
#         num_drinks = 1
#         errorcode = 1

#     return render_template('index.html', drinklist=drinklist, num_drinks=num_drinks, errorcode=errorcode)

# without mixture

# @app.route('/', methods=['POST', 'GET'])
# def index():
#     settings = ReadSettings()
#     drink_db = ReadDrinkDB()

#     drinklist = {}
#     num_drinks = 0
#     mixer_name = "Mixer"  # Define the name of the mixer to ignore

#     # Cycle through each drink recipe
#     for drink_name, drink_details in drink_db['drinks'].items():

#         # Cycle through each ingredient in the drink recipe
#         matched_ingredient = True
#         for drink_ingredient, _ in drink_details['ingredients'].items():
#             if drink_ingredient == mixer_name:
#                 continue  # Skip the mixer in the check

#             # Check if the ingredient is available in the inventory
#             if not any(ingredients_available[1] == drink_ingredient for ingredients_available in settings['inventory'].items()):
#                 matched_ingredient = False
#                 break

#         if matched_ingredient:
#             drinklist[drink_name] = drink_db['drinks'][drink_name]
#             num_drinks += 1

#     if drinklist:
#         # Viable drink recipes were found and the list has been created.
#         errorcode = 0
#     else:
#         # No viable drink recipes were found and the list has been created as below.
#         drinklist['empty'] = {
#             "empty": {
#                 "name": "No Drink Options",
#                 "description": "Sorry, it looks like you don't have any drink options with current ingredients.",
#                 "image": "empty.jpg",
#                 "ingredients": {
#                     "none": 0,
#                 }
#             }
#         }
#         num_drinks = 1
#         errorcode = 1

#     return render_template('index.html', drinklist=drinklist, num_drinks=num_drinks, errorcode=errorcode)


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
#         global stop_threads

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
#                     break  # Stop searching once the correct pump is found

#             # Calculate runtime for this ingredient
#             calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
#             pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
#             pumpThreads.append(pump_t)

#             # Update the quantity of this pump immediately after calculating runtime
#             used_quantity = int(pump_runtime * (settings['flowrate'] / 100))
            
#             if pump_number in settings['quantity']:
#                 original_quantity = settings['quantity'][pump_number]
#                 #updated_quantity = 70ml(original_quantity)-20ml(used_quantity)
#                 settings['quantity'][pump_number] = max(0, original_quantity - used_quantity)
#                 #availabe quantity (Updating)
                
#                 #here checking availabe quantity is greater than 0 or not
            
#                 if (settings['quantity'][pump_number] > 0):
#                     percentage = ((settings['quantity'][pump_number] / original_quantity) * 100)
#                 else:
#                     percentage = 0  # Handle edge case where current_quantity might be zero
                    
#                 print(f"Progress for pump {pump_number}: {percentage}%")
                
#                 settings['percentage'][pump_number] = percentage


#         # Start the pump threads
#         for thread in pumpThreads:
#             thread.start()

#         # Monitor and report progress to WebUI
#         for x in range(total_runtime):
#             current_count += 1
#             status = ReadStatus()
#             if status['control']['stop'] == 1:
#                 stop_threads = True
#                 time.sleep(2)
#                 stop_threads = False
#                 break
#             percent_progress = int((current_count / total_runtime) * 100)
#             status['status']['progress'] = percent_progress
#             WriteStatus(status)
#             time.sleep(1)

#         # Wait for threads to finish
#         for thread in pumpThreads:
#             thread.join()

#         print('Finished dispensing drink.')
#         # Write updated settings to file after updating quantities for all pumps
#         WriteSettings(settings)

#         # Add a 4-second delay before starting the mixer
#         time.sleep(4)
#         print('Starting mixer...')
#         platform.start_mixer()

#         print('Finished. Cleaning up status file.')
#         status['status']['active'] = 0
#         status['control']['start'] = 0
#         status['control']['stop'] = 0
#         WriteStatus(status)

#     else:
#         print('Error, no drinks match that name.')

##################
# pourDrink

# def PourDrink(drink_name):
#     drink_db = ReadDrinkDB()
#     if (drink_name in drink_db['drinks']):
#         # Set Active Status
#         status = ReadStatus()
#         status['status']['active'] = 1
#         WriteStatus(status)

#         total_runtime = 0
#         percent_progress = 0
#         current_count = 0
#         global stop_threads

#         # Initialize Platform Object
#         settings = ReadSettings()
#         platform = PumpControl(settings)

#         print(f'Starting to prepare {drink_name}')
#         # Cycle through each ingredient in the drink recipe to get the highest runtime, to get the total runtime
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             #total_runtime = total_runtime + int(pump_runtime * (settings['flowrate'] / 100))
#             total_runtime = max(total_runtime, int(pump_runtime * (settings['flowrate'] / 100)))

#         print(f'Total Runtime: {total_runtime}')

#         # Cycle through each ingredient and create threads to dispense the beverage
#         pumpThreads = []
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             pump_number = 'none'
#             for index, value in settings['inventory'].items():
#                 if(value == drink_ingredient):
#                     pump_number = index
#                     # print(f'Pump number = {index}')
                    
                    

#             # Init thread
#             calculated_pump_runtime = max(1, int((pump_runtime * (settings['flowrate'] / 100)))) 
#             #print(f'Calculated Pump Runtime for {drink_ingredient} = {calculated_pump_runtime}')
#             pump_t = threading.Thread(target=Pour, args=(pump_number,calculated_pump_runtime,platform))
#             pumpThreads.append(pump_t)
        
#         # start the pump threads		
#         for thread in pumpThreads:
#             thread.start()

#         # Report Progress to WebUI
#         for x in range(total_runtime):
#             current_count += 1
#             status = ReadStatus()
#             if (status['control']['stop'] == 1):
#                 stop_threads = True
#                 time.sleep(2)
#                 stop_threads = False
#                 break
#             percent_progress = int((current_count / total_runtime) * 100)
#             status['status']['progress'] = percent_progress
#             WriteStatus(status) 
#             time.sleep(1)

#         # wait for threads to finish
#         for thread in pumpThreads:
#             thread.join()
   
#         print('Finished dispensing drink.')

#         # Add a 4-second delay before starting the mixer
#         time.sleep(4)
#         print('Starting mixer...')
#         # Start the mixer (replace 'start_mixer()' with actual mixer control logic)
#         platform.start_mixer()

#         print('Finished. Cleaning up status file.')
#         status['status']['active'] = 0
#         status['control']['start'] = 0
#         status['control']['stop'] = 0
#         WriteStatus(status)

#     else:
#         print('Error, no drinks match that name.')



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
#         global stop_threads

#         # Initialize Platform Object
#         settings = ReadSettings()
#         platform = PumpControl(settings)

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
#                     break  # Stop searching once the correct pump is found

#             # Calculate runtime for this ingredient
#             calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
#             pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
#             pumpThreads.append(pump_t)

#         # Start the pump threads
#         for thread in pumpThreads:
#             thread.start()

#         # Monitor and report progress to WebUI
#         for x in range(total_runtime):
#             current_count += 1
#             status = ReadStatus()
#             if status['control']['stop'] == 1:
#                 stop_threads = True
#                 time.sleep(2)
#                 stop_threads = False
#                 break
#             percent_progress = int((current_count / total_runtime) * 100)
#             status['status']['progress'] = percent_progress
#             WriteStatus(status)
#             time.sleep(1)

#         # Wait for threads to finish
#         for thread in pumpThreads:
#             thread.join()

#         print('Finished dispensing drink.')

#         # Add a 4-second delay before starting the mixer
#         time.sleep(4)
#         print('Starting mixer...')
#         # Start the mixer (replace 'start_mixer()' with actual mixer control logic)
#         platform.start_mixer()

#         print('Finished. Cleaning up status file.')
#         status['status']['active'] = 0
#         status['control']['start'] = 0
#         status['control']['stop'] = 0
#         WriteStatus(status)

#         # Update the quantities in settings.json
#         UpdateQuantities(drink_name, drink_db, settings)

#     else:
#         print('Error, no drinks match that name.')

#working code of drink dispense 

# def PourDrink(drink_name):
#     drink_db = ReadDrinkDB()
#     if (drink_name in drink_db['drinks']):
#         # Set Active Status
#         status = ReadStatus()
#         status['status']['active'] = 1
#         WriteStatus(status)

#         total_runtime = 0
#         percent_progress = 0
#         current_count = 0
#         global stop_threads

#         # Initialize Platform Object
#         settings = ReadSettings()
#         platform = PumpControl(settings)

#         print(f'Starting to prepare {drink_name}')
#         # Cycle through each ingredient in the drink recipe to get the highest runtime, to get the total runtime
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             #total_runtime = total_runtime + int(pump_runtime * (settings['flowrate'] / 100))
#             total_runtime = max(total_runtime, int(pump_runtime * (settings['flowrate'] / 100)))

#         print(f'Total Runtime: {total_runtime}')

#         # Cycle through each ingredient and create threads to dispense the beverage
#         pumpThreads = []
#         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
#             pump_number = 'none'
#             for index, value in settings['inventory'].items():
#                 if(value == drink_ingredient):
#                     pump_number = index
#                     print(f"The pum number is {pump_number} using quantity {pump_runtime}")
#                     # print(f'Pump number = {index}')
#                     # pump_01 = 90ml
                    
                    
#             if pump_number != 'none':
#                 # Calculate the used quantity
#                 used_quantity = pump_runtime
#                 current_quantity = settings['quantity'][pump_number]
#                 print(f"The current quantity of {pump_number} is {current_quantity}")
#                 new_quantity = max(0, current_quantity - used_quantity)  # Ensure it doesn't go below 0
#                 settings['quantity'][pump_number] = new_quantity

#                 print(f"Used {used_quantity} units of {drink_ingredient}. Remaining: {new_quantity} units.")

#                 # Update progress bar percentage
#                 if current_quantity > 0:
#                     percentage = (new_quantity / current_quantity) * 100
#                 else:
#                     percentage = 0  # Handle edge case where current_quantity might be zero
#                 print(f"Progress for pump {pump_number}: {percentage}%")

#                 # Calculate pump runtime
#                 calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))

#                 # Start pouring in a thread
#                 pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
#                 pumpThreads.append(pump_t)
        
#         # start the pump threads		
#         for thread in pumpThreads:
#             thread.start()

#         # Report Progress to WebUI
#         for x in range(total_runtime):
#             current_count += 1
#             status = ReadStatus()
#             if (status['control']['stop'] == 1):
#                 stop_threads = True
#                 time.sleep(2)
#                 stop_threads = False
#                 break
#             percent_progress = int((current_count / total_runtime) * 100)
#             status['status']['progress'] = percent_progress
#             WriteStatus(status) 
#             time.sleep(1)

#        # Wait for threads to finish
#         for thread in pumpThreads:
#             thread.join()

#         print('Finished dispensing drink.')

#         # Add a 4-second delay before starting the mixer
#         time.sleep(4)
#         print('Starting mixer...')
#         platform.start_mixer()  # Start the mixer

#         # Write updated settings back to settings.json
#         WriteSettings(settings)

#         print('Finished. Cleaning up status file.')
#         status['status']['active'] = 0
#         status['control']['start'] = 0
#         status['control']['stop'] = 0
#         WriteStatus(status)

#     else:
#         print('Error, no drinks match that name.')



# def connect_to_wifi(ssid):
#     ssid = sanitize_ssid(ssid)

#     # Attempt to connect to the Wi-Fi network
#     command = ['netsh', 'wlan', 'connect', f'name={ssid}']
#     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     if result.returncode != 0:
#         error_message = result.stderr.decode('utf-8')
#         return {"status": "500", "message": f"Failed to connect to {ssid}."}
    
#     # Wait for the connection to establish
#     time.sleep(3)
    
#     # Check the connection status
#     status_command = ['netsh', 'wlan', 'show', 'interfaces']
#     status_result = subprocess.run(status_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     if status_result.returncode == 0:
#         output = status_result.stdout.decode('utf-8')
#         if ("connected" in output):
#             return {'status': "200", "message": f"Successfully connected to {ssid}"}
#         else:
#             return {"status": "500", "message": f"Failed to connect {ssid}."}
#     else:
#         error_message = status_result.stderr.decode('utf-8')
#         return {"status": "500", "message": f"Failed to verify connection to {ssid}."}


# def create_wifi_profile(ssid, password):
#     ssid = sanitize_ssid(ssid)
#     profile = f"""<?xml version="1.0"?>
#     <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
#         <name>{ssid}</name>
#         <SSIDConfig>
#             <SSID>
#                 <name>{ssid}</name>
#             </SSID>
#         </SSIDConfig>
#         <connectionType>ESS</connectionType>
#         <connectionMode>auto</connectionMode>
#         <MSM>
#             <security>
#                 <authEncryption>
#                     <authentication>WPA2PSK</authentication>
#                     <encryption>AES</encryption>
#                     <useOneX>false</useOneX>
#                 </authEncryption>
#                 <sharedKey>
#                     <keyType>passPhrase</keyType>
#                     <protected>false</protected>
#                     <keyMaterial>{password}</keyMaterial>
#                 </sharedKey>
#             </security>
#         </MSM>
#     </WLANProfile>
#     """

#     profile_filename = f'{ssid}.xml'
    
#     try:
#         with open(profile_filename, 'w') as file:
#             file.write(profile)

#         # Add the Wi-Fi profile using netsh
#         result = subprocess.run(['netsh', 'wlan', 'add', 'profile', f'filename={profile_filename}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         os.remove(profile_filename)
#         print(result.returncode)
#         if result.returncode != 0:
#             error_message = result.stderr.decode('utf-8')
#             return {"status": "500", "message": f"Failed to connect to {ssid}."}

#         # Attempt to connect to the Wi-Fi network
#         connect_result = subprocess.run(['netsh', 'wlan', 'connect', f'name={ssid}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#         if connect_result.returncode != 0:
#             connect_error_message = connect_result.stderr.decode('utf-8')
#             return {"status": "500", "message": f"Failed to connect to {ssid}."}
        
#         # Wait for the connection to establish
#         time.sleep(3)
        
#         # Verify the connection status
#         status_command = ['netsh', 'wlan', 'show', 'interfaces']
#         status_result = subprocess.run(status_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#         if status_result.returncode == 0:
#             output = status_result.stdout.decode('utf-8')
#             if ("connected" in output):
#                 return {"status": "200", "message": f"Successfully connected to {ssid}."}
#             else:
#                 return {"status": "500", "message": f"Failed to connect {ssid}. "}
#         else:
#             error_message = status_result.stderr.decode('utf-8')
#             return {"status": "500", "message": f"Failed to verify connection to {ssid}."}
    
#     except Exception as e:
#         return {"status": "500", "message": f"An unexpected error occurred: {str(e)}"}

# def create_wifi_profile(ssid, password):
#     """Create and configure a WiFi profile based on the platform."""
#     ssid = sanitize_ssid(ssid)
    
#     try:
#         if platform.system() == 'Windows':
#             profile = f"""<?xml version="1.0"?>
#             <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
#                 <name>{ssid}</name>
#                 <SSIDConfig>
#                     <SSID>
#                         <name>{ssid}</name>
#                     </SSID>
#                 </SSIDConfig>
#                 <connectionType>ESS</connectionType>
#                 <connectionMode>auto</connectionMode>
#                 <MSM>
#                     <security>
#                         <authEncryption>
#                             <authentication>WPA2PSK</authentication>
#                             <encryption>AES</encryption>
#                             <useOneX>false</useOneX>
#                         </authEncryption>
#                         <sharedKey>
#                             <keyType>passPhrase</keyType>
#                             <protected>false</protected>
#                             <keyMaterial>{password}</keyMaterial>
#                         </sharedKey>
#                     </security>
#                 </MSM>
#             </WLANProfile>
#             """

#             profile_filename = f'{ssid}.xml'
#             with open(profile_filename, 'w') as file:
#                 file.write(profile)

#             # Add the Wi-Fi profile using netsh
#             result = subprocess.run(['netsh', 'wlan', 'add', 'profile', f'filename={profile_filename}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             os.remove(profile_filename)
#             if result.returncode != 0:
#                 return {"status": "500", "message": f"Failed to add profile for {ssid}."}

#             return {"status": "200", "message": "Profile created successfully."}
        
#         elif platform.system() == 'Linux':
#             # Linux does not need to create an XML profile; just configure via wpa_supplicant directly
#             config_file = '/etc/wpa_supplicant/wpa_supplicant.conf'
#             with open(config_file, 'a') as f:
#                 f.write(f"""
# network={{
#     ssid="{ssid}"
#     psk="{password}"
# }}
# """)
            
#             # Reconfigure wpa_supplicant to use the new configuration
#             result = subprocess.run(['sudo', 'wpa_cli', '-i', 'wlan0', 'reconfigure'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             if result.returncode != 0:
#                 return {"status": "500", "message": f"Failed to configure WiFi for {ssid}."}
            
#             return {"status": "200", "message": "Profile created successfully."}
        
#         else:
#             return {"status": "501", "message": "WiFi profile creation not implemented for this platform."}
    
#     except Exception as e:
#         return {"status": "500", "message": f"An unexpected error occurred: {str(e)}"}
# import platform
# import subprocess
# import os


# @app.route('/disconnect-wifi', methods=['POST'])
# def disconnect_wifi():
#     try:
#         if platform.system() == 'Windows':
#             result = subprocess.run(['netsh', 'wlan', 'disconnect'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
#             if result.returncode == 0:
#                 return jsonify({"status": "200", "message": "Disconnected successfully."})
#             else:
#                 return jsonify({"status": "500", "message": f"Failed to disconnect"})
#         else:
#             return jsonify({"status": "501", "message": "Disconnect not implemented for this platform."})
        
#     except Exception as e:
#         return jsonify({"status": "500", "message": f"An unexpected error occurred: {str(e)}"})


# def get_wifi_networks():
#     try:
#         if platform.system() == 'Linux':
#             result = subprocess.run(['nmcli', '-t', '-f', 'ACTIVE,SSID', 'dev', 'wifi'], stdout=subprocess.PIPE)
#         elif platform.system() == 'Windows':
#             result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE)
        
#         networks_output = result.stdout.decode('utf-8')
        
#         ssid_list = re.findall(r'SSID \d+ : (.+)', networks_output)
        
#         connected_ssid = None
#         if platform.system() == 'Windows':
#             connected_ssid_match = re.search(r'\s*SSID\s*:\s*(.+)\s*$', networks_output, re.IGNORECASE)
#             connected_ssid = connected_ssid_match.group(1).strip() if connected_ssid_match else None
#         elif platform.system() == 'Linux':
#             connected_ssid_match = re.search(r'yes:(.+)', networks_output)
#             connected_ssid = connected_ssid_match.group(1).strip() if connected_ssid_match else None
            
#         return {"available_networks": ssid_list, "connected_ssid": connected_ssid}
#     except Exception as e:
#         return {"available_networks": [], "connected_ssid": None}

#working fine code of dispense 

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
#         global stop_threads

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
#                     break  # Stop searching once the correct pump is found

#             # Calculate runtime for this ingredient
#             calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
#             pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
#             pumpThreads.append(pump_t)

#             # Update the quantity of this pump immediately after calculating runtime
#             used_quantity = int(pump_runtime * (settings['flowrate'] / 100))
            
#             if pump_number in settings['quantity']:
#                 original_quantity = settings['quantity'][pump_number]
#                 #updated_quantity = 70ml(original_quantity)-20ml(used_quantity)
#                 settings['quantity'][pump_number] = max(0, original_quantity - used_quantity)
#                 #availabe quantity (Updating)
                
#                 #here checking availabe quantity is greater than 0 or not
            
#                 if (settings['quantity'][pump_number] > 0):
#                     percentage = ((settings['quantity'][pump_number] / original_quantity) * 100)
#                 else:
#                     percentage = 0  # Handle edge case where current_quantity might be zero
                    
#                 print(f"Progress for pump {pump_number}: {percentage}%")
                
#                 settings['percentage'][pump_number] = percentage


#         # Start the pump threads
#         for thread in pumpThreads:
#             thread.start()

#         # Monitor and report progress to WebUI
#         for x in range(total_runtime):
#             current_count += 1
#             status = ReadStatus()
#             if status['control']['stop'] == 1:
#                 stop_threads = True
#                 time.sleep(2)
#                 stop_threads = False
#                 break
#             percent_progress = int((current_count / total_runtime) * 100)
#             status['status']['progress'] = percent_progress
#             WriteStatus(status)
#             time.sleep(1)

#         # Wait for threads to finish
#         for thread in pumpThreads:
#             thread.join()

#         print('Finished dispensing drink.')
#         # Write updated settings to file after updating quantities for all pumps
#         WriteSettings(settings)

#         # Add a 4-second delay before starting the mixer
#         time.sleep(4)
#         print('Starting mixer...')
#         platform.start_mixer()

#         print('Finished. Cleaning up status file.')
#         status['status']['active'] = 0
#         status['control']['start'] = 0
#         status['control']['stop'] = 0
#         WriteStatus(status)

#     else:
#         print('Error, no drinks match that name.')


# def remove_wifi_profile(ssid):
#     """Remove a WiFi profile based on the SSID from wpa_supplicant.conf."""
#     ssid = sanitize_ssid(ssid)
    
#     if platform.system() == 'Linux':
#         interface = 'wlan0'  # Adjust if needed
#         try:
#             # Check current networks
#             networks_before = subprocess.run(['sudo', 'wpa_cli', '-i', interface, 'list_networks'], 
#                                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             print("Networks before removal:", networks_before.stdout.decode('utf-8'))
            
#             # Remove the network
#             remove_result = subprocess.run(['sudo', 'wpa_cli', '-i', interface, 'remove_network', ssid], 
#                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             if remove_result.returncode != 0:
#                 return {"status": "500", "message": f"Failed to remove WiFi profile: {remove_result.stderr.decode('utf-8').strip()}"}
            
#             # Reconfigure wpa_supplicant
#             reconfigure_result = subprocess.run(['sudo', 'wpa_cli', '-i', interface, 'reconfigure'], 
#                                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             if reconfigure_result.returncode != 0:
#                 return {"status": "500", "message": f"Failed to reconfigure WiFi: {reconfigure_result.stderr.decode('utf-8').strip()}"}
            
#             # Check current networks again
#             networks_after = subprocess.run(['sudo', 'wpa_cli', '-i', interface, 'list_networks'], 
#                                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             print("Networks after removal:", networks_after.stdout.decode('utf-8'))
            
#             return {"status": "200", "message": "Profile removed and reconfigured successfully."}
        
#         except Exception as e:
#             return {"status": "500", "message": f"An unexpected error occurred: {str(e)}"}
    
#     else:
#         return {"status": "501", "message": "WiFi profile removal not implemented for this platform."}

# @app.route('/disconnect-wifi', methods=['POST'])
# def disconnect_wifi():
#     """Disconnect from the current WiFi network."""
#     try:
#         if platform.system() == 'Windows':
#             # Attempt to disconnect using Windows command
#             result = subprocess.run(['netsh', 'wlan', 'disconnect'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             if result.returncode == 0:
#                 # Optionally, scan for available networks
#                 scan_result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 print(scan_result.stdout.decode('utf-8'))
#                 return jsonify({"status": "200", "message": "Disconnected successfully.", "available_networks": scan_result.stdout.decode('utf-8')})
#             else:
#                 error_message = result.stderr.decode('utf-8').strip()
#                 return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})

#         elif platform.system() == 'Linux':
#             # Attempt to disconnect using Linux command
#             # disconnect_result = subprocess.run(['sudo', 'ip', 'link', 'set', 'wlan0', 'down'], 
#             #                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             # if disconnect_result.returncode == 0:
#             #     reavailable_network =  subprocess.run(
#             #         ['sudo', 'ip', 'link', 'set', 'wlan0', 'up'],
#             #         stdout=subprocess.PIPE, stderr=subprocess.PIPE
#             #     )
#             #     print(reavailable_network)
#             #     return jsonify({"status": "200", "message": "Disconnected successfully."})
#             # else:
#             #     error_message = disconnect_result.stderr.decode('utf-8').strip()
#             #     return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})
#             networks = get_wifi_networks()
#             ssid_to_remove = networks['connected_ssid']
#             print('Want to remove ssid', ssid_to_remove)
            
#             if not ssid_to_remove:
#                 return jsonify({"status": "404", "message": "No network is currently connected."})
            
#             # Remove the Wi-Fi profile
#             removal_result = remove_wifi_profile(ssid_to_remove)
#             if removal_result['status'] == '200':
#                 # Disconnect Wi-Fi interface
#                 disconnect_result = subprocess.run(['sudo', 'ip', 'link', 'set', 'wlan0', 'down'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 if disconnect_result.returncode == 0:
#                     # Re-enable the interface if needed
#                     reconnect_result = subprocess.run(['sudo', 'ip', 'link', 'set', 'wlan0', 'up'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                     if reconnect_result.returncode == 0:
#                         return jsonify({"status": "200", "message": "Disconnected and profile removed successfully."})
#                     else:
#                         error_message = reconnect_result.stderr.decode('utf-8').strip()
#                         return jsonify({"status": "500", "message": f"Failed to re-enable Wi-Fi interface: {error_message}"})
#                 else:
#                     print("something went wrong")
#                     error_message = disconnect_result.stderr.decode('utf-8').strip()
#                     return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})
#             else:
#                 return jsonify(removal_result)

#     except Exception as e:
#         return jsonify({"status": "500", "message": f"An unexpected error occurred: {str(e)}"})
    
# @app.route('/disconnect-wifi', methods=['POST'])
# def disconnect_wifi():
#     """Disconnect from the current WiFi network."""
#     try:
#         if platform.system() == 'Windows':
#             # Attempt to disconnect using Windows command
#             result = subprocess.run(['netsh', 'wlan', 'disconnect'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             if result.returncode == 0:
#                 # Optionally, scan for available networks
#                 scan_result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 print(scan_result.stdout.decode('utf-8'))
#                 return jsonify({"status": "200", "message": "Disconnected successfully.", "available_networks": scan_result.stdout.decode('utf-8')})
#             else:
#                 error_message = result.stderr.decode('utf-8').strip()
#                 return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})

#         elif platform.system() == 'Linux':
#             # Attempt to disconnect using Linux command
#             disconnect_result = subprocess.run(['sudo', 'ip', 'link', 'set', 'wlan0', 'down'], 
#                                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             if disconnect_result.returncode == 0:
#                 reavailable_network =  subprocess.run(
#                     ['sudo', 'ip', 'link', 'set', 'wlan0', 'up'],
#                     stdout=subprocess.PIPE, stderr=subprocess.PIPE
#                 )
#                 print(reavailable_network)
#                 return jsonify({"status": "200", "message": "Disconnected successfully."})
#             else:
#                 error_message = disconnect_result.stderr.decode('utf-8').strip()
#                 return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})

#     except Exception as e:
#         return jsonify({"status": "500", "message": f"An unexpected error occurred: {str(e)}"})


##################### admin.js working code############################################
# // function cleanPumpAction(pumpNumber) {
# //     event.preventDefault();

# //     const startButton = document.getElementById(`start_${pumpNumber}`);
# //     const stopButton = document.getElementById(`stop_${pumpNumber}`);
# //     console.log("The selected pump by action", pumpNumber);

# //     const data = {
# //         pump_number: pumpNumber,
# //         action: 'clean'
# //     };

# //     fetch('/admin/pump_clean', {
# //         method: 'POST',
# //         headers: {
# //             'Content-Type': 'application/json',
# //         },
# //         body: JSON.stringify(data)
# //     }).then(response => response.json())
# //         .then(data => {
# //             console.log('Pump action response:', data);
# //             const messageContainer = document.querySelector('.message-container');
# //             const successMessageElement = document.getElementById('success-message');
# //             const errorMessageElement = document.getElementById('error-message');
    
# //             if (data.status === 'success') {
# //                 messageContainer.style.display = "block";
# //                 successMessageElement.classList.remove('hidden');
# //                 successMessageElement.classList.add("show-message");
# //                 successMessageElement.innerHTML = data.message;
# //                 startButton.style.display = 'none';
# //                 stopButton.style.display = 'inline-block';

# //                 const intervalId = setInterval(() => {
# //                     checkPumpStatus(pumpNumber, intervalId);
# //                 }, 2000);

# //                 setTimeout(function () {
# //                     messageContainer.style.display = "none";
# //                 successMessageElement.classList.add('hidden');
# //                 successMessageElement.classList.remove("show-message");
# //                 }, 5000);
                
# //             } else {
# //                 messageContainer.style.display = "block";
# //                 errorMessageElement.classList.remove('hidden');
# //                 errorMessageElement.classList.add("show-message")
# //                 errorMessageElement.innerHTML = data.message;
# //                 setTimeout(function () {
# //                     errorMessageElement.classList.add('hidden');
# //                     errorMessageElement.classList.remove("show-message");
# //                     messageContainer.style.display = "none";
# //                 }, 5000);
# //             }
# //         })
# //         .catch(error => console.error('Error:', error));
# // }

# // function checkPumpStatus(pumpNumber, intervalId) {
# //     fetch('/workstatus', {
# //         method: 'GET'
# //     }).then(response => response.json())
# //         .then(data => {
# //             if (data.percent_done === 100) {

# //                 var successMessageElement = document.getElementById('success-message');

# //                 console.log(data.percent_done);
# //                 console.log(`Cleaning process for pump ${pumpNumber} completed.`);
# //                 clearInterval(intervalId); 

# //                 const startButton = document.getElementById(`start_${pumpNumber}`);
# //                 const stopButton = document.getElementById(`stop_${pumpNumber}`);

# //                 startButton.style.display = 'inline-block';
# //                 stopButton.style.display = 'none';

# //                 successMessageElement.classList.remove('hidden');
# //                 successMessageElement.classList.add("show-message");
# //                 successMessageElement.innerHTML = `Cleaning process for pump ${pumpNumber} completed.`;
# //                 setTimeout(function () {
# //                     successMessageElement.classList.add('hidden');
# //                     successMessageElement.classList.remove("show-message");
# //                 }, 5000);
# //             }
# //         })
# //         .catch(error => console.error('Error:', error));
# // }

# // function cancelPumpAction(pumpNumber) {
# //     event.preventDefault();

# //     const startButton = document.getElementById(`start_${pumpNumber}`);
# //     const stopButton = document.getElementById(`stop_${pumpNumber}`);

# //     const data = {
# //         pump_number: pumpNumber,
# //         action: 'cancel'
# //     };

# //     fetch('/admin/pump_clean', {
# //         method: 'POST',
# //         headers: {
# //             'Content-Type': 'application/json',
# //         },
# //         body: JSON.stringify(data)
# //     }).then(response => response.json())
# //         .then(data => {
# //             console.log('Cancel action response:', data);
# //             const messageContainer = document.querySelector('.message-container');
# //             var errorMessageElement = document.getElementById('error-message');
            
# //             if (data.status === 'success') {
# //                 startButton.style.display = 'inline-block';
# //                 stopButton.style.display = 'none';
# //                 messageContainer.style.display = "block";
# //                 errorMessageElement.classList.remove('hidden');
# //                 errorMessageElement.classList.add("show-message");
# //                 errorMessageElement.innerHTML = data.message;
# //                 setTimeout(function () {
# //                     messageContainer.style.display = "none";
# //                     errorMessageElement.classList.add('hidden');
# //                     errorMessageElement.classList.remove("show-message");
# //                 }, 5000);
# //             }
# //         })
# //         .catch(error => console.error('Error:', error));
# // }



# def ReadSettings():
#     # *****************************************
#     # Read Settings from File
#     # *****************************************

#     # Read all lines of settings.json into an list(array)
#     try:
#         json_data_file = open("settings.json", "r")
#         json_data_string = json_data_file.read()
#         settings = json.loads(json_data_string)
#         json_data_file.close()
#     except(IOError, OSError):
#         # Issue with reading states JSON, so create one/write new one
#         settings = {}

#         settings['inventory'] = {
#             "pump_01": "rum",
#             "pump_02": "vodka",
#             "pump_03": "whiskey",
#             "pump_04": "coke",
#             "pump_05": "oj",
#             "pump_06": "tequila",
#             "pump_07": "marg_mix",
#             "pump_08": "iced_tea"
#             }

#         settings['assignments'] = {
#             "pump_01": 17,
#             "pump_02": 27,
#             "pump_03": 22,
#             "pump_04": 23,
#             "pump_05": 24,
#             "pump_06": 25,
#             "pump_07": 2,
#             "pump_08": 3
#             }

#         settings['flowrate'] = 85

#         WriteSettings(settings)

#     return(settings)

# def WriteSettings(settings):
#     # *****************************************
#     # Write all settings to JSON file
#     # *****************************************
#     json_data_string = json.dumps(settings)
#     with open("settings.json", 'w') as settings_file:
#         settings_file.write(json_data_string)


# // pop up modal
# // function openModal(drinkName) {
# //   let inputField = document.createElement('input');
# //   inputField.type = 'hidden';
# //   inputField.name = 'makedrink';
# //   inputField.value = drinkName;

# //   let form = document.getElementById('drinkForm');
# //   form.appendChild(inputField);

# //   document.getElementById("drinkModal").style.display = "block";
# //   document.body.classList.add("modal-open");
  
# //   $('#drinklist').carousel('pause');
# // }

# // function closeModal() {
# //   var video = document.querySelector("#drinkModal video");
# //   if (video) {
# //     video.pause();
# //     video.currentTime = 0;
# //   }

# //   document.getElementById("drinkModal").style.display = "none";
# //   document.body.classList.remove("modal-open");

# //  // Resume the carousel
# //  $('#drinklist').carousel('cycle');
# // }


	# <!-- <script>
	# 	var worker = null; // Worker to handle the interval
	# 	var isPaused = false; // Track pause/resume state

	# 	$('#donebutton').hide(); // Initially hide the "Done" button

	# 	$(document).ready(function () {
	# 		function updateProgress() {
	# 			if (!isPaused) {
	# 				$.ajax({
	# 					url: '/workstatus',
	# 					type: 'GET',
	# 					success: function (data) {
	# 						var loaded = data.percent_done; // Progress percentage
	# 						$('#counter').html(loaded + '%');
	# 						$('#progress-bar').css('width', loaded + '%');

	# 						if (loaded == 100) {
	# 							stopWorking();
	# 						}
	# 					}
	# 				});
	# 			}
	# 		}

	# 		function stopWorking() {
	# 			clearInterval(worker); // Stop the worker interval
	# 			$('#pauseResumeButton').hide(); // Hide the Pause/Resume button
	# 			$('#statusMessage').html('All done!');
	# 			$('#donebutton').show(); // Show the "Done" button
	# 			setTimeout(function () {
	# 				location.replace("/"); // Redirect to the homepage after 30 seconds
	# 			}, 30000);
	# 		}

	# 		// Handle Pause/Resume button click
	# 		$('#pauseResumeButton').on('click', function () {
	# 			if (isPaused) {
	# 				isPaused = false;
	# 				$(this).text('Pause');
	# 				$.get('/work/resume');
	# 				worker = setInterval(updateProgress, 1000);
	# 			} else {
	# 				isPaused = true;
	# 				$(this).text('Resume');
	# 				clearInterval(worker);
	# 				$.get('/work/pause');
	# 			}
	# 		});


	# 		worker = setInterval(updateProgress, 1000);
	# 	});
	# </script> -->

# // function cleanPumpAction(pumpNumber) {

# //   const startButton = document.getElementById(`start_${pumpNumber}`);
# //   const stopButton = document.getElementById(`stop_${pumpNumber}`);

# //   const data = {
# //     pump_number: pumpNumber,
# //     action: "clean",
# //   };

# //   fetch("/inventory/pump/refill", {
# //     method: "POST",
# //     headers: {
# //       "Content-Type": "application/json",
# //     },
# //     body: JSON.stringify(data),
# //   })
# //     .then((response) => response.json())
# //     .then((data) => {
# //       const messageContainer = document.querySelector(".message-container");
# //       const successMessageElement = document.getElementById("success-message");
# //       const errorMessageElement = document.getElementById("error-message");

# //       if (data.status === "success") {
# //         messageContainer.style.display = "block";
# //         successMessageElement.classList.remove("hidden");
# //         successMessageElement.classList.add("show-message");
# //         successMessageElement.innerHTML = data.message;
# //         startButton.style.display = "none";
# //         stopButton.style.display = "inline-block";

# //         // Store interval ID so it can be cleared later
# //         pumpIntervals[pumpNumber] = setInterval(() => {
# //           checkPumpStatus(pumpNumber, pumpIntervals[pumpNumber]);
# //         }, 2000);

# //         setTimeout(function () {
# //           messageContainer.style.display = "none";
# //           successMessageElement.classList.add("hidden");
# //           successMessageElement.classList.remove("show-message");

# //           errorMessageElement.classList.add("hidden");
# //           errorMessageElement.classList.remove("show-message");
# //         }, 3000);
# //       } else {
# //         messageContainer.style.display = "block";
# //         errorMessageElement.classList.remove("hidden");
# //         errorMessageElement.classList.add("show-message");
# //         errorMessageElement.innerHTML = data.message;
# //         setTimeout(function () {
# //           messageContainer.style.display = "none";
# //           errorMessageElement.classList.add("hidden");
# //           errorMessageElement.classList.remove("show-message");
# //           successMessageElement.classList.add("hidden");
# //           successMessageElement.classList.remove("show-message");
# //         }, 3000);
# //       }
# //     })
# //     .catch((error) => console.error("Error:", error));
# // }
####################Working code###############
# var worker = null;
# 		var isPaused = false;

# 		$('#donebutton').hide();

# 		$(document).ready(function () {
# 			function updateProgress() {
# 				if (!isPaused) {
# 					$.ajax({
# 						url: '/workstatus',
# 						type: 'GET',
# 						success: function (data) {
# 							var loaded = data.percent_done;
# 							$('#counter').html(loaded + '%');
# 							$('#progress-bar').css('width', loaded + '%');

# 							if (loaded >= 100) {
# 								stopWorking();
# 							}
# 						}
# 					});
# 				}
# 			}

# 			function stopWorking() {
# 				clearInterval(worker);
# 				$('#pauseResumeButton').hide();
# 				$('#statusMessage').html('All done!');
# 				$('#donebutton').show();
# 				setTimeout(function () {
# 					location.replace("/");
# 				}, 10000);
# 			}

# 			$('#pauseResumeButton').on('click', function () {
# 				if (isPaused) {
# 					isPaused = false;
# 					$(this).text('Pause');
# 					$.get('/work/resume');
# 					worker = setInterval(updateProgress, 1000);
# 				} else {
# 					isPaused = true;
# 					$(this).text('Resume');
# 					clearInterval(worker);
# 					$.get('/work/pause');
# 					document.getElementById('dispenseModal').style.display = 'block';
# 				}
# 			});

# 			worker = setInterval(updateProgress, 1000);
# 		});
# import socket
# import os

# SERVER_PORT = 5500

# def get_my_ip():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     try:
#         s.connect(("8.8.8.8", 80))
#         ip = s.getsockname()[0]
#     finally:
#         s.close()
#     return ip


# def get_subnet(ip):
#     parts = ip.split(".")
#     return f"{parts[0]}.{parts[1]}.{parts[2]}."

# # def find_server(port=SERVER_PORT):
# #     my_ip = get_my_ip()
# #     subnet = get_subnet(my_ip)

# #     print(f"My IP     : {my_ip}")
# #     print(f"Subnet    : {subnet}0/24")
# #     print("Scanning for server...")
    
# #     for i in range(1, 255):
# #         ip = subnet + str(i)
# #         print(ip)
# #         try:
# #             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #             s.settimeout(0.15)
# #             s.connect((ip, port))
# #             s.close()
# #             print(f"✅ Server found at: {ip}")
# #             return ip
# #         except:
# #             pass

# #     print("❌ Server not found")
# #     return None


# def find_server(timeout=10):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.bind(("", 9999))
#     sock.settimeout(timeout)

#     print("Listening for server...")

#     try:
#         data, addr = sock.recvfrom(1024)
#         msg = data.decode()

#         if msg.startswith("MONITOR_SERVER"):
#             print(f"✅ Server found at: {addr[0]}")
#             return addr[0]

#     except socket.timeout:
#         print("❌ No server found")
#         return None

# @app.route('/quantity-status', methods=['POST', 'GET'])
# def quantityStatus():
#     settings = ReadSettings()   
#     errormessage = []
    
#     for pump_number, quantity in settings['quantity'].items():
#         if pump_number == 'pump_16':
#             continue
#         percentage = (settings['in_quantity'].get(pump_number, 0)/1000) * 100
#         inQuantity = settings['in_quantity'].get(pump_number, 0)

#         if inQuantity <= 200:
#             errormessage.append({
#                 'pump_number': pump_number,
#                 'available_quantity': inQuantity,
#                 'status': 'Alert: Below 200 Threshold'
#             })
        
#         elif inQuantity <= 100:
#             errormessage.append({
#                 'pump_number': pump_number,
#                 'available_quantity': inQuantity,
#                 'status': 'Alert: Below 100 Threshold'
#             })
#             print(errormessage)
       
#     return jsonify({
#         'status': 'error',
#         'errormessage': errormessage
#     })
#############################
# from flask import Flask, flash, url_for, request, render_template, make_response, jsonify, redirect
# from flask_cors import CORS
# import subprocess
# import time
# import os
# import json
# from datetime import datetime
# from common import *
# from werkzeug.utils import secure_filename
# import re
# import platform
# import random,string
# if platform.system() == "Windows":
#     from platform_prototype import SensorSignal  
# else:
#     from platform_raspi import SensorSignal  
# from version import __system_name__,__system_id__

# import threading

# app = Flask(__name__)
# CORS(app)

# moniterData = MoniterDB()
# metadata = ReadMetadata()

# @app.route('/', methods=['POST','GET'])
# def index():
#     print(platform.system())
#     settings = ReadSettings()
#     drink_db = ReadDrinkDB()
#     show_navbar = False  # Hide the navbar on this page
#     drinklist = {}
#     num_drinks = 0
#     moniterDB = MoniterDB()
#     moniterDB.write()

#     for drink_name, drink_details in drink_db['drinks'].items():
#         # Cycle through each ingredient in the drink recipe
#         for drink_ingredients in drink_details['ingredients'].items():
#             matched_ingredient = False

#             # Cycle through each ingredient in the inventory and check against the recipe
#             for ingredients_available in settings['inventory'].items():
#                 if (ingredients_available[1] == drink_ingredients[0]):
#                     matched_ingredient = True
                    
#             if(matched_ingredient == False):
#                 # If even one ingredient is missing from current inventory, then break from loop
#                 break

#         if(matched_ingredient == True):
#             drinklist[drink_name] = drink_db['drinks'][drink_name]
#             num_drinks += 1
#         # else:
#             # - Missing ingredients, not storing in drinklist.
#     for pump_number in settings['quantity'].keys():
#         moniterDB.ingridients(pump_number,settings['in_quantity'][pump_number],settings['quantity'][pump_number])
    
#     if (drinklist != {}):
#         errorcode = 0
#     else:
#         drinklist['empty'] = {
#             "empty": {
#                 "name": "No Drink Options",
#                 "description": "Sorry, it looks like you don't have any drink options with current ingredients.",
#                 "image": "empty.jpg",
#                 "ingredients": {
#                     "none": 0,
#                 }
#             }
#         }
#         num_drinks = 1
#         errorcode = 1
#     moniterDB.update_total_drink(num_drinks)
#     return render_template('index.html', show_navbar = True  , drinklist=drinklist, num_drinks=num_drinks, errorcode=errorcode)

# @app.route('/work/<action>', methods=['POST','GET'])
# @app.route('/work', methods=['POST','GET'])
# def do_work(action=None):
#     global pause_threads,stop_threads
#     status = ReadStatus()
#     drink_db = ReadDrinkDB()
#     moniterDB = MoniterDB()

#     if action == "pause":
#         status = ReadStatus()
#         if status['status']['active'] == 1:
#             pause_threads = True
#             status['control']['pause'] = 1  
#             WriteStatus(status)
#             print("Pouring paused.")
#         return render_template('work.html', action=action, workmode='pause')

#     if action == "resume":
#         status = ReadStatus()
#         if status['status']['active'] == 1 and pause_threads:
#             pause_threads = False
#             status['control']['pause'] = 0  
#             WriteStatus(status)
#             print("Pouring resumed.")
#         return render_template('work.html', action=action, workmode='dispense')
    
#     if action == 'cancel':
#         stop_threads = True
#         status['control']['pause'] = 0
#         status['control']['stop'] = 1
#         WriteStatus(status) 
#         return render_template('work.html', action=action, workmode='cancel')
    
#     if (request.method == 'POST') and (status['status']['active'] == 0):
#         response = request.form
#         if(response['makedrink'] in drink_db.get('drinks', {})):
#             drink_name = response['makedrink']
#             drink_info = drink_db['drinks'][drink_name]
#             drinkDespenseImage = drink_info['image']['drinkDespenseImage']
#             status['status']['active'] = 0
#             status['status']['progress'] = 0
#             status['control']['start'] = 1
#             status['control']['pause'] = 0
#             status['control']['stop'] = 0
#             status['control']['clean'] = ""
#             status['control']['drink_name'] = drink_name
#             WriteStatus(status)
            
#             return render_template('work.html', drink_name=drink_name, action="default", workmode='dispense',drinkDespenseImage=drinkDespenseImage)
#     return redirect('/')

# @app.route('/workstatus')
# def workstatus(action=None):
#     status = ReadStatus()
#     percent_done = status['status']['progress']
#     return jsonify({ 'percent_done' : percent_done})

# def generate_system_info(length=25):
#     key_file = 'system_key.txt'
#     all_characters = (string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

#     if not os.path.exists(key_file):
#         system_key = ''.join(random.choice(all_characters) for _ in range(length))
#         with open(key_file, 'w') as file:
#             file.write(system_key)
#         time.sleep(0.5) 
#     else:
#         time.sleep(0.5)   
#         with open(key_file, 'r') as file:
#             system_key = file.read().strip()

#     return {"system_key": system_key, "system_machine_name": __system_name__}

# def get_wifi_networks():
#     try:
#         if platform.system() == 'Linux':
#             result = subprocess.run(['sudo', 'iwlist', 'wlan0', 'scan'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             networks_output = result.stdout.decode('utf-8')

#             # Extract SSIDs from the iwlist output
#             ssid_list = re.findall(r'ESSID:"([^"]*)"', networks_output)
            
#             # Get the currently connected SSID
#             connected_ssid_result = subprocess.run(['iwgetid', '-r'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             connected_ssid_output = connected_ssid_result.stdout.decode('utf-8').strip()
#             connected_ssid = connected_ssid_output if connected_ssid_output else None
            
#             print(connected_ssid)
#             return {"available_networks": ssid_list, "connected_ssid": connected_ssid}
        
#         elif platform.system() == 'Windows':
#             result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             networks_output = result.stdout.decode('utf-8')

#             # Extract SSIDs from the network scan output
#             ssid_list = re.findall(r'SSID \d+ : (.+)', networks_output)

#             # Get the currently connected SSID using netsh wlan show interfaces
#             connected_result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             connected_output = connected_result.stdout.decode('utf-8')

#             # Extract the connected SSID from the interface output
#             connected_ssid_match = re.search(r'SSID\s*:\s*(.+)', connected_output)
#             connected_ssid = connected_ssid_match.group(1).strip() if connected_ssid_match else None
#             return {"available_networks": ssid_list, "connected_ssid": connected_ssid}
        
#     except Exception as e:
#         return {"available_networks": [], "connected_ssid": None}

# @app.route('/get-available-networks', methods=['GET'])
# def get_available_networks():
#     networks = get_wifi_networks()  
#     available_networks = networks.get('available_networks', [],)
#     return jsonify({'networks': available_networks,"message": f"We are trying fatching wifi network"}) 

# def sanitize_ssid(ssid):
#     print(ssid.strip())
#     return ssid.strip()

# def create_wifi_profile(ssid, password):
#     """Create and configure a WiFi profile based on the platform."""
#     ssid = sanitize_ssid(ssid)
    
#     # try:
#     if platform.system() == 'Windows':
#             # Create an XML profile for Windows
#             profile = f"""<?xml version="1.0"?>
#             <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
#                 <name>{ssid}</name>
#                 <SSIDConfig>
#                     <SSID>
#                         <name>{ssid}</name>
#                     </SSID>
#                 </SSIDConfig>
#                 <connectionType>ESS</connectionType>
#                 <connectionMode>auto</connectionMode>
#                 <MSM>
#                     <security>
#                         <authEncryption>
#                             <authentication>WPA2PSK</authentication>
#                             <encryption>AES</encryption>
#                             <useOneX>false</useOneX>
#                         </authEncryption>
#                         <sharedKey>
#                             <keyType>passPhrase</keyType>
#                             <protected>false</protected>
#                             <keyMaterial>{password}</keyMaterial>
#                         </sharedKey>
#                     </security>
#                 </MSM>
#             </WLANProfile>
#             """

#             profile_filename = f'{ssid}.xml'
#             try:
#                 with open(profile_filename, 'w') as file:
#                     file.write(profile)

#                 # Add the Wi-Fi profile using netsh
#                 result = subprocess.run(['netsh', 'wlan', 'add', 'profile', f'filename={profile_filename}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 if result.returncode != 0:
#                     error_message = result.stderr.decode('utf-8').strip()
#                     return {"status": "500", "message": f"Failed to add profile for {ssid}: {error_message}"}
                
#                 return {"status": "200", "message": "Profile created successfully."}
            
#             finally:
#                 # Remove the profile file after use
#                 if os.path.exists(profile_filename):
#                     os.remove(profile_filename)
        
#     elif platform.system() == 'Linux':
#             config_entry = f"""
#                 network={{
#                     ssid="{ssid}"
#                     psk="{password}"
#                     }}
#             """
#             print(config_entry)
#             config_file = '/etc/wpa_supplicant/wpa_supplicant.conf'
#             try:
#                 # Use 'sudo tee' to write to the file with superuser permissions
#                 process = subprocess.Popen(['sudo', 'tee', '-a', config_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 stdout, stderr = process.communicate(input=config_entry.encode('utf-8'))
#                 print(process)
                    
#                 if process.returncode != 0:
#                     return {"status": "500", "message": f"Failed to write to configuration file: {stderr.decode('utf-8').strip()}"}
                
#                 # Reconfigure wpa_supplicant
#                 result = subprocess.run(['sudo', 'wpa_cli', '-i', 'wlan0', 'reconfigure'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               
#                 if result.returncode != 0:
#                     return {"status": "500", "message": f"Failed to configure WiFi for {ssid}: {result.stderr.decode('utf-8').strip()}"}
#                 return {"status": "200", "message": "Profile created successfully."}
            
#             except subprocess.CalledProcessError as e:
#                 return {"status": "500", "message": f"Subprocess error: {str(e)}"}
#             except PermissionError:
#                 return {"status": "403", "message": "Permission denied. You need to run this as a superuser."}
#             except Exception as e:
#                 return {"status": "500", "message": f"An unexpected error occurred: {str(e)}"}
#     else:
#                 return {"status": "501", "message": "WiFi profile creation not implemented for this platform."}

# def connect_to_wifi(ssid):
#     """Connect to a WiFi network based on the platform."""
#     ssid = sanitize_ssid(ssid)
    
#     try:
#         if platform.system() == 'Windows':
#             # Attempt to connect to the Wi-Fi network
#             command = ['netsh', 'wlan', 'connect', f'name={ssid}']
#             result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#             if result.returncode != 0:
#                 return {"status": "500", "message": f"Failed to connect to {ssid}."}
            
#             # Wait for the connection to establish
#             time.sleep(6)
            
#             # Check the connection status
#             status_command = ['netsh', 'wlan', 'show', 'interfaces']
#             status_result = subprocess.run(status_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#             if status_result.returncode == 0:
#                 output = status_result.stdout.decode('utf-8')
#                 if "connected" in output:
#                     return {'status': "200", "message": f"Successfully connected to {ssid}"}
#                 else:
#                     return {"status": "500", "message": f"Failed to connect to {ssid}."}
#             else:
#                 return {"status": "500", "message": "Failed to verify connection."}
        
#         elif platform.system() == 'Linux':
#             # Linux assumes the WiFi profile was created; connect via `wpa_cli`
#             result = subprocess.run(['sudo', 'iwconfig', 'wlan0', 'essid', ssid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   
#             time.sleep(6)

#             if (result.returncode == 0):
#                return {"status": "200", "message": f"Successfully connected to {ssid}"}
#             else:
#                return {"status": "500", "message": f"Failed to connect to {ssid}."}
            
        
#         else:
#             return {"status": "501", "message": "Connection not implemented for this platform."}
    
#     except Exception as e:
#         return {"status": "500", "message": f"An unexpected error occurred: {str(e)}"}
    
# @app.route('/connect-via-wifi', methods=['GET', 'POST'])
# @app.route('/admin', methods=['GET', 'POST'])
# def connect_wifi():
#     if request.method == 'POST':
#         ssid = request.form['ssid'] 
#         password = request.form['password']
#         profile_status = create_wifi_profile(ssid, password)
#         if profile_status['status'] != "200":
#             return jsonify({'response': profile_status})

#         connection_status = connect_to_wifi(ssid)
#         print(connection_status)
#         return jsonify({'response': connection_status})

#     networks = get_wifi_networks()
#     system_generate_info = generate_system_info()
#     return render_template('connect_wifi.html', networks=networks,show_navbar = True,system_access_key = system_generate_info['system_key'],system_name = system_generate_info['system_machine_name'])
    
# @app.route('/disconnect-wifi', methods=['POST'])
# def disconnect_wifi():
#     """Disconnect from the current WiFi network and prevent automatic reconnection."""
#     try:
#         if platform.system() == 'Windows':
#             # Attempt to disconnect using Windows command
#             result = subprocess.run(['netsh', 'wlan', 'disconnect'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             if result.returncode == 0:
#                 scan_result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 return jsonify({"status": "200", "message": "Disconnected successfully.", "available_networks": scan_result.stdout.decode('utf-8')})
#             else:
#                 error_message = result.stderr.decode('utf-8').strip()
#                 return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})

#         elif platform.system() == 'Linux':
#             # Disconnect using Linux command
#             disconnect_result = subprocess.run(['sudo', 'ip', 'link', 'set', 'wlan0', 'down'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             if disconnect_result.returncode == 0:
#                 config_file = '/etc/wpa_supplicant/wpa_supplicant.conf'
                
#                 networks = get_wifi_networks()
#                 ssid_to_remove = networks['connected_ssid']
#                 remove_network_config(ssid_to_remove, config_file)

#                 # Re-enable wlan0 if needed
#                 subprocess.run(['sudo', 'ip', 'link', 'set', 'wlan0', 'up'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
#                 return jsonify({"status": "200", "message": "Disconnected and auto-reconnection prevented."})
#             else:
#                 error_message = disconnect_result.stderr.decode('utf-8').strip()
#                 return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})

#     except Exception as e:
#         return jsonify({"status": "500", "message": f"An unexpected error occurred: {str(e)}"})

# def remove_network_config(ssid, config_file):
#     print('{ssid} want to remove profile')
#     try:
#         with open(config_file, 'r') as file:
#             lines = file.readlines()

#         # Prepare the updated content, excluding the SSID block
#         updated_lines = []
#         skip = False
#         for line in lines:
#             if f'ssid="{ssid}"' in line:
#                 skip = True
#             elif '}' in line and skip:
#                 skip = False
#                 continue  # Skip the closing brace
#             if not skip:
#                 updated_lines.append(line)

#         # Join updated lines into a string
#         updated_config = ''.join(updated_lines)

#         # Use subprocess with 'sudo' to write the updated content to the config file
#         process = subprocess.Popen(['sudo', 'tee', config_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         stdout, stderr = process.communicate(input=updated_config.encode('utf-8'))

#         if process.returncode != 0:
#             print(f"Failed to modify {config_file}: {stderr.decode('utf-8')}")
#         else:
#             print(f"{ssid} network configuration removed successfully.")

#     except Exception as e:
#         print(f"Failed to modify {config_file}: {str(e)}")
    
# def clean_pumps(pump_group, status):
#     for pump_number in pump_group:
#         status['status']['active'] = 0
#         status['status']['progress'] = 0
#         status['control']['start'] = 0
#         status['control']['pause'] = 0
#         status['control']['stop'] = 0
#         status['control']['clean'] = pump_number
#         status['control']['drink_name'] = 'empty'
#         WriteStatus(status)


# @app.route('/inventory/<action>', methods=['POST', 'GET'])
# @app.route('/inventory/pump/<action>', methods=['POST', 'GET'])
# @app.route('/inventory', methods=['POST', 'GET'])
# def inventory(action=None):
#     settings = ReadSettings()   
#     drink_db = ReadDrinkDB()
#     status = ReadStatus()
#     moniterDB = MoniterDB()
#     available_GPIOs = [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
#     errorcode = 0
#     errormessage = []

#     if request.method == 'POST' and action == 'settings':
#         response = request.form
#         for pump_number, pin_number in settings['assignments'].items():
#             index = 'inv_' + pump_number
#             if index in response:
#                 settings['inventory'][pump_number] = response[index]

#         for pump_number, inv_name in settings['inventory'].items():
#             index = 'ass_' + pump_number
#             if index in response:
#                 settings['assignments'][pump_number] = int(response[index])

#         for pump_number in settings['quantity'].keys():
#             quantity_index = 'qty_' + pump_number 
#             if quantity_index in response:             
#                 settings['quantity'][pump_number] = int(response[quantity_index])
#                 settings['in_quantity'][pump_number] = int(response[quantity_index])
#                 moniterDB.ingridients(pump_number,int(response[quantity_index]),int(response[quantity_index]))

#         duplicated_pin = []
#         for pump_number, pin_number in settings['assignments'].items():
#             for pump_number_inside, pin_number_inside in settings['assignments'].items():
#                 if (pin_number != 0) and (pin_number == pin_number_inside) and (pump_number != pump_number_inside):
#                     errorcode = 1
#                     if pin_number not in duplicated_pin:
#                         duplicated_pin.append(pin_number)
#                         errormessage.append('Pin ' + str(pin_number) + ' is assigned to more than one pump. ')

#         used_drinks = {}
#         for pump_number, drink_name in settings['inventory'].items():
#             if drink_name == "Default":
#                 continue
#             elif drink_name in used_drinks:
#                 errorcode = 1
#                 errormessage.append(f'Drink "{drink_name}" is already assigned to pump {used_drinks[drink_name]} and cannot be assigned to pump {pump_number}.')
#             else:
#                 used_drinks[drink_name] = pump_number  

#         if 'flow_rate' in response:
#             settings['flowrate'] = int(response['flow_rate'])

#         if errorcode > 0:
#             settings = ReadSettings()
#             errormessage.append('Settings NOT saved. Please check your settings and try again. ')
#         else:
#             WriteSettings(settings)

#     if request.method == 'POST' and action == 'refill':
#         response = request.get_json()
#         pump_number_clean = response.get('pump_number')
#         action = response.get('action')
#         drink_name = 'clean'
        
#         metadata = ReadMetadata()

#         non_alcoholic_pumps = {
#             'pump_01', 'pump_02', 'pump_03',
#             'pump_04', 'pump_05', 'pump_06', 'pump_07'
#         }

#         if pump_number_clean in non_alcoholic_pumps:
#             metadata['machine']['non_alcoholic_last_refilled'][pump_number_clean] = datetime.datetime.now().isoformat()
#             WriteMetadata(metadata)
        
#         if (action == "cancel"):
#             status['control']['stop'] = 1 
#             WriteStatus(status)
#             return jsonify({'status': 'success', 'message': 'Pump re-fill deactivated'})

#         if (status['status']['active']==1):
#             return jsonify({'status': 'error', 'message': 'Another refill process is in progress. Please wait.'})

#         # Verify pump number and activate refill
#         for pump_numbers, pin_number in settings['assignments'].items():
#             if pump_numbers == pump_number_clean:
#                 status['status']['active'] = 0
#                 status['status']['progress'] = 0
#                 status['control']['start'] = 0
#                 status['control']['pause'] = 0
#                 status['control']['stop'] = 0
#                 status['control']['clean'] = pump_number_clean
#                 status['control']['drink_name'] = 'empty'
#                 WriteStatus(status)
                
#                 return jsonify({'status': 'success', 'message': f'{pump_number_clean} is re-fill activated. Please wait a minute.'})

#         return jsonify({'status': 'error', 'message': 'Pump not found'})

#     return render_template('inventory.html', show_navbar=False,  action=action,errorcode=errorcode, errormessage=errormessage, settings=settings, drink_db=drink_db, available_GPIOs=available_GPIOs)

# @app.route('/cleaning/pump/<action>', methods=['POST', 'GET'])
# @app.route('/cleaning',methods = ['POST','GET'])
# def cleaning(action=None):
#     settings = ReadSettings()   
#     drink_db = ReadDrinkDB()
#     status = ReadStatus()
#     available_GPIOs = [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
#     errorcode = 0
#     errormessage = []    
    
#     if request.method == 'POST' and action == 'clean':
#         response = request.form
#         clean_group = response.get('clean_group') 
#         drink_name = 'clean'
#         metadata = ReadMetadata() 
#         metadata['machine']['last_cleaned_at'] = datetime.datetime.now().isoformat()
#         WriteMetadata(metadata)
      
        
#         # Define pump two groups dynamically from settings.json
#         non_alcoholic_pumps = [pump for pump in settings['inventory'].keys() if pump in ['pump_01', 'pump_02', 'pump_03', 'pump_04', 'pump_05', 'pump_06', 'pump_07']]
#         alcoholic_pumps = [pump for pump in settings['inventory'].keys() if pump in ['pump_08', 'pump_09', 'pump_10', 'pump_11', 'pump_12', 'pump_13', 'pump_14', 'pump_15']]

#         if clean_group == 'all':
#             status['status']['active'] = 0
#             status['status']['progress'] = 0
#             status['control']['start'] = 0
#             status['control']['pause'] = 0
#             status['control']['stop'] = 0
#             status['control']['clean'] = "all"
#             status['control']['drink_name'] = 'empty'
#             WriteStatus(status)
#             return render_template('work.html', drink_name=drink_name, action="default", workmode='clean',clean_pump_group = 'all')

#         elif clean_group == 'non_alcoholic':
#             clean_pumps(non_alcoholic_pumps, status)
           
#             return render_template('work.html', drink_name=drink_name, action="default", workmode='clean', clean_pump_group='non alcoholic')

#         elif clean_group == 'alcoholic':
#             clean_pumps(alcoholic_pumps, status)
#             return render_template('work.html', drink_name=drink_name, action="default", workmode='clean', clean_pump_group='alcoholic')

#         else:
#             return "Error: Invalid selection", 400  
    
#     return render_template('cleaning.html',show_navbar = True, action=action, errorcode=errorcode, errormessage=errormessage, settings=settings, drink_db=drink_db,available_GPIOs=available_GPIOs)

# @app.route('/ir-sensor-detection',methods=["POST","GET"])
# def irSensorDetection():
#     try:
#         settings = ReadSettings()
#         errorcode = 0
#         errormessage = []
        
#         sensor = SensorSignal(settings) 
        
#         sensor_result = sensor.detectObject(settings)
        
#         return jsonify({"sensor_results":sensor_result,"detection":settings["ir_sensor"]["detection"]})
    
#     except Exception as e:
#         errorcode = 500
#         errormessage.append(str(e))
#         return jsonify({"errorcode":errorcode, "errormessage":errormessage})
        
        
# @app.route('/manifest')
# def manifest():
#     res = make_response(render_template('manifest.json'), 200)
#     res.headers["Content-Type"] = "text/cache-manifest"
#     return res


# if __name__ == '__main__':
#     app.run(host='0.0.0.0',  port=5000,
#         threaded=True,
#         use_reloader=False) 
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
        print(f"{request.form.getlist('makedrink')}, {response}")
        
        # Collect all possible drinks
        settings = ReadSettings()
        drink_list = []
        for d_name, d_details in drink_db['drinks'].items():
            matched = True
            for ing_name in d_details['ingredients']:
                if ing_name not in settings['inventory'].values():
                    matched = False
                    break
            if matched:
                drink_list.append(d_name)
                
        if not drink_list:
            return redirect('/')
        
        if (response['makedrink'] in drink_list):
            drink_name = response['makedrink']
            print(f"drink_name: {drink_name}")
            drink_info = drink_db['drinks'][drink_name]
            drinkDespenseImage = drink_info['image']['drinkDespenseImage']
            status['status']['active'] = 0
            status['status']['progress'] = 0
            status['status']['waiting'] = 0
            status['status']['active_pumps'] = []
            status['control']['start'] = 1
            status['control']['pause'] = 0
            status['control']['stop'] = 0
            status['control']['clean'] = ""
            status['control']['drink_name'] = drink_name
            status['control']['infinite_mode'] = 1
            status['control']['infinite_drinks'] = drink_list
            try:
                curr_idx = drink_list.index(drink_name)
                next_idx = (curr_idx + 1) % len(drink_list)
            except ValueError:
                next_idx = 0
            status['control']['infinite_index'] = next_idx
            WriteStatus(status)
            return render_template('work.html', drink_name=drink_name, action="default", workmode='dispense',drinkDespenseImage=drinkDespenseImage, infinite_mode=1)

    return redirect('/')
       
def CleanPump(pump_selected):
    print(f"The selected pump is {pump_selected} for cleaning")
    control_logger.info(f"The selected pump is {pump_selected} for cleaning")
    settings = ReadSettings()
    status = ReadStatus()
    status['status']['active'] = 1
    WriteStatus(status)

    # Initialize Platform Object
    platform = PumpControl(settings)

    if pump_selected == "all":
        total_runtime = 0
        progress = 0

        for pump_number, pin_number in settings['assignments'].items():
            if pin_number != 0:
                total_runtime += 20

        for pump_number, pin_number in settings['assignments'].items():

            if (pin_number != 0) and (status['control']['stop'] == 0):
                platform.ActivatePump(pump_number)
                for index in range(20):
                    status = ReadStatus()
                    if (status['control']['stop'] == 0):
                        progress += 1
                        status['status']['progress'] = int(100 * (progress / total_runtime))
                        WriteStatus(status)
                        time.sleep(1) # Run for X seconds
                    else:
                        break
                platform.DeActivatePump(pump_number)
    else:
        for pump_number, pin_number in settings['assignments'].items():
            if (pump_selected == pump_number):
                platform.ActivatePump(pump_number)
                for index in range(21):
                    status = ReadStatus()
                    if (status['control']['stop'] == 0):
                        status['status']['progress'] = index*5
                        WriteStatus(status)
                        time.sleep(1) # Run for X seconds
                    else:
                        break
                platform.DeActivatePump(pump_number)


    status['status']['active'] = 0
    status['control']['stop'] = 0
    status['control']['clean'] = ""
    WriteStatus(status)
