# # <!-- Main Body Container -->
# # <!-- <div class="container">
# #     <div class="container-message">
# #         <div id="success-message" class="hidden"></div>
# #         <div id="error-message" class="hidden"></div>
# #     </div>
    
# #     <div class="card-container">
# #         <h2>System Information</h2>
# #         <div class="sysinfo-group">
# #             <p class="system-name-info"  id="systemName">System Name: MySystem123 </p>
# #             <p class="system-key-info"  id="systemKey">System Key: ABC123XYZ </p>
# #         </div>
# #     </div>
# #     <div class="card-container">
# #         <h2>Connect your system </h2>
# #         <form id="wifiForm">
# #             <div class="input-group">
# #                 <label for="wifiNetworks">Select Available Wi-Fi Networks:</label>
# #                 <select id="wifiNetworks" name="ssid">
# #                     Connect wifi
# #                     {% for network in networks %}
# #                     <option value="{{ network }}">{{ network }}</option>
# #                     {% endfor %}
# #                 </select>
# #             </div>
# #             <div class="input-group">
# #                 <label for="wifiPassword">Enter Password:</label>
# #                 <input type="password" id="wifiPassword" name="password" placeholder="Enter Wi-Fi Password">
# #             </div>
# #             <button type="button" class="btn-connect" onclick="connectWifi()">Connect</button>
# #         </form>
    
# #     </div>
# #     <div id="message" class="message" style="display: none;"></div>

# # </div> -->
# # # def get_wifi_networks():
# # #     try:
# # #         # List available Wi-Fi networks using netsh command
# # #         result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # #         networks_output = result.stdout.decode('utf-8')
        
# # #         # Extract SSIDs using regex
# # #         ssid_list = re.findall(r'SSID \d+ : (.+)', networks_output)
# # #         return ssid_list
# # #     except Exception as e:
# # #         return str(e)

# # # def connect_to_wifi(ssid, password):
# # #     try:
# # #         # Command to connect to the Wi-Fi network using netsh
# # #         command = ['netsh', 'wlan', 'connect', f'name={ssid}', f'key={password}']
# # #         result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # #         if result.returncode == 0:
# # #             return {'response':"200","message":f"Connected to {ssid}"}
# # #         else:
# # #             return {"response":"200","message":f"Failed to connect to {ssid}: {result.stderr.decode('utf-8')}"}
# # #     except Exception as e:
# # #         return str(e)

# # # @app.route('/connect-via-wifi', methods=['GET', 'POST'])
# # # def connect_wifi():
# # #     if request.method == 'POST':
# # #         ssid = request.form['ssid']
# # #         password = request.form['password']
# # #         connection_status = connect_to_wifi(ssid, password)
# # #         return jsonify({'status': connection_status})
    
# # #     networks = get_wifi_networks()
# # #     return render_template('connect_wifi.html', networks=networks)


# // function connectWifi() {
# //     var formData = new FormData(document.getElementById('wifiForm'));

# //     fetch('/connect-via-wifi', {
# //         method: 'POST',
# //         body: formData
# //     })
# //     .then(response => response.json())
# //     .then(data => {
# //         var successMessageElement = document.getElementById('success-message');
# //         var errorMessageElement = document.getElementById('error-message');
# //         if (data.response.status == "200") {
# //             successMessageElement.classList.remove('hidden');
# //             successMessageElement.classList.add("show-message");
# //             successMessageElement.innerHTML = data.response.message;
# //         } else {
# //           errorMessageElement.classList.remove('hidden');
# //           errorMessageElement.classList.add("show-message");
# //           errorMessageElement.innerHTML = data.response.message;
# //         }
# //         setTimeout(function() {
# //           successMessageElement.classList.add('hidden');
# //           errorMessageElement.classList.add('hidden');
# //       }, 5000); 
# //     })
# //     .catch(error => {
# //        var errorMessageElement = document.getElementById('error-message');
# //         console.error('Error:', error);
# //         errorMessageElement.classList.remove('hidden');
# //         errorMessageElement.classList.add("show-message");
# //         errorMessageElement.innerHTML = error;
# //         setTimeout(function() {
# //           successMessageElement.classList.add('hidden');
# //           errorMessageElement.classList.add('hidden');
# //       }, 5000); 
# //     });

# // }

#   <!-- Admin Functions Card -->
# 			<div class="card">
# 				<div class="card-header">
# 							Administrative Functions
# 				</div>
# 				<div class="card-body">
# 						<form name="input" action="/admin/reboot">
# 							<button type="button" class="btn btn-warning btn-block" data-toggle="modal" data-target="#rebootModal">
# 								Reboot System
# 							</button>

# 							<!-- Reboot Modal -->
# 							<div class="modal fade" id="rebootModal" tabindex="-1" role="dialog" aria-labelledby="rebootModalLabel" aria-hidden="true">
# 								<div class="modal-dialog" role="document">
# 									<div class="modal-content">
# 										<div class="modal-header">
# 											<h5 class="modal-title" id="rebootModalLabel">Reboot</h5>
# 											<button type="button" class="close" data-dismiss="modal" aria-label="Close">
# 												<span aria-hidden="true">&times;</span>
# 											</button>
# 										</div>
# 										<div class="modal-body">
# 											<p>Are you sure you would like to reboot the system?
# 											<br><i>Any unsaved data may be lost.</i></p>
# 										</div>
# 										<div class="modal-footer">
# 											<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
# 											<button type="submit" class="btn btn-primary" name="reboot" value="True">Confirm</button>
# 										</div>
# 									</div>
# 								</div>
# 							</div>

# 						</form>

# 						<br>
# 						<!-- Shutdown -->
# 						<form name="input" action="/admin/shutdown">
# 							<!-- Button trigger modal -->
# 							<button type="button" class="btn btn-danger btn-block" data-toggle="modal" data-target="#shutdownModal">
# 								Shutdown System
# 							</button>

# 							<!-- Shutdown Modal -->
# 							<div class="modal fade" id="shutdownModal" tabindex="-1" role="dialog" aria-labelledby="shutdownModalLabel" aria-hidden="true">
# 								<div class="modal-dialog" role="document">
# 									<div class="modal-content">
# 										<div class="modal-header">
# 											<h5 class="modal-title" id="shutdownModalLabel">Shutdown</h5>
# 											<button type="button" class="close" data-dismiss="modal" aria-label="Close">
# 												<span aria-hidden="true">&times;</span>
# 											</button>
# 										</div>
# 										<div class="modal-body">
# 											<p>Are you sure you would like to shutdown the system?
# 											<br><i>Any unsaved data may be lost.  System must be manually started after a shutdown.</i></p>
# 										</div>
# 										<div class="modal-footer">
# 											<button type="button" class="btn btn-secondary" data-dismiss="modal">Cancel</button>
# 											<button type="submit" class="btn btn-primary" name="shutdown" value="True">Confirm</button>
# 										</div>
# 									</div>
# 								</div>
# 							</div>
# 						</form>

# 					</div>
# 				</div>
# 			<br>
			
# <!--     
# 			<div class="card">
# 				<div class="card-header">
# 							System Info
# 				</div>
# 	      <div class="card-body">
# 					<b>CPU Info</b><br>
# 	        {% for line in cpuinfo %}
# 	          {{ line }}<br>
# 	        {% endfor %}
# 					<br>
# 					<p><b>CPU Temperature:</b> {{ temp }}</p>
# 					<br>
# 					<b>Network Info</b><br>
# 					{% for lines in ifconfig %}
# 						{{ lines }}<br>
# 					{% endfor %}
# 	      </div>
# 			</div>
# 			<br>

# 			<div class="card">
# 				<div class="card-header">
# 							Uptime
# 				</div>
# 	      <div class="card-body">
# 					{{ uptime }}
# 				</div>
# 	    </div> -->
# 			<!-- <br>

# 				<div class="card">
# 					<div class="card-header">
# 					</div>

#           <div class="card card-body">
#           </div>
# 				</div>
# 					<br><br><br>

# 				<div class="container">
# 				</div> -->


	# <!-- Pump Settings Card -->
	# <form name="input" action="/admin/settings" method="POST">
	# 	<div class="card">
	# 		<div class="card-header">
	# 					Pump Settings
	# 		</div>
	# 		<div class="card-body">
		
	# 	<span class="badge badge-warning">INFO:</span><i class="small"> Adjust the average flow rate of the pumps where the value 'n' input below will be used to adjust the flow through the following calculation (n/100) * (ml) of liquid to dispense.</i>
	# 	<div class="input-group mb-3">
	# 		<div class="input-group-prepend">
	# 			<span class="input-group-text" data-toggle="tooltip" title="Flow Rate: Adjust flow rate for the pumps installed. [Value = 1-100]"><i class="fas fa-wind"></i>&nbsp; Flow Rate[x/100]:</span>
	# 		</div>
	# 		<input id="flow_rate" type="number" min="1" max = "100" class="form-control" name="flow_rate" value="{{ settings['flowrate'] }}">
	# 	</div>

	# 	<button type="submit" class="btn btn-primary btn-sm">Save Settings</button>
	# </div>
	# </div>
	# </form>
	# <br>

# <form name="input" action="/admin/settings" method="POST">
# 		<div class="card">
# 			<div class="card-header">
# 				Inventory
# 			</div>
# 			<div class="card-body">
# 				<table class="table">
# 					<thead>
# 						<tr>
# 							<th>Pump</th>
# 							<th>GPIO Assignment</th>
# 							<th>Drink Ingredient</th>
# 						</tr>
# 					</thead>
# 					<tbody>
# 						{% for pump_number, pin_number in settings['assignments'].items()|sort %}
# 						<tr>
# 							<td>{{ pump_number }}</td>
# 							<td>
# 								<div class="form-group">
# 									<select class="form-control" id="ass_{{ pump_number }}"
# 										name="ass_{{ pump_number }}">
# 										{% for pin_index in available_GPIOs|sort %}
# 										{% if (pin_index == pin_number) and (pin_index == 0) %}
# 										<option selected value="{{ pin_index }}">Un-Assigned</option>
# 										{% elif (pin_index == pin_number) %}
# 										<option selected value="{{ pin_index }}">{{ pin_index }}</option>
# 										{% elif (pin_index == 0) %}
# 										<option value="{{ pin_index }}">Un-Assigned</option>
# 										{% else %}
# 										<option value="{{ pin_index }}">{{ pin_index }}</option>
# 										{% endif %}
# 										{% endfor %}
# 									</select>
# 								</div>
# 							</td>
# 							<td>
# 								<div class="form-group">
# 									<select class="form-control" id="inv_{{ pump_number }}"
# 										name="inv_{{ pump_number }}">
# 										{% for ingredient_index, ingredient_name in drink_db['ingredients'].items()|sort
# 										%}
# 										{% if ingredient_index == settings['inventory'][pump_number] %}
# 										<option selected value="{{ ingredient_index }}">{{ ingredient_name }}</option>
# 										{% else %}
# 										<option value="{{ ingredient_index }}">{{ ingredient_name }}</option>
# 										{% endif %}
# 										{% endfor %}
# 									</select>
# 								</div>

# 							</td>
# 						</tr>
# 						{% endfor %}
# 					</tbody>
# 				</table>
# 				<button type="submit" class="btn btn-success btn-sm">Save Settings</button>
# 			</div>
# 		</div>
# 	</form>
# 	<br>

# <!-- <table class="table">
# 					<thead>
# 						<tr>
# 							<th>Pump</th>
# 							<th>Drink Ingredient</th>
# 							<th>Quantity</th>
# 							<th>Action</th>
# 							<th>Status</th>
# 						</tr>
# 					</thead>
# 					<tbody>
# 						{% for pump_number, pin_number in settings['assignments'].items()|sort %}
# 						<tr>
# 							<td>{{ pump_number }}</td>
							
# 							<td>
# 								<div class="form-group">
# 									<select class="form-control" id="inv_{{ pump_number }}"
# 										name="inv_{{ pump_number }}">
# 										{% for ingredient_index, ingredient_name in drink_db['ingredients'].items()|sort
# 										%}
# 										{% if ingredient_index == settings['inventory'][pump_number] %}
# 										<option selected value="{{ ingredient_index }}">{{ ingredient_name }}</option>
# 										{% else %}
# 										<option value="{{ ingredient_index }}">{{ ingredient_name }}</option>
# 										{% endif %}
# 										{% endfor %}
# 									</select>
# 								</div>

# 							</td>
# 						</tr>
# 						{% endfor %}
# 					</tbody>
# 				</table> -->

				# <!-- <table class="table">
				# 	<thead>
				# 		<tr>
				# 			<th>Pump</th>
				# 			<th>Drink Ingredient</th>
				# 			<th>Quantity</th>
				# 			<th>Action</th>
				# 			<th>Status</th>
				# 		</tr>
				# 	</thead>
				# 	<tbody>
				# 		{% for pump_number, pin_number in settings['assignments'].items()|sort %}
				# 		<tr>
				# 			<td>{{ pump_number }}</td>
				
				# 			<td>
				# 				<div class="form-group">
				# 					<select class="form-control" id="inv_{{ pump_number }}" name="inv_{{ pump_number }}">
				# 						{% for ingredient_index, ingredient_name in drink_db['ingredients'].items()|sort %}
				# 						{% if ingredient_index == settings['inventory'][pump_number] %}
				# 						<option selected value="{{ ingredient_index }}">{{ ingredient_name }}</option>
				# 						{% else %}
				# 						<option value="{{ ingredient_index }}">{{ ingredient_name }}</option>
				# 						{% endif %}
				# 						{% endfor %}
				# 					</select>
				# 				</div>
				# 			</td>
				
				# 			<td>
				# 				<p type="number" class="form-control" id="qty_{{ pump_number }}" name="qty_{{ pump_number }}" min="1" step="0.1" placeholder="Enter quantity">
				# 			</td>
				
				# 			<td>
				# 				<button class="btn-start-action btn-success" id="start_{{ pump_number }}" title="Start">
				# 					<i class="fas fa-play"></i>
				# 				</button>
				# 				<button class="btn btn-danger" id="stop_{{ pump_number }}" title="Stop">
				# 					<i class="fas fa-stop"></i>
				# 				</button>
				# 			</td>
				
				# 			<td>
				# 				<div class="progress">
				# 					<div class="progress-bar" id="progress_{{ pump_number }}" role="progressbar" style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">0%</div>
				# 				</div>
				# 			</td>
				# 		</tr>
				# 		{% endfor %}
				# 	</tbody>
				# </table> -->

				# <!-- <table class="table">
				# 	<thead>
				# 		<tr>
				# 			<th>Pump</th>
				# 			<th>Drink Ingredient</th>
				# 			<th>Quantity</th>
				# 			<th>Action</th>
				# 			<th>Status</th>
				# 		</tr>
				# 	</thead>
				# 	<tbody>
				# 		{% for pump_number, pin_number in settings['assignments'].items()|sort %}
				# 		<tr>
				# 			<td>{{ pump_number }}</td>
				
				# 			<td>
				# 				<div class="form-group">
				# 					<select class="form-control" id="inv_{{ pump_number }}" name="inv_{{ pump_number }}">
				# 						{% for ingredient_index, ingredient_name in drink_db['ingredients'].items()|sort %}
				# 						{% if ingredient_index == settings['inventory'][pump_number] %}
				# 						<option selected value="{{ ingredient_index }}">{{ ingredient_name }}</option>
				# 						{% else %}
				# 						<option value="{{ ingredient_index }}">{{ ingredient_name }}</option>
				# 						{% endif %}
				# 						{% endfor %}
				# 					</select>
				# 				</div>
				# 			</td>
				
				# 			<td>
				# 				<p type="number" class="form-control" id="qty_{{ pump_number }}" name="qty_{{ pump_number }}" min="1" step="0.1" placeholder="Enter quantity">
				# 			</td>
				
				# 			<td>
				# 				<button class="btn-start-action btn-green" id="start_{{ pump_number }}" title="Start" onclick="toggleAction('{{ pump_number }}')">
				# 					<i class="fas fa-play"></i>
				# 				</button>
				# 				<button class="btn-stop-action btn-danger" id="stop_{{ pump_number }}" title="Stop" style="display:none;" onclick="toggleAction('{{ pump_number }}')">
				# 					<i class="fas fa-stop"></i>
				# 				</button>
				# 			</td>
				
				# 			<td>
				# 				<div class="progress">
				# 					<div class="progress-bar" id="progress_{{ pump_number }}" role="progressbar" style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">0%</div>
				# 				</div>
				# 			</td>
				# 		</tr>
				# 		{% endfor %}
				# 	</tbody>
				# </table> -->

#   <!-- <div id="CleanStatus" class="progress-bar progress-bar-striped progress-bar-animated" style="width: 0%"> <b>0 %</b> </div>
# 					  </div> -->

#wifi connection code 

# #wifi connection code 
# def get_wifi_networks():
#     try:
#         result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         networks_output = result.stdout.decode('utf-8')
        
#         # Extract SSIDs using regex
#         ssid_list = re.findall(r'SSID \d+ : (.+)', networks_output)
#         return ssid_list
#     except Exception as e:
#         return []
    
# def connect_to_wifi(ssid, password):
#     try:
#         command = ['netsh', 'wlan', 'connect', f'name={ssid}', f'key={password}']
#         print("The command",command)
#         result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         print("The result",result)
#         print("The result code",result.returncode)
#         print("check",result.returncode == 0)
#         if result.returncode == 0:
#             return {'status':"200","message":f"Connected to {ssid}"}
#         else:
#             return {"message": f"Failed to connect to {ssid}"}
#     except Exception as e:
#         return str(e)

# @app.route('/connect-via-wifi', methods=['GET', 'POST'])
# def connect_wifi():
#     if request.method == 'POST':
#         ssid = request.form['ssid']
#         password = request.form['password']
#         print(f"The password of wifi for {ssid}",password)
#         connection_status = connect_to_wifi(ssid, password)
#         print("The status of {ssid} is",connection_status)
#         return jsonify({'response': connection_status})
    
#     networks = get_wifi_networks()
#     return render_template('connect_wifi.html', networks=networks)
# def sanitize_ssid(ssid):
#     leading_ssid = re.sub(r'[^A-Za-z0-9]', '', ssid)
#     leading_ssid = leading_ssid.strip()
#     return leading_ssid

# import subprocess
# import os


# // function connectWifi() {
# //   var formData = new FormData(document.getElementById('wifiForm'));
# //       console.log(formData);
      
# //   fetch('/connect-via-wifi', {
# //       method: 'POST',
# //       body: formData
# //   })
# //   .then(response => response.json())
# //   .then(data => {
# //       var successMessageElement = document.getElementById('success-message');
# //       var errorMessageElement = document.getElementById('error-message');

# //       if (data.response.status === "200") {
# //           successMessageElement.classList.remove('hidden');
# //           successMessageElement.classList.add("show-message");
# //           successMessageElement.innerHTML = data.response.message;
# //           setTimeout(function() {
# //             successMessageElement.classList.add('hidden');
# //             successMessageElement.classList.remove("show-message");
# //         }, 5000);
# //         location.reload();
# //       } else {
# //           errorMessageElement.classList.remove('hidden');
# //           errorMessageElement.classList.add("show-message");
# //           errorMessageElement.innerHTML = data.response.message;
# //           setTimeout(function() {
# //             errorMessageElement.classList.add('hidden');
# //             errorMessageElement.classList.remove("show-message");
# //         }, 5000);
# //       }

    
# //   })
# //   .catch(error => {
# //       var errorMessageElement = document.getElementById('error-message');
# //       console.error('Error:', error);
# //       errorMessageElement.classList.remove('hidden');
# //       errorMessageElement.classList.add("show-message");
# //       errorMessageElement.innerHTML = 'An error occurred. Please try again.';

# //       setTimeout(function() {
# //         successMessageElement.classList.add('hidden');
# //         errorMessageElement.classList.add('hidden');
# //     }, 5000);  
# //   });
# // }

# <!-- <form id="wifiForm">
#             <div class="input-group">
#                 <label for="wifiNetworks">Select Available Wi-Fi Networks:</label>
#                 <select id="wifiNetworks" name="ssid" onchange="showPasswordField()">
#                     <option value="" disabled selected>Select Wi-Fi Network</option>
#                     {% for network in networks %}
#                     <option value="{{ network }}">{{ network }}</option>
#                     {% endfor %}
#                 </select>
#             </div>
#             <div class="input-group" id="passwordGroup" style="display: none;">
#                 <label for="wifiPassword">Enter Password:</label>
#                 <input type="password" id="wifiPassword" name="password" placeholder="Enter Wi-Fi Password" required
#                     autocomplete="new-password">
#             </div>


#             <button type="button" id="connectButton" class="btn-connect" style="display: none;"
#                 onclick="connectWifi()">Connect</button>
#         </form> -->

#admin code 
# @app.route('/admin/pump_clean/', methods=['POST'])
# def pump_clean(action=None):
#     settings = ReadSettings()
#     drink_db = ReadDrinkDB()
#     status = ReadStatus()

#     if request.method == 'POST':
#         data  = request.get_json()
#         pump_number = data.get('pump_number')
#         action = data.get('action')
#         drink_name = 'clean'
        
#         print("Received form data:", pump_number, action)

#         if action == 'clean':
#             status['status']['active'] = 0
#             # status['status']['progress'] = 0
#             # status['control']['start'] = 0
#             # status['control']['pause'] = 0
#             # status['control']['stop'] = 0
#             # status['control']['clean'] = pump_number
#             # status['control']['drink_name'] = 'empty'
#             # WriteStatus(status)
            

#             # # return jsonify({'status': 'success', 'message': f'Pump {pump_number} cleaned successfully'})
#             # return render_template('work.html', drink_name=drink_name, action="default", workmode='clean',clean_pump_group = pump_number)
#             #print('Clean ALL pumps for 20 seconds.')
#             status['status']['active'] = 0
#             status['status']['progress'] = 0
#             status['control']['start'] = 0
#             status['control']['pause'] = 0
#             status['control']['stop'] = 0
#             status['control']['clean'] = pump_number
#             status['control']['drink_name'] = 'empty'
#             WriteStatus(status)
#             return render_template('work.html', drink_name=drink_name, action="default", workmode='clean')
#         else:
#             return jsonify({'status': 'error', 'message': 'Invalid action'}), 400

#     return render_template('admin.html', action=action, settings=settings, drink_db=drink_db)

# @app.route('/admin/pump_clean/', methods=['POST'])

# // function cleanPumpAction(pumpNumber) {
# //     event.preventDefault()
# //     const startButton = document.getElementById(`start_${pumpNumber}`);
# //     const stopButton = document.getElementById(`stop_${pumpNumber}`);
# //     console.log("The selected pump by action",pumpNumber);
    
# //     

# //     // Send AJAX request to the backend
# //     fetch('/admin/clean', {
# //         method: 'POST',
# //         headers: {
# //             'Content-Type': 'application/json',
# //         },
# //         body: JSON.stringify({
# //             pump_number: pumpNumber,
# //             action: 'clean'
# //         })
# //     }).then(response => response.json())
# //       .then(data => {
# //           console.log('Pump action response:', data);
# //           // Handle the response here
# //       })
# // }
  #print('Clean Requested.')
        #print(response['clean'])
            #print('Clean ALL pumps for 20 seconds.')
        # status['status']['active'] = 0
        # status['status']['progress'] = 0
        # status['control']['start'] = 0
        # status['control']['pause'] = 0
        # status['control']['stop'] = 0
        # status['control']['clean'] = pump_number
        # status['control']['drink_name'] = 'empty'
        # WriteStatus(status)
        # return render_template('work.html', drink_name=drink_name, action="default", workmode='clean')
        
        
# // function cleanPumpAction(pumpNumber) {
# //     event.preventDefault();
# //     const startButton = document.getElementById(`start_${pumpNumber}`);
# //     const stopButton = document.getElementById(`stop_${pumpNumber}`);
# //     console.log("The selected pump by action", pumpNumber);

# //     const data = {
# //         pump_number: pumpNumber,
# //         action: 'clean'
# //     };
# //     console.log(JSON.stringify(data));
    
# //     // Send AJAX request to the backend
# //     fetch('/admin/pump_clean', {
# //         method: 'POST',
# //         headers: {
# //             'Content-Type': 'application/json',
# //         },
# //         body: JSON.stringify(data) 
# //     }).then(response => response.json())
# //       .then(data => {
# //           console.log('Pump action response:', data);
# //           if (action === 'start') {
# //         startButton.style.display = 'none';
# //         stopButton.style.display = 'inline-block';
# //     } else {
# //         startButton.style.display = 'inline-block';
# //         stopButton.style.display = 'none';
# //     }
# //       })
# //       .catch(error => console.error('Error:', error));
# // }

# <form name="input" action="/admin/clean" method="POST">
# 		<div class="card">
# 			<div class="card-header">
# 				Cleaning
# 			</div>
# 			<div class="card-body">
# 				<p class="pump-clean-card"> Select the group of pump to clean, then touch Start Cleaning. As per
# 					selected group of pumps will turn on to flush the existing liquid from the tubes. It is recommended
# 					to take the tubes out of the water source halfway through to remove all liquid from the pumps.
# 					Important: make sure you have a glass under the funnel to catch the flushed out liquid.</p>
# 				<div class="form-group">
# 					<select class="form-control" id="clean" name="clean">
# 						<!-- <option selected value="pump_42">Clean ALL</option>
# 						{% for pump_number, pin_number in settings['assignments'].items()|sort %}
# 						<option value="{{ pump_number }}">{{ pump_number }}</option>
# 						{% endfor %} -->
# 						<option selected value="all">Clean ALL</option>
# 						<option value="non_alcoholic">Clean Non-Alcoholic Pumps (1-7)</option>
# 						<option value="alcoholic">Clean Alcoholic Pumps (8-15)</option>
# 					</select>
# 				</div>

# 				<button type="submit" class="btn btn-success btn-sm">Start Cleaning</button>
# 			</div>
# 		</div>
# 	</form>
# 	<br>
# <!-- Inventory Card -->
# 	<form name="input" action="/admin/settings" method="POST">
# 		<div class="card">
# 			<div class="card-header">
# 				Inventory
# 			</div>
# 			<div class="card-body">
# 				<table class="table">
# 					<thead>
# 						<tr>
# 							<th>Pump</th>
# 							<th style="width:40%">Drink Ingredient</th>
# 							<th style="width: 14%;">Quantity(in ml)</th>
# 							<th style="width: 10%; text-align:center">Action</th>
# 							<th>Status</th>
# 						</tr>
# 					</thead>
# 					<tbody>
# 						{% for pump_number, pin_number in settings['assignments'].items()|sort %}
# 						<tr>
# 							<td>{{ pump_number }}</td>

# 							<td>
# 								<div>
# 									<select class="form-control" id="inv_{{ pump_number }}"
# 										name="inv_{{ pump_number }}">
# 										{% for ingredient_index, ingredient_name in drink_db['ingredients'].items()|sort
# 										%}
# 										{% if ingredient_index == settings['inventory'][pump_number] %}
# 										<option selected value="{{ ingredient_index }}">{{ ingredient_name }}</option>
# 										{% else %}
# 										<option value="{{ ingredient_index }}">{{ ingredient_name }}</option>
# 										{% endif %}
# 										{% endfor %}
# 									</select>
# 								</div>
# 							</td>
# 							<td>
# 								<input type="number" class="form-control form-control-quantity"
# 									id="qty_{{ pump_number }}" name="qty_{{ pump_number }}" min="0" max="100" step="0.1"
# 									value="{{ settings['quantity'][pump_number] }}"
# 									oninput="updateProgress('{{ pump_number }}')" readonly>
# 							</td>
# 							<td style="text-align: center;">
# 								<button class="btn-start-action btn-green" id="start_{{ pump_number }}" title="Start"
# 									onclick="cleanPumpAction('{{ pump_number }}')">
# 									<i class="fas fa-play"></i>
# 								</button>
# 								<button class="btn-stop-action btn-danger" id="stop_{{ pump_number }}" title="Stop"
# 									style="display:none;" onclick="cancelPumpAction('{{ pump_number }}')">
# 									<i class="fa fa-pause"></i>
# 								</button>
# 							</td>
# 							<td>
# 								<div class="progress">
# 									<div class="progress-bar" id="progress_{{ pump_number }}" role="progressbar"
# 										style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">0%
# 									</div>
# 								</div>
# 							</td>
# 						</tr>
# 						{% endfor %}
# 					</tbody>
# 				</table>
# 				<button type="submit" class="btn btn-success btn-sm">Save Settings</button>
# 			</div>
# 		</div>
# 	</form>

# <!-- <form id="wifiForm">
#             <div class="input-group">
#                 <label for="wifiNetworks">Select Available Wi-Fi Networks:</label>
#                 <select id="wifiNetworks" name="ssid" onchange="showPasswordField()">
#                     <option value="" disabled selected>Select Wi-Fi Network</option>
#                     {% for network in networks.available_networks %}
#                     <option value="{{ network }}">{{ network }}</option>
#                     {% endfor %}
#                 </select>
#             </div>
#             <div class="input-group" id="passwordGroup" style="display: none;">
#                 <label for="wifiPassword">Enter Password:</label>
#                 <input type="password" id="wifiPassword" name="password" placeholder="Enter Wi-Fi Password" required
#                     autocomplete="new-password">
#             </div>
#             <button type="button" id="connectButton" class="btn-connect" style="display: none;"
#                 onclick="connectWifi()">Connect</button>
#         </form> -->

# // function updateProgress(pumpNumber) {
# //     const quantityInput = document.getElementById(`qty_${pumpNumber}`);
# //     const progressBar = document.getElementById(`progress_${pumpNumber}`);

# //     if (!quantityInput || !progressBar) return;

# //     const quantity = parseFloat(quantityInput.value);
# //     let percentage = (quantity / 100) * 100;
# //     let color;

# //     if (percentage <= 20) {
# //         color = 'red';
# //     } else if (percentage > 20 && percentage <= 50) {
# //         color = 'orange';
# //     } else {
# //         color = 'green';
# //     }

# //     progressBar.style.width = `${percentage}%`;
# //     progressBar.style.backgroundColor = color;
# //     progressBar.innerText = `${Math.round(percentage)}%`;
# // }

# // document.addEventListener('DOMContentLoaded', () => {
# //     const quantityDataScript = document.getElementById('quantity-data');
# //     const quantityData = JSON.parse(quantityDataScript.textContent);


# //     for (const [pumpNumber, valueOfPump] of Object.entries(quantityData)) {
# //         const inputElement = document.getElementById(`qty_${pumpNumber}`);
# //         if (inputElement) {
# //             inputElement.value = valueOfPump;
# //             updateProgress(pumpNumber);
# //         }
# //     }
# // });
# // function updateProgress(pumpNumber, percentage) {
# //     const progressBar = document.getElementById(`progress_${pumpNumber}`);

# //     if (progressBar) {
# //         progressBar.style.width = `${percentage}%`;

# //         if (percentage <= 20) {
# //             progressBar.style.backgroundColor = 'red';
# //         } else if (percentage > 20 && percentage <= 50) {
# //             progressBar.style.backgroundColor = 'orange';
# //         } else {
# //             progressBar.style.backgroundColor = 'green';
# //         }

# //         progressBar.innerText = `${Math.round(percentage)}%`;
# //         progressBar.setAttribute('aria-valuenow', Math.round(percentage));
# //     }
# // }

# // function fetchAndUpdateSettings() {
# //     fetch('/get_settings')
# //         .then(response => response.json())
# //         .then(data => {
# //             console.log(data);
            
# //             for (const [pumpNumber, quantity] of Object.entries(data['quantity'])) {
# //                 const currentQuantity = parseFloat(document.getElementById(`qty_${pumpNumber}`).value);
# //                 const percentage = (quantity / currentQuantity) * 100;
# //                 updateProgress(pumpNumber, percentage);
# //             }
# //         });
# // }

# // document.addEventListener('DOMContentLoaded', () => {
# //     fetchAndUpdateSettings();
# //     setInterval(fetchAndUpdateSettings, 5000); // Poll every 5 seconds
# // });


# // function fetchAndUpdateSettings() {
# //     fetch('/get_settings')
# //         .then(response => response.json())
# //         .then(data => {
# //             for (const [pumpNumber, quantity] of Object.entries(data['quantity'])) {
# //                 const progress = data['quantity'][pumpNumber] / 100 * 100;
# //                 updateProgress(pumpNumber, quantity, progress);
# //             }
# //         });
# // }

# // document.addEventListener('DOMContentLoaded', () => {
# //     fetchAndUpdateSettings();
# //     setInterval(fetchAndUpdateSettings, 5000); // Poll every 5 seconds
# // });
# <!-- <tbody>
# 						{% for pump_number, pin_number in settings['assignments'].items()|sort %}
# 						<tr>
# 							<td>{{ pump_number }}</td>

# 							<td>
# 								<div>
# 									<select class="form-control" id="inv_{{ pump_number }}"
# 										name="inv_{{ pump_number }}">
# 										{% for ingredient_index, ingredient_name in drink_db['ingredients'].items()|sort
# 										%}
# 										{% if ingredient_index == settings['inventory'][pump_number] %}
# 										<option selected value="{{ ingredient_index }}">{{ ingredient_name }}</option>
# 										{% else %}
# 										<option value="{{ ingredient_index }}">{{ ingredient_name }}</option>
# 										{% endif %}
# 										{% endfor %}
# 									</select>
# 								</div>
# 							</td>
# 							<td>
# 								<input type="number" class="form-control form-control-quantity"
# 									id="qty_{{ pump_number }}" name="qty_{{ pump_number }}" min="0" max="100" step="0.1"
# 									value="{{ settings['quantity'][pump_number] }}"
# 									oninput="updateProgress('{{ pump_number }}')" readonly>
# 							</td>
# 							<td style="text-align: center;">
# 								<button class="btn-start-action btn-green" id="start_{{ pump_number }}" title="Start"
# 									onclick="cleanPumpAction('{{ pump_number }}')">
# 									<i class="fas fa-play"></i>
# 								</button>
# 								<button class="btn-stop-action btn-danger" id="stop_{{ pump_number }}" title="Stop"
# 									style="display:none;" onclick="cancelPumpAction('{{ pump_number }}')">
# 									<i class="fa fa-pause"></i>
# 								</button>
# 							</td>
# 							<td>
# 								<div class="progress">
# 									<div class="progress-bar" id="progress_{{ pump_number }}" role="progressbar"
# 										 style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">0%
# 									</div>
# 								</div>
# 							</td>
# 						</tr>
# 						{% endfor %}
# 					</tbody> -->

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
# //             var successMessageElement = document.getElementById('success-message');
# //             var errorMessageElement = document.getElementById('error-message');
# //             if (data.status === 'success') {

# //                 successMessageElement.classList.remove('hidden');
# //                 successMessageElement.classList.add("show-message");
# //                 successMessageElement.innerHTML = data.message;
# //                 startButton.style.display = 'none';
# //                 stopButton.style.display = 'inline-block';

# //                 setTimeout(function () {
# //                     successMessageElement.classList.add('hidden');
# //                     successMessageElement.classList.remove("show-message");
# //                 }, 5000);
# //             } else {
# //                 errorMessageElement.classList.remove('hidden');
# //                 errorMessageElement.classList.add("show-message");
# //                 errorMessageElement.innerHTML = data.message;
# //                 setTimeout(function () {
# //                     errorMessageElement.classList.add('hidden');
# //                     errorMessageElement.classList.remove("show-message");
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
# //             var errorMessageElement = document.getElementById('error-message');
# //             if (data.status === 'success') {
# //                 startButton.style.display = 'inline-block';
# //                 stopButton.style.display = 'none';
# //                 errorMessageElement.classList.remove('hidden');
# //                 errorMessageElement.classList.add("show-message");
# //                 errorMessageElement.innerHTML = data.message;
# //                 setTimeout(function () {
# //                     errorMessageElement.classList.add('hidden');
# //                     errorMessageElement.classList.remove("show-message");
# //                 }, 5000);
# //             }
# //         })
# //         .catch(error => console.error('Error:', error));
# // }

# @app.route('/get_settings', methods=['GET'])
# def get_settings():
#     with open('settings.json', 'r') as f:
#         settings = json.load(f)
#     return jsonify(settings)
# def connect_to_wifi(ssid):
#     ssid = sanitize_ssid(ssid)
#     command = ['netsh', 'wlan', 'connect', f'name={ssid}']
#     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     if result.returncode == 0:
#         return {'status': "200", "message": f"Connected to {ssid}"}
#     else:
#         error_message = result.stderr.decode('utf-8')
#         return {"status": "500", "message": f"Failed to connect to {ssid}. Error: {error_message}"}
    
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

#         result = subprocess.run(['netsh', 'wlan', 'add', 'profile', f'filename={profile_filename}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         os.remove(profile_filename)

        
#         if result.returncode != 0:
#             return {"status": "500", "message": f"Failed to connect {ssid}"}
        
#         connect_result = subprocess.run(['netsh', 'wlan', 'connect', 'name=' + ssid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#         if connect_result.returncode != 0:
#             connect_error_message = connect_result.stderr.decode('utf-8')
#             return {"status": "500", "message": f"Failed to connect to {ssid}. Error: {connect_error_message}"}
#         else:
#             return {"status": "200", "message": f"Profile {ssid} added and connected successfully."}
    
#     except Exception as e:
#         return {"status": "500", "message": f"An unexpected error occurred: {str(e)}"}

    # <!-- <div class="card-container">
    #     <h2>Wifi Network Setting</h2>
        
    #     <form id="wifiForm">
    #         <div class="input-group">
    #             <label for="wifiNetworks">Select Available Wi-Fi Networks:</label>
    #             <select id="wifiNetworks" name="ssid" onchange="handleWifiSelection()">
    #                 <option value="" disabled selected>Select Wi-Fi Network</option>
    #                 {% for network in networks.available_networks %}
    #                 <option value="{{ network }}">{{ network }}</option>
    #                 {% endfor %}
    #             </select>
    #         </div>
    #         <div class="input-group" id="passwordGroup" style="display: none; position: relative;">
    #             <label for="wifiPassword">Enter Password:</label>
    #             <input type="password" id="wifiPassword" name="password" placeholder="Enter Wi-Fi Password" required autocomplete="new-password">
    #             <span id="togglePassword" style="position: absolute; right: 10px; top: 50%; transform: translateY(-50%); cursor: pointer;">
    #                 <i id="eyeIcon" class="fas fa-eye"></i>
    #             </span>
    #         </div>
    #         <button type="button" id="connectButton" class="btn-connect" style="display: none;" onclick="connectWifi()">Connect</button>
    #     </form> -->
    
#     // Function to fetch and update the list of available Wi-Fi networks
# // Function to fetch and update the list of available Wi-Fi networks
# // function refreshNetworks() {
# //   fetch('/get-available-networks')
# //       .then(response => response.json())
# //       .then(data => {
# //           const wifiNetworksSelect = document.getElementById('wifiNetworks');
# //           wifiNetworksSelect.innerHTML = '<option value="" disabled selected>Select Wi-Fi Network</option>'; // Reset options
# //           console.log(data);
          
# //           data.networks.forEach(network => {
# //               const option = document.createElement('option');
# //               option.value = network;
# //               option.textContent = network;
# //               wifiNetworksSelect.appendChild(option);
# //           });

# //           // Hide password group and connect button if no network is selected
# //           document.getElementById('passwordGroup').style.display = 'none';
# //           document.getElementById('connectButton').style.display = 'none';
# //       })
# //       .catch(error => {
# //           console.error('Error fetching networks:', error);
# //       });
# // }

# // // Add event listener to the refresh button
# // document.getElementById('refreshButton').addEventListener('click', refreshNetworks);

# // // Existing code for password toggle
# // document.getElementById('togglePassword').addEventListener('click', function (event) {
# //   event.preventDefault();
# //   var passwordField = document.getElementById('wifiPassword');
# //   var icon = document.getElementById('eyeIcon');

# //   if (passwordField.type === "password") {
# //       passwordField.type = "text";
# //       icon.classList.remove('fa-eye');
# //       icon.classList.add('fa-eye-slash');
# //   } else {
# //       passwordField.type = "password";
# //       icon.classList.remove('fa-eye-slash');
# //       icon.classList.add('fa-eye');
# //   }
# // });

# // // Existing code for handling Wi-Fi selection
# // function handleWifiSelection() {
# //   var selectedNetwork = document.getElementById('wifiNetworks').value;

# //   if (selectedNetwork) {
# //       document.getElementById('passwordGroup').style.display = 'block';
# //       document.getElementById('connectButton').style.display = 'block';
# //   } else {
# //       document.getElementById('passwordGroup').style.display = 'none';
# //       document.getElementById('connectButton').style.display = 'none';
# //   }
# // }

# // // Existing code for connecting to Wi-Fi
# // function connectWifi() {
# //   var formData = new FormData(document.getElementById('wifiForm'));

# //   fetch('/connect-via-wifi', {
# //       method: 'POST',
# //       body: formData
# //   })
# //   .then(response => response.json())
# //   .then(data => {
# //       var successMessageElement = document.getElementById('success-message');
# //       var errorMessageElement = document.getElementById('error-message');

# //       if (data.response.status === "200") {
# //           successMessageElement.classList.remove('hidden');
# //           successMessageElement.classList.add("show-message");
# //           successMessageElement.innerHTML = data.response.message;

# //           document.getElementById('wifiForm').style.display = 'none';
# //           document.querySelector('.connected-network').style.display = 'block';
# //           document.querySelector('.connected-network').innerHTML = `<p>Connected to: ${formData.get('ssid')}</p><button type="button" onclick="disconnectWifi()">Disconnect</button>`;
          
# //           setTimeout(function() {
# //               successMessageElement.classList.add('hidden');
# //               successMessageElement.classList.remove("show-message");
# //           }, 5000);
# //       } else {
# //           errorMessageElement.classList.remove('hidden');
# //           errorMessageElement.classList.add("show-message");
# //           errorMessageElement.innerHTML = data.response.message;
# //           setTimeout(function() {
# //               errorMessageElement.classList.add('hidden');
# //               errorMessageElement.classList.remove("show-message");
# //           }, 5000);
# //       }
# //   })
# //   .catch(error => {
# //       var errorMessageElement = document.getElementById('error-message');
# //       console.error('Error:', error);
# //       errorMessageElement.classList.remove('hidden');
# //       errorMessageElement.classList.add("show-message");
# //       errorMessageElement.innerHTML = 'An error occurred. Please try again.';

# //       setTimeout(function() {
# //           errorMessageElement.classList.add('hidden');
# //       }, 5000);
# //   });
# // }
# // Function to fetch and update the list of available Wi-Fi networks
# // Function to fetch and update the list of available Wi-Fi networks
# // function refreshNetworks() {
# //   fetch('/get-available-networks')
# //       .then(response => response.json())
# //       .then(data => {
# //           const wifiNetworksSelect = document.getElementById('wifiNetworks');
# //           wifiNetworksSelect.innerHTML = '<option value="" disabled selected>Select Wi-Fi Network</option>'; // Reset options
# //           console.log(data);
          
# //           data.networks.forEach(network => {
# //               const option = document.createElement('option');
# //               option.value = network;
# //               option.textContent = network;
# //               wifiNetworksSelect.appendChild(option);
# //           });

# //           // Hide password group and connect button if no network is selected
# //           document.getElementById('passwordGroup').style.display = 'none';
# //           document.getElementById('connectButton').style.display = 'none';
# //       })
# //       .catch(error => {
# //           console.error('Error fetching networks:', error);
# //       });
# // }

# // // Add event listener to the refresh button
# // document.getElementById('refreshButton').addEventListener('click', refreshNetworks);

# // // Existing code for password toggle
# // document.getElementById('togglePassword').addEventListener('click', function (event) {
# //   event.preventDefault();
# //   var passwordField = document.getElementById('wifiPassword');
# //   var icon = document.getElementById('eyeIcon');

# //   if (passwordField.type === "password") {
# //       passwordField.type = "text";
# //       icon.classList.remove('fa-eye');
# //       icon.classList.add('fa-eye-slash');
# //   } else {
# //       passwordField.type = "password";
# //       icon.classList.remove('fa-eye-slash');
# //       icon.classList.add('fa-eye');
# //   }
# // });

# // // Existing code for handling Wi-Fi selection
# // function handleWifiSelection() {
# //   var selectedNetwork = document.getElementById('wifiNetworks').value;

# //   if (selectedNetwork) {
# //       document.getElementById('passwordGroup').style.display = 'block';
# //       document.getElementById('connectButton').style.display = 'block';
# //   } else {
# //       document.getElementById('passwordGroup').style.display = 'none';
# //       document.getElementById('connectButton').style.display = 'none';
# //   }
# // }

# // // Existing code for connecting to Wi-Fi
# // function connectWifi() {
# //   var formData = new FormData(document.getElementById('wifiForm'));

# //   fetch('/connect-via-wifi', {
# //       method: 'POST',
# //       body: formData
# //   })
# //   .then(response => response.json())
# //   .then(data => {
# //       var successMessageElement = document.getElementById('success-message');
# //       var errorMessageElement = document.getElementById('error-message');

# //       if (data.response.status === "200") {
# //           successMessageElement.classList.remove('hidden');
# //           successMessageElement.classList.add("show-message");
# //           successMessageElement.innerHTML = data.response.message;

# //           document.getElementById('wifiForm').style.display = 'none';
# //           document.querySelector('.connected-network').style.display = 'block';
# //           document.querySelector('.connected-network').innerHTML = `<p>Connected to: ${formData.get('ssid')}</p><button type="button" onclick="disconnectWifi()">Disconnect</button>`;
          
# //           setTimeout(function() {
# //               successMessageElement.classList.add('hidden');
# //               successMessageElement.classList.remove("show-message");
# //           }, 5000);
# //       } else {
# //           errorMessageElement.classList.remove('hidden');
# //           errorMessageElement.classList.add("show-message");
# //           errorMessageElement.innerHTML = data.response.message;
# //           setTimeout(function() {
# //               errorMessageElement.classList.add('hidden');
# //               errorMessageElement.classList.remove("show-message");
# //           }, 5000);
# //       }
# //   })
# //   .catch(error => {
# //       var errorMessageElement = document.getElementById('error-message');
# //       console.error('Error:', error);
# //       errorMessageElement.classList.remove('hidden');
# //       errorMessageElement.classList.add("show-message");
# //       errorMessageElement.innerHTML = 'An error occurred. Please try again.';

# //       setTimeout(function() {
# //           errorMessageElement.classList.add('hidden');
# //       }, 5000);
# //   });
# // }

#working code

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


# def get_wifi_networks():
#     try:
#         if platform.system() == 'Linux':
#             # Scan for available WiFi networks using iwlist
#             result = subprocess.run(['sudo', 'iwlist', 'wlan0', 'scan'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             networks_output = result.stdout.decode('utf-8')

#             # Extract SSIDs from the iwlist output
#             ssid_list = re.findall(r'ESSID:"([^"]*)"', networks_output)
            
#             # Get the currently connected SSID
#             connected_ssid_result = subprocess.run(['iwgetid', '-r'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             connected_ssid_output = connected_ssid_result.stdout.decode('utf-8').strip()
#             connected_ssid = connected_ssid_output if connected_ssid_output else None

#             return {"available_networks": ssid_list, "connected_ssid": connected_ssid}
        
#         elif platform.system() == 'Windows':
#             result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             networks_output = result.stdout.decode('utf-8')

#             # Extract SSIDs
#             ssid_list = re.findall(r'SSID \d+ : (.+)', networks_output)

#             # Get the currently connected SSID
#             connected_ssid_match = re.search(r'\s*SSID\s*:\s*(.+)\s*$', networks_output, re.IGNORECASE)
#             connected_ssid = connected_ssid_match.group(1).strip() if connected_ssid_match else None

#             return {"available_networks": ssid_list, "connected_ssid": connected_ssid}
        
#     except Exception as e:
#         return {"available_networks": [], "connected_ssid": None}

# // function connectWifi() {
# //   var formData = new FormData(document.getElementById('wifiForm'));

# //   fetch('/connect-via-wifi', {
# //       method: 'POST',
# //       body: formData
# //   })
# //   .then(response => response.json())
# //   .then(data => {
# //       var successMessageElement = document.getElementById('success-message');
# //       var errorMessageElement = document.getElementById('error-message');

# //       if (data.response.status === "200") {
# //           document.getElementById('refreshButton').style.display = 'none';
# //           successMessageElement.classList.remove('hidden');
# //           successMessageElement.classList.add("show-message");
# //           successMessageElement.innerHTML = data.response.message;

# //           document.getElementById('wifiForm').style.display = 'none';
# //           document.querySelector('.connected-network').style.display = 'block';
# //           document.querySelector('.connected-network').innerHTML = `<p>Connected to: ${formData.get('ssid')}</p><button type="button" onclick="disconnectWifi()">Disconnect</button>`;
          
# //           setTimeout(function() {
# //               successMessageElement.classList.add('hidden');
# //               successMessageElement.classList.remove("show-message");
# //           }, 5000);
# //       } else {
# //           errorMessageElement.classList.remove('hidden');
# //           errorMessageElement.classList.add("show-message");
# //           errorMessageElement.innerHTML = data.response.message;
# //           setTimeout(function() {
# //               errorMessageElement.classList.add('hidden');
# //               errorMessageElement.classList.remove("show-message");
# //           }, 5000);
# //       }
# //   })
# //   .catch(error => {
# //       var errorMessageElement = document.getElementById('error-message');
# //       console.error('Error:', error);
# //       errorMessageElement.classList.remove('hidden');
# //       errorMessageElement.classList.add("show-message");
# //       errorMessageElement.innerHTML = 'An error occurred. Please try again.';

# //       setTimeout(function() {
# //           errorMessageElement.classList.add('hidden');
# //       }, 5000);
# //   });
# // }



# // function disconnectWifi() {
# //   fetch('/disconnect-wifi', {
# //       method: 'POST',
# //   })
# //   .then(response => response.json())
# //   .then(data => {
# //         var successMessageElement = document.getElementById('success-message');
# //         var errorMessageElement = document.getElementById('error-message');
# //       if (data.status === "200") {
# //         successMessageElement.classList.remove('hidden');
# //         successMessageElement.classList.add("show-message");
# //         successMessageElement.innerHTML = "Wifi disconnected";
          
# //           document.getElementById('wifiForm').style.display = 'block';
# //           document.querySelector('.connected-network').style.display = 'none';
# //           setTimeout(function() {
# //             successMessageElement.classList.add('hidden');
# //             successMessageElement.classList.remove("show-message");
# //         }, 5000);
# //       } else {
# //         errorMessageElement.classList.remove('hidden');
# //         errorMessageElement.classList.add("show-message");
# //         errorMessageElement.innerHTML = 'An error occurred. Please try again.';
# //         setTimeout(function() {
# //           errorMessageElement.classList.add('hidden');
# //       }, 5000);
# //       }
# //   })
# //   .catch(error => {
# //       console.error('Error:', error);
# //       alert('An error occurred. Please try again.');
# //   });
# // }



# @app.route('/disconnect-wifi', methods=['POST'])
# def disconnect_wifi():
#     """Disconnect from the current WiFi network."""
#     try:
#         if platform.system() == 'Windows':
#             result = subprocess.run(['netsh', 'wlan', 'disconnect'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
#             if result.returncode == 0:
#                 return jsonify({"status": "200", "message": "Disconnected successfully."})
#             else:
#                 error_message = result.stderr.decode('utf-8').strip()
#                 return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})
        
#         elif platform.system() == 'Linux':
#             result = subprocess.run(['sudo', 'nmcli', 'device', 'disconnect', 'wlan0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
#             if result.returncode == 0:
#                 return jsonify({"status": "200", "message": "Disconnected successfully."})
#             else:
#                 error_message = result.stderr.decode('utf-8').strip()
#                 return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})
        
#         else:
#             return jsonify({"status": "501", "message": "Disconnect not implemented for this platform."})
        
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
#                 return jsonify({"status": "200", "message": "Disconnected successfully."})
#             else:
#                 error_message = result.stderr.decode('utf-8').strip()
#                 return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})

#         elif platform.system() == 'Linux':
#             # Attempt to disconnect using Linux command
#             disconnect_result = subprocess.run(['sudo', 'ifconfig', 'wlan0', 'down'], 
#                                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             print(disconnect_result)
#             print(disconnect_result.returncode)
#             if disconnect_result.returncode == 0:
#                 return jsonify({"status": "200", "message": "Disconnected successfully."})
#             else:
#                 error_message = disconnect_result.stderr.decode('utf-8').strip()
#                 return jsonify({"status": "500", "message": f"Failed to disconnect: {error_message}"})

#     except Exception as e:
#         return jsonify({"status": "500", "message": f"An unexpected error occurred: {str(e)}"})

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
#     #         # Create or append to the wpa_supplicant configuration file
#     #         config_entry = f"""
#     #             network={{
#     #                 ssid="{ssid}"
#     #                 psk="{password}"
#     #                 }}
#     #                         """
#     #         config_file = '/etc/wpa_supplicant/wpa_supplicant.conf'
#     #         print(config_entry)
#     #         # Write to the configuration file
#     #         try:
#     #             with open(config_file, 'a') as f:
#     #                 f.write(config_entry)
#     #             print(config_file)    
#     #             # Reconfigure wpa_supplicant to apply the new configuration
#     #             result = subprocess.run(['sudo', 'wpa_cli', '-i', 'wlan0', 'reconfigure'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     #             print("The result is profile",result.returncode)
#     #             if result.returncode != 0:
#     #                 error_message = result.stderr.decode('utf-8').strip()
#     #                 return {"status": "500", "message": f"Failed to configure WiFi for {ssid}: {error_message}"}
                
#     #             return {"status": "200", "message": "Profile created successfully."}
            
#     #         #except PermissionError:
#     #         #     return {"status": "403", "message": "Permission denied. You need to run this as a superuser."}
#     #         except Exception as e:
#     #             return {"status": "500", "message": f"An unexpected error occurred while writing to {config_file}: {str(e)}"}
#     #     else:
#     #         return {"status": "501", "message": "WiFi profile creation not implemented for this platform."}
    
#     # except Exception as e:
#     #     return {"status": "500", "message": f"An unexpected error occurred: {str(e)}"}

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
#                 print(result)
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
#             time.sleep(3)
            
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
#             print(result)
#             print("The result is",result.returncode)
            
#             # Wait for the connection to establish
            
            
#             # time.sleep(3)
            
#             # status_result = subprocess.run(['iwgetid', '-r'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             # connected_ssid = status_result.stdout.decode('utf-8').strip()
#             # print(status_result)
#             # print(connected_ssid)
            
#             # if (result.returncode == 0):
                
#             #     return {"status": "200", "message": f"Successfully connected to {ssid}"}
#             # else:    
#             #     return {"status": "500", "message": f"Failed to connect to {ssid}."}
#             time.sleep(6)
            
#             # status_result = subprocess.run(['iwgetid', '-r'],
#             #                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             # connected_ssid = status_result.stdout.decode('utf-8').strip()
#             # print("Status result:", status_result)
#             # print("Connected SSID:", connected_ssid)

#             if (result.returncode == 0):
#                return {"status": "200", "message": f"Successfully connected to {ssid}"}
#             else:
#                return {"status": "500", "message": f"Failed to connect to {ssid}."}
            
#             # # Check the connection status
#             # status_result = subprocess.run(['iwgetid', '-r'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             # connected_ssid = status_result.stdout.decode('utf-8').strip()
#             # print(status_result)
#             # print(connected_ssid)
            
#             # if connected_ssid == ssid:
#             #     return {"status": "200", "message": f"Successfully connected to {ssid}"}
#             # else:
#             #     return {"status": "500", "message": f"Failed to connect to {ssid}."}
        
#         else:
#             return {"status": "501", "message": "Connection not implemented for this platform."}
    
#     except Exception as e:
#         return {"status": "500", "message": f"An unexpected error occurred: {str(e)}"}


# {% extends 'base.html' %}

# {% block title %} Settings & Admin {% endblock %}
# {% block cssextend %}
# <link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet">
# {% endblock %}
# {% block content %}
# <div class="container">

# 	<!-- Settings Success -->
# 	{% if (action == "settings") and (errorcode == 0) %}
# 	<div id="alertMessage" class="alert alert-success">
# 		<b> Settings Updated Successfully.</b>
# 	</div>
# 	{% elif (action == "settings") and (errorcode == 1) %}
# 	<div id="alertMessage" class="alert alert-danger">
# 		{% for index in errormessage %}
# 		<b>{{ index }}</b><br>
# 		{% endfor %}
# 	</div>
# 	{% endif %}
# 	<div id="success-message" class="hidden"></div>
# 	<div id="error-message" class="hidden"></div>
# 	<!-- Inventory Card -->
# 	<form name="input" action="/admin/settings" method="POST">
# 		<div class="card">
# 			<div class="card-header">
# 				Inventory
# 			</div>
# 			<div class="card-body">
# 				<table class="table">
# 					<thead>
# 						<tr>
# 							<th>Pump</th>
# 							<th style="width:40%">Drink Ingredient</th>
# 							<th style="width: 14%;">Quantity (in ml)</th>
# 							<th style="width: 10%; text-align:center">Action</th>
# 							<th>Status</th>
# 						</tr>
# 					</thead>

# 					<tbody>
# 						{% for pump_number, pin_number in settings['assignments'].items()|sort %}
# 						<tr>
# 							<td>{{ pump_number }}</td>
# 							<td>
# 								<div>
# 									<select class="form-control" id="inv_{{ pump_number }}"
# 										name="inv_{{ pump_number }}">
# 										{% for ingredient_index, ingredient_name in drink_db['ingredients'].items()|sort
# 										%}
# 										{% if ingredient_index == settings['inventory'][pump_number] %}
# 										<option selected value="{{ ingredient_index }}">{{ ingredient_name }}</option>
# 										{% else %}
# 										<option value="{{ ingredient_index }}">{{ ingredient_name }}</option>
# 										{% endif %}
# 										{% endfor %}
# 									</select>
# 								</div>
# 							</td>
# 							<td>
# 								<input type="number" class="form-control form-control-quantity"
# 									id="qty_{{ pump_number }}" name="qty_{{ pump_number }}" min="0" max="100" step="0.1"
# 									value="{{ settings['quantity'][pump_number] }}"
# 									oninput="updateProgress('{{ pump_number }}')" readonly>
# 							</td>
# 							<td style="text-align: center;">
# 								<button class="btn-start-action btn-green" id="start_{{ pump_number }}" title="Start"
# 									onclick="cleanPumpAction('{{ pump_number }}')">
# 									<i class="fas fa-play"></i>
# 								</button>
# 								<button class="btn-stop-action btn-danger" id="stop_{{ pump_number }}" title="Stop"
# 									style="display:none;" onclick="cancelPumpAction('{{ pump_number }}')">
# 									<i class="fa fa-pause"></i>
# 								</button>
# 							</td>
# 							<td>
# 								<div class="progress">
# 									<div class="progress-bar" id="progress_{{ pump_number }}" role="progressbar"
# 										style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">0%
# 									</div>
# 								</div>
# 							</td>
# 						</tr>
# 						{% endfor %}
# 					</tbody>
# 				</table>
# 				<button type="submit" class="btn btn-success btn-sm">Save Settings</button>
# 			</div>
# 		</div>
# 	</form>
# 	<br>

# 	<!-- Clean Function Card -->
# 	<form name="input" action="/admin/clean" method="POST">
# 		<div class="card">
# 			<div class="card-header">
# 				Cleaning
# 			</div>
# 			<div class="card-body">
# 				<p class="pump-clean-card">
# 					Select the group of pumps to clean, then touch Start Cleaning. The selected group of pumps will turn
# 					on to flush the existing liquid from the tubes. It is recommended to take the tubes out of the water
# 					source halfway through to remove all liquid from the pumps. Important: make sure you have a glass
# 					under the funnel to catch the flushed-out liquid.
# 				</p>
# 				<div class="form-group">
# 					<select class="form-control" id="clean" name="clean_group">
# 						<option selected value="all">Clean ALL</option>
# 						<option value="non_alcoholic">Clean Non-Alcoholic Pumps (1-7)</option>
# 						<option value="alcoholic">Clean Alcoholic Pumps (8-15)</option>
# 					</select>
# 				</div>
# 				<button type="submit" class="btn btn-success btn-sm">Start Cleaning</button>
# 			</div>
# 		</div>
# 	</form>
# 	<br>

# 	{% endblock %}
# 	{% block scripts %}
# 	<script src="{{ url_for('static', filename='js/admin.js') }}"></script>

# 	<script id="quantity-data" type="application/json">
# 		{{ settings['quantity'] | tojson | safe }}
# 	</script>

# 	<script id="percentage-data" type="application/json">
#         {{ settings['percentage']|tojson|safe }}
#     </script>

# 	<script>

# 		setTimeout(function () {
# 			var alertmessage = document.getElementById('alertMessage')
# 			alertmessage.classList.add('hidden');
# 			alertmessage.classList.remove("show-message");
# 		}, 5000);
# 		document.addEventListener('DOMContentLoaded', function () {
# 			// Parse JSON data from script tags
# 			const quantityData = JSON.parse(document.getElementById('quantity-data').textContent);
# 			const percentageData = JSON.parse(document.getElementById('percentage-data').textContent);

# 			function updateProgress(pumpNumber, percentage) {
# 				const progressBar = document.getElementById(`progress_${pumpNumber}`);

# 				if (progressBar) {
# 					progressBar.style.width = `${percentage}%`;

# 					if (percentage <= 20) {
# 						progressBar.style.backgroundColor = 'red';
# 					} else if (percentage > 20 && percentage <= 50) {
# 						progressBar.style.backgroundColor = 'orange';
# 					} else {
# 						progressBar.style.backgroundColor = 'green';
# 					}

# 					progressBar.innerText = `${Math.round(percentage)}%`;
# 					progressBar.setAttribute('aria-valuenow', Math.round(percentage));
# 				}
# 			}

# 			// Iterate through each pump and update the progress bar
# 			for (const [pumpNumber, percentage] of Object.entries(percentageData)) {
# 				updateProgress(pumpNumber, percentage);
# 			}
# 		});
# 	</script>
# 	{% endblock %}

# {% extends 'base.html' %}

# {% block title %} Settings & Admin {% endblock %}
# {% block cssextend %}
# <link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet">
# {% endblock %}
# {% block content %}
# <div class="container">

# 	<!-- Settings Success -->
# 	{% if (action == "settings") and (errorcode == 0) %}
# 	<div id="alertMessage" class="alert alert-success">
# 		<b> Settings Updated Successfully.</b>
# 	</div>
# 	{% elif (action == "settings") and (errorcode == 1) %}
# 	<div id="alertMessage" class="alert alert-danger">
# 		{% for index in errormessage %}
# 		<b>{{ index }}</b><br>
# 		{% endfor %}
# 	</div>
# 	{% endif %}
# 	<div class="message-container">
# 		<div id="success-message" class="hidden message"></div>
# 		<div id="error-message" class="hidden message"></div>
# 	</div>


# 	<!-- Inventory Card -->
# 	<form name="input" action="/admin/settings" method="POST">
# 		<div class="card">
# 			<div class="card-header">
# 				Inventory
# 			</div>
# 			<div class="card-body">
# 				<table class="table">
# 					<thead>
# 						<tr>
# 							<th>Pump</th>
# 							<th style="width:40%">Drink Ingredient</th>
# 							<th style="width: 14%;">Quantity (in ml)</th>
# 							<th style="width: 10%; text-align:center">Action</th>
# 							<th>Status</th>
# 						</tr>
# 					</thead>

# 					<tbody>
# 						{% for pump_number, pin_number in settings['assignments'].items()|sort %}
# 						<tr>
# 							{% if pump_number == "pump_16" %}
# 							<td>Mixture</td>
# 							{% else %}
# 							<td>{{ pump_number }}</td>
# 							{% endif %}
# 							<td>
# 								<!-- <div class="select-wrapper">
# 									<select class="form-control" id="inv_{{ pump_number }}" name="inv_{{ pump_number }}"
# 										{% if pump_number=="pump_16" %}disabled{% endif %}>
# 										{% for ingredient_index, ingredient_name in drink_db['ingredients'].items()|sort%}
										
# 										{% if ingredient_index == settings['inventory'][pump_number] %}

# 										<option selected value="{{ ingredient_index }}" {% if pump_number=="pump_16"
# 											%}disabled{% endif %}>{{ ingredient_name }}</option>
										
# 										{% else %}

# 										<option value="{{ ingredient_index }}" {% if pump_number=="pump_16" %}disabled{%
# 											endif %}>{{ ingredient_name }}</option>
# 										{% endif %}
# 										{% endfor %}
# 									</select>
# 								</div> -->
# 								<div class="select-wrapper">
# 									<div class="custom-dropdown" id="inv_{{ pump_number }}">
# 										<div class="selected-option">
# 											<span>
# 												{% for ingredient_index, ingredient_name in drink_db['ingredients'].items()|sort %}
# 													{% if ingredient_index == settings['inventory'][pump_number] %}
# 														{{ ingredient_name }}
# 													{% endif %}
# 												{% endfor %}
# 											</span>
# 											<i class="arrow"></i>
# 										</div>
# 										<div class="options-container">
# 											{% for ingredient_index, ingredient_name in drink_db['ingredients'].items()|sort %}
# 												<div class="option {% if ingredient_index == settings['inventory'][pump_number] %}selected{% endif %}"
# 													 data-value="{{ ingredient_index }}"
# 													 {% if pump_number == "pump_16" %}style="opacity: 0.5; pointer-events: none;" {% endif %}>
# 													{{ ingredient_name }}
# 												</div>
# 											{% endfor %}
# 										</div>
# 										<input type="hidden" id="hidden_inv_{{ pump_number }}" name="inv_{{ pump_number }}" value="{{ settings['inventory'][pump_number] }}">
# 									</div>
# 								</div>
								
# 							</td>
# 							<td>
# 								<input type="number" class="form-control form-control-quantity"
# 									id="qty_{{ pump_number }}" name="qty_{{ pump_number }}" min="0" max="100" step="0.1"
# 									value="{{ settings['quantity'][pump_number] }}"
# 									oninput="updateProgress('{{ pump_number }}')" readonly>
# 							</td>
# 							<td style="text-align: center;">
# 								<button class="btn-start-action btn-green" id="start_{{ pump_number }}" title="Start"
# 									onclick="cleanPumpAction('{{ pump_number }}')">
# 									<i class="fas fa-play"></i>
# 								</button>
# 								<button class="btn-stop-action btn-danger" id="stop_{{ pump_number }}" title="Stop"
# 									style="display:none;" onclick="cancelPumpAction('{{ pump_number }}')">
# 									<i class="fa fa-pause"></i>
# 								</button>
# 							</td>
# 							<td>
# 								<div class="progress">
# 									<div class="progress-bar" id="progress_{{ pump_number }}" role="progressbar"
# 										style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">0%
# 									</div>
# 								</div>
# 							</td>
# 						</tr>
# 						{% endfor %}
# 					</tbody>
# 				</table>
# 				<button type="submit" class="btn btn-success btn-sm">Save Settings</button>
# 			</div>
# 		</div>
# 	</form>
# 	<br>

# 	<!-- Clean Function Card -->
# 	<form name="input" action="/admin/clean" method="POST">
# 		<div class="card">
# 			<div class="card-header">
# 				Cleaning
# 			</div>
# 			<div class="card-body">
# 				<p class="pump-clean-card">
# 					Select the group of pumps to clean, then touch Start Cleaning. The selected group of pumps will turn
# 					on to flush the existing liquid from the tubes. It is recommended to take the tubes out of the water
# 					source halfway through to remove all liquid from the pumps. Important: make sure you have a glass
# 					under the funnel to catch the flushed-out liquid.
# 				</p>
# 				<div class="form-group">
# 					<select class="form-control" id="clean" name="clean_group">
# 						<option selected value="all">Clean ALL</option>
# 						<option value="non_alcoholic">Clean Non-Alcoholic Pumps (1-7)</option>
# 						<option value="alcoholic">Clean Alcoholic Pumps (8-15)</option>
# 					</select>
# 				</div>
# 				<button type="submit" class="btn btn-success btn-sm">Start Cleaning</button>
# 			</div>
# 		</div>
# 	</form>
# 	<br>

# 	{% endblock %}
# 	{% block scripts %}
# 	<script src="{{ url_for('static', filename='js/admin.js') }}"></script>

# 	<script id="quantity-data" type="application/json">
# 		{{ settings['quantity'] | tojson | safe }}
# 	</script>

# 	<script id="percentage-data" type="application/json">
#         {{ settings['percentage']|tojson|safe }}
#     </script>

# 	<script>

# 		setTimeout(function () {
# 			var alertmessage = document.getElementById('alertMessage')
# 			alertmessage.classList.add('hidden');
# 			alertmessage.classList.remove("show-message");
# 		}, 5000);
# 		document.addEventListener('DOMContentLoaded', function () {
# 			// Parse JSON data from script tags
# 			const quantityData = JSON.parse(document.getElementById('quantity-data').textContent);
# 			const percentageData = JSON.parse(document.getElementById('percentage-data').textContent);

# 			function updateProgress(pumpNumber, percentage) {
# 				const progressBar = document.getElementById(`progress_${pumpNumber}`);

# 				if (progressBar) {
# 					progressBar.style.width = `${percentage}%`;

# 					if (percentage <= 20) {
# 						progressBar.style.backgroundColor = 'red';
# 					} else if (percentage > 20 && percentage <= 50) {
# 						progressBar.style.backgroundColor = 'orange';
# 					} else {
# 						progressBar.style.backgroundColor = 'green';
# 					}

# 					progressBar.innerText = `${Math.round(percentage)}%`;
# 					progressBar.setAttribute('aria-valuenow', Math.round(percentage));
# 				}
# 			}

# 			// Iterate through each pump and update the progress bar
# 			for (const [pumpNumber, percentage] of Object.entries(percentageData)) {
# 				updateProgress(pumpNumber, percentage);
# 			}
# 		});
# 	</script>
# 	<script>
# 		document.querySelectorAll('.custom-dropdown').forEach(select => {
# 			const selectedOption = select.querySelector('.selected-option');
# 			const optionsContainer = select.querySelector('.options-container');
# 			const hiddenInput = select.querySelector('input[type="hidden"]'); // Select hidden input

# 			selectedOption.addEventListener('click', () => {
# 				console.log("click");

# 				optionsContainer.style.display = optionsContainer.style.display === 'block' ? 'none' : 'block';
# 			});

# 			select.querySelectorAll('.option').forEach(option => {
# 				option.addEventListener('click', () => {
# 					if (option.style.pointerEvents !== 'none') { // Check if not disabled
# 						selectedOption.querySelector('span').textContent = option.textContent;
# 						selectedOption.setAttribute('data-value', option.getAttribute('data-value'));
# 						hiddenInput.value = option.getAttribute('data-value');
# 						console.log(hiddenInput);
						
# 						optionsContainer.style.display = 'none';
# 					}
# 				});
# 			});

# 			// Close dropdown when clicking outside
# 			document.addEventListener('click', (event) => {
# 				if (!select.contains(event.target)) {
# 					optionsContainer.style.display = 'none';
# 				}
# 			});
# 		});
		

# 	</script>

# 	<!-- <script>
# 		document.querySelectorAll('.custom-dropdown').forEach(select => {
# 			const selectedOption = select.querySelector('.selected-option');
# 			const optionsContainer = select.querySelector('.options-container');
# 			const hiddenInput = select.querySelector('input[type="hidden"]'); // Select hidden input
	
# 			selectedOption.addEventListener('click', () => {
# 				console.log("click");
# 				optionsContainer.style.display = optionsContainer.style.display === 'block' ? 'none' : 'block';
# 			});
	
# 			select.querySelectorAll('.option').forEach(option => {
# 				option.addEventListener('click', () => {
# 					if (option.style.pointerEvents !== 'none') { // Check if not disabled
# 						selectedOption.querySelector('span').textContent = option.textContent;
# 						selectedOption.setAttribute('data-value', option.getAttribute('data-value'));
						
# 						// Update the hidden input value
# 						hiddenInput.value = option.getAttribute('data-value');
	
# 						optionsContainer.style.display = 'none';
# 					}
# 				});
# 			});
	
# 			// Close dropdown when clicking outside
# 			document.addEventListener('click', (event) => {
# 				if (!select.contains(event.target)) {
# 					optionsContainer.style.display = 'none';
# 				}
# 			});
# 		});
# 	</script> -->
# 		{% endblock %}

# <!-- pop up modal -->
# <!-- <div id="drinkModal" class="modal">
#   <div class="modal-content">
#     <div class="embed-responsive">
#       <p class="popup-heading-info">
#         Please make sure you have placed the mixer.
#       </p>
#     </div>
#     <video
#       src="{{ url_for('static', filename='img/animation-pop-up-make-it.gif') }}" type="video"
#     ></video>
#     <div class="modal-footer">
#       <button class="btn-cancel" onclick="closeModal()">Back</button>
#       <button
#         type="submit"
#         name="makedrink"
#         value="{{ drink_name }}"
#         class="btn-proceed"
#         onclick="proceed()"
#       >
#         Proceed
#       </button>
#     </div>
#   </div>
# </div> -->

#  <!-- <nav class="navbar sticky-top navbar-dark bg-transparent">
#       <a href="/" class="navbar-brand"
#         ><img
#           src="{{ url_for('static', filename='img/cxb-rbg.png') }}"
#           alt="cxb-rbg.png"
#           srcset=""
#       /></a>
#       <button
#         class="navbar-toggler"
#         type="button"
#         data-toggle="collapse"
#         data-target="#navbarNav"
#         aria-controls="navbarNav"
#         aria-expanded="false"
#         aria-label="Toggle navigation"
#       >
#         <span class="navbar-toggler-icon"> </span>
#       </button>

#       <div class="collapse navbar-collapse" id="navbarNav">
#         <ul class="nav navbar-nav mr-auto">
#           <li class="nav-item">
#             <a class="nav-link" href="/"
#               ><i class="far fa-list-alt"></i>&nbsp; Drink Menu</a
#             >
#           </li>
#           <li class="nav-item">
#             <a class="nav-link" href="/bottle-config"
#               ><i class="fa fa-cog" aria-hidden="true"></i>&nbsp; Bottle
#               Config</a
#             >
#           </li>
#           <li class="nav-item">
#             <a class="nav-link" href="/cleaning"
#               ><i class="fa fa-cog" aria-hidden="true"></i>&nbsp; Cleaning</a
#             >
#           </li>
#           <li class="nav-item">
#             <a class="nav-link" href="/admin"
#               ><i class="fa fa-wifi"></i>&nbsp; Admin</a
#             >
#           </li>
#         </ul>
#       </div>
#     </nav> -->
# generating system access key & wifi connection code 
# def generate_system_info(length=25):
#     # File where the key will be stored
#     key_file = 'system_key.txt'

#     # Define the characters to use for the key
#     all_characters = (
#         string.ascii_uppercase +
#         string.ascii_lowercase +
#         string.digits +
#         string.punctuation
#     )

#     # Check if the key already exists
#     if not os.path.exists(key_file):
#         # Generate a new system key
#         system_key = ''.join(random.choice(all_characters) for _ in range(length))

#         # Store the key in the file
#         with open(key_file, 'w') as file:
#             file.write(system_key)
#     else:
#         # Read the existing key from the file
#         with open(key_file, 'r') as file:
#             system_key = file.read().strip()
#     print("Using existing system key:", system_key)
    
#     return {"system_key":system_key,"system_machine_name":"Barhostess123"}


# @app.route('/admin/<action>', methods=['POST', 'GET'])
# @app.route('/admin', methods=['POST', 'GET'])
# def admin(action=None):
#     settings = ReadSettings()
#     drink_db = ReadDrinkDB()
#     status = ReadStatus()
#     available_GPIOs = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
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

#         duplicated_pin = []
#         for pump_number, pin_number in settings['assignments'].items():
#             for pump_number_inside, pin_number_inside in settings['assignments'].items():
#                 if (pin_number != 0) and (pin_number == pin_number_inside) and (pump_number != pump_number_inside):
#                     errorcode = 1
#                     if pin_number not in duplicated_pin:
#                         duplicated_pin.append(pin_number)
#                         errormessage.append('Pin ' + str(pin_number) + ' is assigned to more than one pump. ')

#         if 'flow_rate' in response:
#             settings['flowrate'] = int(response['flow_rate'])

#         if errorcode > 0:
#             settings = ReadSettings()
#             errormessage.append('Settings NOT saved. Please check your settings and try again. ')
#         else:
#             WriteSettings(settings)

#     if request.method == 'POST' and action == 'pump_clean':
#         response = request.get_json()
#         pump_number_clean = response.get('pump_number')
#         action = response.get('action')
#         drink_name = 'clean'
        
#         if (action == "cancel"):
#                     status['control']['stop'] = 1 
#                     WriteStatus(status)
#                     return jsonify({'status': 'success', 'message': 'Pump re-fill deactivated'})
                
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

    # if request.method == 'POST' and action == 'clean':
    #     response = request.form
    #     clean_group = response.get('clean_group')  # Accessing the form data safely
    #     print(f"Clean group selected: {clean_group} ")  
    #     drink_name = 'clean'
        
    #     # Define pump two groups dynamically from settings.json
    #     non_alcoholic_pumps = [pump for pump in settings['inventory'].keys() if pump in ['pump_01', 'pump_02', 'pump_03', 'pump_04', 'pump_05', 'pump_06', 'pump_07']]
    #     alcoholic_pumps = [pump for pump in settings['inventory'].keys() if pump in ['pump_08', 'pump_09', 'pump_10', 'pump_11', 'pump_12', 'pump_13', 'pump_14', 'pump_15']]

    #     if clean_group == 'all':
    #         status['status']['active'] = 0
    #         status['status']['progress'] = 0
    #         status['control']['start'] = 0
    #         status['control']['pause'] = 0
    #         status['control']['stop'] = 0
    #         status['control']['clean'] = "all"
    #         status['control']['drink_name'] = 'empty'
    #         WriteStatus(status)
    #         return render_template('work.html', drink_name=drink_name, action="default", workmode='clean',clean_pump_group = 'all')

    #     elif clean_group == 'non_alcoholic':
    #         clean_pumps(non_alcoholic_pumps, status)
    #         return render_template('work.html', drink_name=drink_name, action="default", workmode='clean', clean_pump_group='non alcoholic')

    #     elif clean_group == 'alcoholic':
    #         clean_pumps(alcoholic_pumps, status)
    #         return render_template('work.html', drink_name=drink_name, action="default", workmode='clean', clean_pump_group='alcoholic')

    #     else:
    #         return "Error: Invalid selection", 400  
    
#     return render_template('admin.html', action=action, errorcode=errorcode, errormessage=errormessage, settings=settings, drink_db=drink_db, available_GPIOs=available_GPIOs)
		# <!-- <td>
		# 						<div class="select-wrapper">
		# 							<div class="custom-dropdown" id="qty_{{ pump_number }}">
		# 								<div class="selected-option" onclick="toggleDropdown(this)">
		# 									<span>
		# 										{% if settings['quantity'][pump_number] in [1000, 700, 500, 350, 200] %}
		# 										{{ settings['quantity'][pump_number] }}
		# 										{% else %}
		# 										1000
		# 										{% endif %}
		# 									</span>
		# 									<i class="fas fa-chevron-down down-arrow"></i>
		# 									<i class="fas fa-chevron-up up-arrow" style="display: none;"></i>
		# 								</div>

		# 								<div class="qty-options-container" style="display: none;">
		# 									{% for quantity in [1000, 700, 500, 350, 200] %}
		# 									<div class="option {% if quantity == settings['quantity'][pump_number] %}selected{% endif %}"
		# 										data-value="{{ quantity }}"
		# 										onclick="selectQuantity('{{ pump_number }}', {{ quantity }})">
		# 										{{ quantity }}
		# 									</div>
		# 									{% endfor %}
		# 								</div>

		# 								<input type="hidden" id="hidden_qty_{{ pump_number }}"
		# 									name="qty_{{ pump_number }}"
		# 									value="{{ settings['quantity'][pump_number] }}">
		# 							</div>
		# 						</div>
		# 					</td> -->
     # Update the quantity of this pump immediately after calculating runtime
            # consumed_quantity = int(pump_runtime * (settings['flowrate'] / 100))
            # if pump_number in settings['quantity']:
            #     standard_quantity = settings['quantity'][pump_number]
            #     # settings['quantity'][pump_number] = max(0, standard_quantity - consumed_quantity)
            #     current_quantity = max(0, standard_quantity - consumed_quantity)

            #     # Calculate and store percentage for pump
            #     if standard_quantity > 0:
            #         percentage = (current_quantity / standard_quantity) * 100
            #     else:
            #         percentage = 0
                
            #     print(f"Progress for pump {pump_number}: {percentage}%")
                
            #     # Store updated percentage in settings
            #     settings['percentage'][pump_number] = percentage
                # settings['quantity'][pump_number] = current_quantity  # Update quantity
                
        #         // document.addEventListener('DOMContentLoaded', function () {
		# // 	const quantityData = JSON.parse(document.getElementById('quantity-data').textContent);
		# // 	const percentageData = JSON.parse(document.getElementById('percentage-data').textContent);

		# // 	function updateProgress(pumpNumber, percentage) {
		# // 		const progressBar = document.getElementById(`progress_${pumpNumber}`);

		# // 		if (progressBar) {
		# // 			progressBar.style.width = `${percentage}%`;

		# // 			if (percentage <= 20) {
		# // 				progressBar.style.backgroundColor = 'red';
		# // 			} else if (percentage > 20 && percentage <= 50) {
		# // 				progressBar.style.backgroundColor = 'orange';
		# // 			} else {
		# // 				progressBar.style.backgroundColor = 'green';
		# // 			}

		# // 			progressBar.innerText = `${Math.round(percentage)}%`;
		# // 			progressBar.setAttribute('aria-valuenow', Math.round(percentage));
		# // 		}
		# // 	}

		# // 	for (const [pumpNumber, percentage] of Object.entries(percentageData)) {
		# // 		updateProgress(pumpNumber, percentage);
		# // 	}
		# // });
  
      # Update the quantity of this pump immediately after calculating runtime
            # consumed_quantity = int(pump_runtime * (settings['flowrate'] / 100))
            # if pump_number in settings['quantity']:
            #     standard_quantity = settings['quantity'][pump_number]
            #     # settings['quantity'][pump_number] = max(0, standard_quantity - consumed_quantity)
            #     current_quantity = max(0, standard_quantity - consumed_quantity)

            #     # Calculate and store percentage for pump
            #     if standard_quantity > 0:
            #         percentage = (current_quantity / standard_quantity) * 100
            #     else:
            #         percentage = 0
                
            #     print(f"Progress for pump {pump_number}: {percentage}%")
                
            #     # Store updated percentage in settings
            #     settings['percentage'][pump_number] = percentage
                # settings['quantity'][pump_number] = current_quantity  # Update quantity


# /* #loader {

#     position: absolute;
#     top: 27%;
#     left: 59%;
#     height: 80px;
#     width: 256px;
#     background-color: #f8f9fa;
#     margin: 20px auto;
# }

# #glass {
#     position: relative;
#     height: 400%;
#     width: 257px;
#     background: rgba(255, 255, 255, .1);
#     border-radius: 0% 0% 15% 15%;
#     border: 10px solid;
#     border-top: 0;
#     border-bottom: 21px solid;
#     border-color: rgba(166, 235, 213, 0.7);
#     overflow: hidden;

# }

# #drink {
#     position: absolute;
#     top: 100%;
#     right: 0;
#     bottom: 0;
#     left: 0;
#     background: linear-gradient(to bottom, orange, orangered);
#     box-shadow: inset 0 2px 1px rgba(255, 69, 0, .2);
#     opacity: .7;
# }

# #counter {
#     position: relative;
#     line-height: 200px;
#     font-size: 60px;
#     font-weight: 700;
#     color: #e9ecef;
#     top: 30%;
#     right: -32%;
# }

# #lemon {
#     display: block;
#     position: absolute;
#     top: 0;
#     right: 0;
#     height: 79px;
#     width: 79px;
#     margin-top: -38px;
#     margin-right: -38px;
#     background: radial-gradient(#f7f3b6 10%, #d7d26c);
#     border-radius: 50%;
#     border: 4px solid #47582e;
#     box-shadow: inset 0 0 0 2px #f7f3b6;
# }

# #straw {
#     display: block;
#     position: absolute;
#     bottom: 20px;
#     right: 30%;
#     height: 220px;
#     width: 6px;
#     background: steelblue;
#     border-radius: 0 6px 0 0;
#     transform: rotate(-18.5deg);
#     transform-origin: left bottom;
#     -webkit-transform: rotate(-18.5deg);
#     -webkit-transform-origin: left bottom;
# }

# #straw:after {
#     content: '';
#     position: absolute;
#     top: 0;
#     right: 0;
#     height: 6px;
#     width: 80px;
#     background: inherit;
#     border-radius: 0 6px 0 0;
# }

# #cubes {
#     position: absolute;
#     top: 0;
#     right: 0;
#     bottom: 0;
#     left: 0;
# }

# #cubes div {
#     position: absolute;
#     width: 50px;
#     height: 50px;
#     background: rgba(255, 255, 255, .3);
#     border-radius: 10px;
#     box-shadow: inset 0 0 10px rgba(255, 255, 255, .6);
# }

# #cubes div:nth-child(1) {
#     bottom: 0;
# }

# #cubes div:nth-child(2) {
#     bottom: 45px;
#     left: 25px;
#     transform: rotate(32deg);
#     transform-origin: center bottom;
#     -webkit-transform: rotate(32deg);
#     -webkit-transform-origin: center bottom;
# }

# #cubes div:nth-child(3) {
#     bottom: 90px;
#     left: 20px;
#     transform: rotate(-34deg);
#     transform-origin: center bottom;
#     -webkit-transform: rotate(-34deg);
#     -webkit-transform-origin: center bottom;
# }

# #coaster {
#     width: 139%;
#     height: 8px;
#     margin-left: -15%;
#     background: steelblue;
#     border-radius: 2px;
# }

# .glass-container {
#     position: absolute;
#     top: 5%;
#     right: 2%;
# }


# .dispense-button {
#     display: flex;
#     justify-content: end;
# }

# .glass-container .btn {
#     margin-top: 0px;
# }

# .glass-container h4 {
#     text-align: start !important;
#     padding-right: 10px;
# } */


# /* 
# .dispense-container {
#     position: absolute;
#     background-color: #d7d26c;
#     left: 10px;
#     bottom: 0;
#     right: 10px;
#     padding: 10px;
#     border-radius: 8px;
# }

# .dispense-actions {
#     display: flex;
#     align-items: center;
# }

# .progress-container {
#     flex: 7;
# }


# #CleanStatus {
#     width: 100%;
#     height: 100%;
# }

# .dispense-button {
#     display: flex;
#     width: 30%;
#     justify-content: space-between;
# }

# #cancelbutton {
#     margin-right: auto;
# }

# #donebutton {
#     margin-left: auto;
# } */

# /* Styling the overall container and progress bar */
# <!-- 
# 			<div class="glass-container">
# 				<div class="dispense-button">
# 					<a href="/work/cancel" class="btn btn-danger btn-lg" role="button" id="cancelbutton">Cancel</a>
# 					<a href="/" class="btn btn-success btn-lg" role="button" id="donebutton">Enjoy</a>
# 				</div>
# 			</div>

# 			<div id="loader">
# 				<div id="lemon"></div>
# 				<div id="straw"></div>
# 				<div id="glass">
# 					<div id="cubes">
# 						<div></div>
# 						<div></div>
# 						<div></div>
# 					</div>
# 					<div id="drink"></div>
# 					<span id="counter"></span>
# 				</div>
# 				<div id="coaster"></div>

# 			</div>  -->
	# <!-- 
	# <script>
	# 	var worker = null;
	# 	$('#donebutton').hide();
	# 	$(document).ready(function () {
	# 		req = $.ajax({
	# 			url: '/workstatus',
	# 			type: 'GET'
	# 		});

	# 		req.done(function (data) {
	# 			var loaded = data.percent_done;

	# 			$('#lemon').hide();
	# 			$('#straw').hide();
	# 			$('#cubes div').hide();

	# 			$('#counter').html(loaded + '%');
	# 			$('#drink').css('top', (100 - loaded * .9) + '%');
	# 			if (loaded == 25) $('#cubes div:nth-child(1)').fadeIn(100);
	# 			if (loaded == 50) $('#cubes div:nth-child(2)').fadeIn(100);
	# 			if (loaded == 75) $('#cubes div:nth-child(3)').fadeIn(100);
	# 			if (loaded == 100) {
	# 				$('#lemon').fadeIn(100);
	# 				$('#straw').fadeIn(300);
	# 				stopWorking();
	# 			};
	# 		});

	# 		// Get data every 1 second
	# 		function drawDrink() {
	# 			req = $.ajax({
	# 				url: '/workstatus',
	# 				type: 'GET'
	# 			});

	# 			req.done(function (data) {
	# 				loaded = data.percent_done;

	# 				$('#counter').html(loaded + '%');
	# 				$('#drink').css('top', (100 - loaded * .9) + '%');
	# 				if (loaded == 25) $('#cubes div:nth-child(1)').fadeIn(100);
	# 				if (loaded == 50) $('#cubes div:nth-child(2)').fadeIn(100);
	# 				if (loaded == 75) $('#cubes div:nth-child(3)').fadeIn(100);
	# 				if (loaded == 100) {
	# 					$('#lemon').fadeIn(100);
	# 					$('#straw').fadeIn(300);
	# 					stopWorking();
	# 				};
	# 			});
	# 		};

	# 		function stopWorking() {
	# 			console.log('stopWorking');
	# 			clearInterval(worker);
	# 			$('#cancelbutton').hide();
	# 			$('#statusMessage').html('All done!');
	# 			$('#donebutton').show();
	# 			setTimeout(function () {
	# 				location.replace("/");
	# 			}, 30000);
	# 		}

	# 		worker = setInterval(drawDrink, 1000);

	# 	});

	# </script> -->

# {% extends 'base.html' %}

# {% block title %} Settings & Admin {% endblock %}
# {% block cssextend %}
# <link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet">
# {% endblock %}
# {% block content %}
# <div class="container config-container">
# 	<!-- Settings Success -->
# 	{% if (action == "settings") and (errorcode == 0) %}
# 	<div id="alertMessage" class="alert alert-success">
# 		<b> Settings Updated Successfully.</b>
# 	</div>
# 	{% elif (action == "settings") and (errorcode == 1) %}
# 	<div id="alertMessage" class="alert alert-danger">
# 		{% for index in errormessage %}
# 		<b>{{ index }}</b><br>
# 		{% endfor %}
# 	</div>
# 	{% endif %}
# 	<div class="message-container">
# 		<div id="success-message" class="hidden message"></div>
# 		<div id="error-message" class="hidden message"></div>
# 	</div>


# 	<!-- Inventory Card -->
# 	<form name="input" id="settingsForm" action="/bottle-config/settings" method="POST">
# 		<div class="card">
# 			<div class="card-body">
# 				<table class="table">
# 					<thead>
# 						<tr>
# 							<th style="width: 14%;">Pump</th>
# 							<th style="width: 20%;">Drink Ingredient</th>
# 							<th style="width: 20%;">Quantity (in ml)</th>
# 							<th style="width: 14%;">In Quantity (in ml)</th>
# 							<th style="width: 10%; text-align:center">Action</th>
# 							<th>Status</th>
# 						</tr>
# 					</thead>
# 					<tbody>
# 						{% for pump_number, pin_number in settings['assignments'].items()|sort %}
# 						<tr data-pump="{{ pump_number }}" data-quantity="{{ settings['quantity'][pump_number] }}">
# 							<!-- {% if pump_number == "pump_16" %}
# 							<td>Mixture</td>
# 							{% else %} -->
# 							<td>{{ pump_number }}</td>
# 							{% endif %}
# 							<td>
# 								<div class="select-wrapper">
# 									<div class="custom-dropdown" id="inv_{{ pump_number }}">
# 										<div class="selected-option">
# 											<span>
# 												{% for ingredient_index, ingredient_name in
# 												drink_db['ingredients'].items()|sort %}
# 												{% if ingredient_index == settings['inventory'][pump_number] %}
# 												{{ ingredient_name }}
# 												{% endif %}
# 												{% endfor %}
# 											</span>
# 											<i class="fas fa-chevron-down down-arrow"></i>
# 											<i class="fas fa-chevron-up up-arrow" style="display: none;"></i>
# 										</div>
# 										<div class="options-container">
# 											{% for ingredient_index, ingredient_name in
# 											drink_db['ingredients'].items()|sort %}
# 											<div class="option {% if ingredient_index == settings['inventory'][pump_number] %}selected{% endif %}"
# 												data-value="{{ ingredient_index }}" {% if pump_number=='pump_16'
# 												%}style="opacity: 0.5; pointer-events: none;" {% endif %}>
# 												{{ ingredient_name }}
# 											</div>
# 											{% endfor %}
# 										</div>
# 										<input type="hidden" id="hidden_inv_{{ pump_number }}"
# 											name="inv_{{ pump_number }}"
# 											value="{{ settings['inventory'][pump_number] }}">
# 									</div>
# 								</div>

# 							</td>

# 							<td>
# 								<div class="select-wrapper">
# 									<div class="custom-dropdown" id="qty_{{ pump_number }}">
# 										<div class="selected-option">
# 											<span>
# 												{% if settings['quantity'][pump_number] in [1000, 700, 500, 350, 200] %}
# 												{{ settings['quantity'][pump_number] }}
# 												{% else %}
# 												1000
# 												{% endif %}
# 											</span>
# 											<i class="fas fa-chevron-down down-arrow"></i>
# 											<i class="fas fa-chevron-up up-arrow" style="display: none;"></i>
# 										</div>

# 										<div class="options-container" style="display: none;">
# 											{% for quantity in [1000, 700, 500, 350, 200] %}
# 											<div class="option {% if quantity == settings['quantity'][pump_number] %}selected{% endif %}"
# 												data-value="{{ quantity }}">
# 												{{ quantity }}
# 											</div>
# 											{% endfor %}
# 										</div>

# 										<input type="hidden" id="hidden_qty_{{ pump_number }}"
# 											name="qty_{{ pump_number }}"
# 											value="{{ settings['quantity'][pump_number] }}">
# 									</div>
# 								</div>
# 							</td>

# 							<td>
# 								<input type="number" class="form-control form-control-quantity"
# 									id="qty_{{ pump_number }}" name="qty_{{ pump_number }}" min="0" max="100" step="0.1"
# 									value="{{ settings['in_quantity'][pump_number] }}"
# 									oninput="updateProgress('{{ pump_number }}')" readonly>
# 							</td>
# 							<td style="text-align: center;">
# 								<button class="btn-start-action btn-green" id="start_{{ pump_number }}" title="Start"
# 									onclick="cleanPumpAction('{{ pump_number }}')">
# 									<i class="fas fa-play"></i>
# 								</button>
# 								<button class="btn-stop-action btn-danger" id="stop_{{ pump_number }}" title="Stop"
# 									style="display:none;" onclick="cancelPumpAction('{{ pump_number }}')">
# 									<i class="fa fa-pause"></i>
# 								</button>
# 							</td>
# 							<td>
# 								<div class="progress">
# 									<div class="progress-bar" id="progress_{{ pump_number }}" role="progressbar"
# 										style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">0%
# 									</div>
# 								</div>
# 							</td>
# 						</tr>
# 						{% endfor %}
# 					</tbody>
# 				</table>
# 			</div>
# 		</div>
# 	</form>
# 	<div class="toggle-panel-container" style="display: none;">
# 		<button id="toggle-open-panel" onclick="togglePanelVisibility()">

# 			<svg fill="#ffffff" height="40px" width="40px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
# 				xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512.006 512.006" xml:space="preserve"
# 				transform="rotate(90)" stroke="#ffffff">
# 				<g id="SVGRepo_bgCarrier" stroke-width="0"></g>
# 				<g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
# 				<g id="SVGRepo_iconCarrier">
# 					<g>
# 						<g>
# 							<path
# 								d="M388.419,475.59L168.834,256.005L388.418,36.421c8.341-8.341,8.341-21.824,0-30.165s-21.824-8.341-30.165,0 L123.586,240.923c-8.341,8.341-8.341,21.824,0,30.165l234.667,234.667c4.16,4.16,9.621,6.251,15.083,6.251 c5.461,0,10.923-2.091,15.083-6.251C396.76,497.414,396.76,483.931,388.419,475.59z">
# 							</path>
# 						</g>
# 					</g>
# 				</g>
# 			</svg>
# 		</button>

# 		<!-- Panel Content -->
# 		<div id="bottom-panel" class="bottom-panel">
# 			<button class="close-panel" onclick="togglePanelVisibility()">
# 				<svg height="40px" width="40px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"
# 					transform="rotate(180)" stroke="#ffffff">
# 					<g id="SVGRepo_bgCarrier" stroke-width="0"></g>
# 					<g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
# 					<g id="SVGRepo_iconCarrier">
# 						<path d="M20 15L12 7L4 15" stroke="#ffffff" stroke-width="1.5" stroke-linecap="round"
# 							stroke-linejoin="round"></path>
# 					</g>
# 				</svg>
# 			</button>
# 			<div class="panel-buttons">
# 				<a href="/" class="panel-btn" rel="noopener noreferrer">Back</a>
# 				<a href="/cleaning" class="panel-btn" rel="noopener noreferrer">Cleaning</a>
# 				<button type="button" class="panel-btn" onclick="submitSettingsForm()">Save Settings</button>
# 			</div>
# 		</div>
# 	</div>

# 	{% endblock %}
# 	{% block scripts %}
# 	<script src="{{ url_for('static', filename='js/bottle_config.js') }}"></script>

# 	<script id="quantity-data" type="application/json">
# 		{{ settings['quantity'] | tojson | safe }}
# 	</script>

# 	<script id="percentage-data" type="application/json">
#         {{ settings['percentage']|tojson|safe }}
#     </script>

# 	<script>

# 		setTimeout(function () {
# 			var alertmessage = document.getElementById('alertMessage')
# 			alertmessage.classList.add('hidden');
# 			alertmessage.classList.remove("show-message");
# 		}, 5000);

# 		document.addEventListener('DOMContentLoaded', function () {
# 			const quantityData = JSON.parse(document.getElementById('quantity-data').textContent);

# 			function updateProgress(pumpNumber, quantity) {
# 				const progressBar = document.getElementById(`progress_${pumpNumber}`);

# 				if (progressBar) {
# 					const percentage = (quantity / 1000) * 100;

# 					progressBar.style.width = `${percentage}%`;

# 					if (quantity <= 200) {
# 						progressBar.style.backgroundColor = 'red';
# 					} else if (quantity <= 500) {
# 						progressBar.style.backgroundColor = 'orange';
# 					} else {
# 						progressBar.style.backgroundColor = 'green';
# 					}

# 					// Update the percentage text inside the progress bar
# 					progressBar.innerText = `${Math.round(percentage)}%`;
# 					progressBar.setAttribute('aria-valuenow', Math.round(percentage));
# 				}
# 			}

# 			// Loop through each pump's quantity and update the progress bar
# 			Object.entries(quantityData).forEach(([pumpNumber, quantity]) => {
# 				updateProgress(pumpNumber, quantity);
# 			});
# 		});


# 	</script>
# 	<script>
# 		document.querySelectorAll('.custom-dropdown').forEach(select => {
# 			const selectedOption = select.querySelector('.selected-option');
# 			const optionsContainer = select.querySelector('.options-container');
# 			const hiddenInput = select.querySelector('input[type="hidden"]');

# 			const toggleArrows = (isOpen) => {
# 				selectedOption.querySelector('.down-arrow').style.display = isOpen ? 'none' : 'block';
# 				selectedOption.querySelector('.up-arrow').style.display = isOpen ? 'block' : 'none';
# 			};

# 			selectedOption.addEventListener('click', () => {
# 				const isOpen = optionsContainer.style.display === 'block';
# 				optionsContainer.style.display = isOpen ? 'none' : 'block';
# 				toggleArrows(!isOpen);
# 			});

# 			select.querySelectorAll('.option').forEach(option => {
# 				option.addEventListener('click', () => {
# 					if (option.style.pointerEvents !== 'none') {
# 						selectedOption.querySelector('span').textContent = option.textContent;
# 						selectedOption.setAttribute('data-value', option.getAttribute('data-value'));
# 						hiddenInput.value = option.getAttribute('data-value');
# 						console.log(option.getAttribute('data-value'))
# 						toggleArrows(false);
# 						optionsContainer.style.display = 'none';
# 					}
# 				});
# 			});

# 			document.addEventListener('click', (event) => {
# 				if (!select.contains(event.target)) {
# 					optionsContainer.style.display = 'none';
# 					toggleArrows(false);
# 				}
# 			});
# 		});

# 	</script>
# 	<!-- panel button -->
# 	<script>
# 		document.addEventListener("DOMContentLoaded", function () {
# 			function togglePanelVisibility() {
# 				const panel = document.getElementById('bottom-panel');
# 				if (panel) {
# 					panel.classList.toggle('active');
# 				} else {
# 					console.error("Panel element not found!");
# 				}
# 			}
# 			const toggleButton = document.getElementById('toggle-open-panel');
# 			const closeButton = document.querySelector('.close-panel');

# 			if (toggleButton) {
# 				toggleButton.addEventListener('click', togglePanelVisibility);
# 			}
# 			if (closeButton) {
# 				closeButton.addEventListener('click', togglePanelVisibility);
# 			}
# 		});

# 		function submitSettingsForm() {
# 			document.getElementById('settingsForm').submit();
# 		}
# 	</script>

# 	{% endblock %}

# function proceed() {
#   var video = document.querySelector("#drinkModal video");
#   if (video) {
#     video.pause();
#     video.currentTime = 0;
#   }
#   document.getElementById('drinkForm').submit();
# }


# function closeModal() {
#   var video = document.querySelector("#drinkModal video");
#   if (video) {
#     video.pause();
#     video.currentTime = 0;
#   }

#   document.getElementById("drinkModal").style.display = "none";
#   document.body.classList.remove("modal-open");

#   // Resume the carousel
#   let carousel = document.getElementById('drinklist');
#   if (carousel && typeof carousel.carousel === 'undefined') {
#     $(carousel).carousel('cycle'); // Ensure cycling through jQuery fallback
#   } else {
#     bootstrap.Carousel.getInstance(carousel).cycle();
#   }
# }

        # <li class="nav-item dropdown">
        #   <a class="nav-link dropdown-toggle" href="#" id="adminDropdown" role="button" data-toggle="dropdown"
        #     aria-haspopup="true" aria-expanded="false">
        #     <i class="fa fa-user" aria-hidden="true"></i>&nbsp; Admin
        #   </a>
        #   <div class="dropdown-menu sub-menu" aria-labelledby="adminDropdown">
        #     <a class="dropdown-item" href="/wifi-configuration">
        #       <i class="fa fa-wifi"></i>&nbsp; WiFi configuration
        #     </a>
        #   </div>
        # </li>


# function openModal(drinkName) {
#   let inputField = document.createElement("input");
#   inputField.type = "hidden";
#   inputField.name = "makedrink";
#   inputField.value = drinkName;

#   let form = document.getElementById("drinkForm");
#   form.appendChild(inputField);

#   document.getElementById("drinkModal").style.display = "block";
#   document.body.classList.add("modal-open");

#   // // Pause the carousel using Bootstrap's native JavaScript API
#   // let carousel = document.getElementById("drinklist");
#   // if (carousel && typeof carousel.carousel === "undefined") {
#   //   $(carousel).carousel("pause");
#   // } else {
#   //   bootstrap.Carousel.getInstance(carousel).pause();
#   // }
#   let carousel = document.getElementById("drinklist");
#   if (carousel) {
#     let carouselInstance = bootstrap.Carousel.getOrCreateInstance(carousel);
#     carouselInstance.pause();
#   }
# }

# var worker = null;
# 		var isPaused = false;
# 		$('#donebutton').hide();

# 		$(document).ready(function () {
			
# 			req = $.ajax({
# 				url: '/workstatus',
# 				type: 'GET'
# 			});

# 			req.done(function (data) {
# 				var loaded = data.percent_done;

# 				$('#counter').html(loaded + '%');
# 				$('#progress-bar').css('width', loaded + '%');

# 				if (loaded == 100) {
# 					stopWorking();
# 				}
# 			});

# 			// Get data every 1 second
# 			function drawDrink() {
# 				req = $.ajax({
# 					url: '/workstatus',
# 					type: 'GET'
# 				});

# 				req.done(function (data) {
# 					loaded = data.percent_done;

# 					$('#counter').html(loaded + '%');
# 					$('#progress-bar').css('width', loaded + '%'); 
# 					if (loaded == 100) {
# 						stopWorking();
# 					}
# 				});
# 			};

# 			function stopWorking() {
# 				console.log('stopWorking');
# 				clearInterval(worker);
# 				$('#cancelbutton').hide();
# 				$('#statusMessage').html('All done!');
# 				$('#donebutton').show();
# 				setTimeout(function () {
# 					location.replace("/");
# 				}, 30000);
# 			}

# 			worker = setInterval(drawDrink, 1000);

# 		});

	# <!-- <script>
	# 	var worker = null;
	# 	var isPaused = false;
	# 	$('#donebutton').hide();

	# 	$(document).ready(function () {
			
	# 		req = $.ajax({
	# 			url: '/workstatus',
	# 			type: 'GET'
	# 		});

	# 		req.done(function (data) {
	# 			var loaded = data.percent_done;

	# 			$('#counter').html(loaded + '%');
	# 			$('#progress-bar').css('width', loaded + '%');

	# 			if (loaded == 100) {
	# 				stopWorking();
	# 			}
	# 		});

	# 		// Get data every 1 second
	# 		function drawDrink() {
	# 			req = $.ajax({
	# 				url: '/workstatus',
	# 				type: 'GET'
	# 			});

	# 			req.done(function (data) {
	# 				loaded = data.percent_done;

	# 				$('#counter').html(loaded + '%');
	# 				$('#progress-bar').css('width', loaded + '%'); 
	# 				if (loaded == 100) {
	# 					stopWorking();
	# 				}
	# 			});
	# 		};

	# 		function stopWorking() {
	# 			console.log('stopWorking');
	# 			clearInterval(worker);
	# 			$('#cancelbutton').hide();
	# 			$('#statusMessage').html('All done!');
	# 			$('#donebutton').show();
	# 			setTimeout(function () {
	# 				location.replace("/");
	# 			}, 30000);
	# 		}

	# 		worker = setInterval(drawDrink, 1000);

	# 	});
	# </script> -->
#  <!-- <a href="/work/cancel" class="btn " role="button" id="cancelbutton">Pause</a>
# 					<a href="/" class="btn btn-success" role="button" id="donebutton">Enjoy</a> -->

# control.py
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
# prototype_mode = False
#prototype_mode = True # Comment out for normal operation
# *****************************************
# Imported Libraries
# *****************************************

#from __future__ import division
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

# def Pour(pump_number, waitTime, platform):
#     print(f' * Thread: {pump_number} Started for {waitTime} seconds.')
#     platform.ActivatePump(pump_number)
#     for x in range(waitTime): 
#         time.sleep(1)
#         global stop_threads 
#         if(stop_threads): 
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
# $('#pauseResumeButton').on('click', function () {
#     if (isPaused) {
#         // Resume: Restart progress updates
#         isPaused = false;
#         $(this).text('Pause'); // Change button text to "Pause"
#         $.get('/work/resume', function () {
#             console.log("Server notified to resume work.");
#         }); // Notify the server to resume work

#         // Restart the interval only if not already running
#         if (!worker) {
#             worker = setInterval(updateProgress, 1000); // Restart the interval
#         }
#     } else {
#         // Pause: Stop progress updates
#         isPaused = true;
#         $(this).text('Resume'); // Change button text to "Resume"
#         clearInterval(worker); // Stop the interval
#         worker = null; // Clear the worker to avoid duplicates
#         $.get('/work/pause', function () {
#             console.log("Server notified to pause work.");
#         }); // Notify the server to pause work
#     }
# });

############################Working Code##################3
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
#         global stop_threads 
#         if stop_threads: 
#             print(f' * Thread: {pump_number} cancelling.')
#             break
#         while pause_threads:
#             print(f' * Thread: {pump_number} paused. Waiting to resume...')
#             time.sleep(1)  # Pause while `pause_threads` is True
#         time.sleep(1)
#     platform.DeActivatePump(pump_number)
#     print(f' * Thread: {pump_number} finished.')
    
# def DelayedPour(pump_number, runtime, platform, delay):
#     time.sleep(delay)
#     Pour(pump_number, runtime, platform)


# # def PourDrink(drink_name):
# #     drink_db = ReadDrinkDB()
# #     if drink_name in drink_db['drinks']:
# #         # Set Active Status
# #         status = ReadStatus()
# #         status['status']['active'] = 1
        
# #         print(status['control']['pause'])    
# #         WriteStatus(status)

# #         total_runtime = 0
# #         percent_progress = 0
# #         current_count = 0
# #         global stop_threads

# #         # Initialize Platform Object
# #         settings = ReadSettings()
# #         platform = PumpControl(settings)
# #         if 'percentage' not in settings:
# #             settings['percentage'] = {}

# #         print(f'Starting to prepare {drink_name}')

# #         # Calculate total runtime
# #         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
# #             total_runtime = max(total_runtime, int(pump_runtime * (settings['flowrate'] / 100)))

# #         print(f'Total Runtime: {total_runtime}')

# #         # Create and start threads to dispense each ingredient
# #         pumpThreads = []
# #         for drink_ingredient, pump_runtime in drink_db['drinks'][drink_name]['ingredients'].items():
# #             pump_number = 'none'
# #             for index, value in settings['inventory'].items():
# #                 if value == drink_ingredient:
# #                     pump_number = index
# #                     break  

            
# #             calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
# #             if pump_number == 'pump_16':  # Mixture pump
# #                 delay = 4 #mixture pump pause for 4 seconds
# #                 pump_t = threading.Thread(target=DelayedPour, args=(pump_number, calculated_pump_runtime, platform, delay))
# #             else:
# #                 pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
            
# #             pumpThreads.append(pump_t)
            
# #             consumed_quantity = int(pump_runtime * (settings['flowrate'] / 100))
# #             if pump_number in settings['quantity']:
                
# #                 standard_quantity = settings['quantity'][pump_number]
# #                 settings['in_quantity'][pump_number] = max(0, standard_quantity - consumed_quantity)
                
# #                 # calculation related to find how much % availaible drink 
# #                 # settings['percentage'][pump_number] = (settings['in_quantity'][pump_number] * 100)/standard_quantity
                
                
        

# #         # Start the pump threads
# #         for thread in pumpThreads:
# #             thread.start()

# #         # Monitor and report progress to WebUI
# #         # for x in range(total_runtime):
# #         #     current_count += 1
# #         #     status = ReadStatus()
# #         #     if status['control']['stop'] == 1:
# #         #         stop_threads = True
# #         #         time.sleep(2)
# #         #         stop_threads = False
# #         #         break
# #         #     percent_progress = int((current_count / total_runtime) * 100)
# #         #     status['status']['progress'] = percent_progress
# #         #     WriteStatus(status)
# #         #     time.sleep(1)
# #         for x in range(total_runtime):
# #             if stop_threads:
# #                 break
# #             while pause_threads:
# #                 time.sleep(0.5)  # Wait while paused
# #             current_count += 1
# #             percent_progress = int((current_count / total_runtime) * 100)
# #             status = ReadStatus()
# #             status['status']['progress'] = percent_progress
# #             WriteStatus(status)
# #             time.sleep(1)

# #         # Wait for threads to finish
# #         for thread in pumpThreads:
# #             thread.join()

# #         print('Finished dispensing drink.')
# #         # Write updated settings to file after updating quantities for all pumps
# #         WriteSettings(settings)

# #         print('Finished. Cleaning up status file.')
# #         status['status']['active'] = 0
# #         status['control']['start'] = 0
# #         status['control']['stop'] = 0
# #         WriteStatus(status)
# #     else:
# #         print('Error, no drinks match that name.')
# def PourDrink(drink_name):
#     drink_db = ReadDrinkDB()
#     if drink_name in drink_db['drinks']:
#         # Set Active Status
#         status = ReadStatus()
#         status['status']['active'] = 1
        
#         print(status['control']['pause'])    
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
#                     break  

#             calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
#             if pump_number == 'pump_16':  # Mixture pump
#                 delay = 4  # mixture pump pause for 4 seconds
#                 pump_t = threading.Thread(target=DelayedPour, args=(pump_number, calculated_pump_runtime, platform, delay))
#             else:
#                 pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
            
#             pumpThreads.append(pump_t)
            
#             consumed_quantity = int(pump_runtime * (settings['flowrate'] / 100))
#             if pump_number in settings['quantity']:
#                 standard_quantity = settings['quantity'][pump_number]
#                 settings['in_quantity'][pump_number] = max(0, standard_quantity - consumed_quantity)

#         # Start the pump threads
#         for thread in pumpThreads:
#             thread.start()

#         # Monitor and report progress to WebUI
#         for x in range(total_runtime):
#             if stop_threads:
#                 break
#             while pause_threads:  # Wait while paused
#                 print(f'Progress paused, waiting to resume...')
#                 time.sleep(1)  # Pause progress calculation for 1 second while paused

#             if not pause_threads:  # Only update progress when not paused
#                 current_count += 1
#                 percent_progress = int((current_count / total_runtime) * 100)
#                 status = ReadStatus()
#                 status['status']['progress'] = percent_progress
#                 WriteStatus(status)
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
#                     break  

#             calculated_pump_runtime = max(1, int(pump_runtime * (settings['flowrate'] / 100)))
#             if pump_number == 'pump_16':  # Mixture pump
#                 delay = 4  # mixture pump pause for 4 seconds
#                 pump_t = threading.Thread(target=DelayedPour, args=(pump_number, calculated_pump_runtime, platform, delay))
#             else:
#                 pump_t = threading.Thread(target=Pour, args=(pump_number, calculated_pump_runtime, platform))
            
#             pumpThreads.append(pump_t)

#             consumed_quantity = int(pump_runtime * (settings['flowrate'] / 100))
#             if pump_number in settings['quantity']:
#                 standard_quantity = settings['quantity'][pump_number]
#                 settings['in_quantity'][pump_number] = max(0, standard_quantity - consumed_quantity)

#         # Start the pump threads
#         for thread in pumpThreads:
#             thread.start()

#         # Monitor and report progress to WebUI
#         for x in range(total_runtime):
#             if stop_threads:
#                 break
#             while pause_threads:  # Wait while paused
#                 print(f'Progress paused, waiting to resume...')
#                 time.sleep(1)  # Pause progress calculation for 1 second while paused
                
#             if not pause_threads:  # Only update progress when not paused
#                 current_count += 1
#                 percent_progress = int((current_count / total_runtime) * 100)
#                 status = ReadStatus()
#                 status['status']['progress'] = percent_progress
#                 WriteStatus(status)
#             time.sleep(1)
#         print(pause_threads)
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
# def Pour(pump_number, waitTime, platform):
#     print(f' * Thread: {pump_number} Started for {waitTime} seconds.')
#     platform.ActivatePump(pump_number)
#     for x in range(waitTime):
#         time.sleep(1)
#         global stop_threads
#         if stop_threads:
#             print(f' * Thread: {pump_number} cancelling.')
#             break
#         while pause_threads:
#             print(f' * Thread: {pump_number} paused. Waiting to resume...')
#             time.sleep(1)  # Pause while `pause_threads` is True
#         time.sleep(1)
#     platform.DeActivatePump(pump_number)
#     print(f' * Thread: {pump_number} finished.')
####################################

# def MixerControl(platform, delay=5, start_percentage=50):
   
#     global stop_threads, pause_threads
    
#     print(f" * MixerControl: Starting mixer at {start_percentage}% progress.")
#     platform.ActivatePump("pump_16")  

#     while True:
#         status = ReadStatus()
#         progress = status['status']['progress']
        
#         if progress >= 100 or stop_threads:
#             break
#         while pause_threads:
#             print(f" * MixerControl: Mixer paused. Waiting to resume...")
#             time.sleep(1)
#         time.sleep(1)  
    
#     print(" * MixerControl: Reached 100% progress. Continuing mixer for additional seconds.")
#     time.sleep(delay)  
#     platform.DeActivatePump("pump_16")  
#     print(" * MixerControl: Mixer finished.")


# def PourDrink(drink_name):
#     drink_db = ReadDrinkDB()
#     if drink_name in drink_db['drinks']:
#         status = ReadStatus()
#         status['status']['active'] = 1
#         WriteStatus(status)

#         total_runtime = 0
#         current_count = 0
#         global stop_threads

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

#         # Start MixerControl in a separate thread
#         mixer_thread = threading.Thread(target=MixerControl, args=(platform,))
#         mixer_thread.start()

#         for x in range(total_runtime):
#             current_count += 1
#             status = ReadStatus()
#             if status['control']['stop'] == 1:
#                 stop_threads = True
#                 time.sleep(2)
#                 stop_threads = False
#                 break

#             if status['control']['pause'] == 1:
#                 percent_progress = int((current_count / total_runtime) * 100)
#                 status['status']['progress'] = percent_progress
#                 WriteStatus(status)
#                 while status['control']['pause'] == 1:
#                     time.sleep(1)
#                     status = ReadStatus() 

#             percent_progress = int((current_count / total_runtime) * 100)
#             status['status']['progress'] = percent_progress
#             WriteStatus(status) 
#             time.sleep(1)

#         # Wait for all pump threads to finish
#         for thread in pumpThreads:
#             thread.join()

#         # Wait for mixer thread to finish
#         mixer_thread.join()

#         print("Finished dispensing drink.")
#         WriteSettings(settings)

#         print("Finished. Cleaning up status file.")
#         status['status']['active'] = 0
#         status['control']['start'] = 0
#         status['control']['stop'] = 0
#         WriteStatus(status)
#     else:
#         print("Error, no drinks match that name.")

# import RPi.GPIO as GPIO

# class PumpControl:
# 	def __init__(self, settings):
# 		# Init GPIO's to default values / behavior
# 		GPIO.setwarnings(False)
# 		GPIO.setmode(GPIO.BCM)
# 		self.pump_pins = {}
# 		for pump_number, pin_number in settings['assignments'].items():
# 			# GPIO.setup(pin_number, GPIO.OUT, initial=1)
# 			GPIO.setup(pin_number, GPIO.OUT, initial=GPIO.HIGH)
# 			self.pump_pins[pump_number] = pin_number
# 			print(f"Pin number {pin_number} initialized as output for {pump_number}.  Set to 1. ")

# 	def ActivatePump(self, pump_number):
# 		# GPIO.output(self.pump_pins[pump_number], 0) # Turn on Relay
# 		GPIO.output(self.pump_pins[pump_number], GPIO.LOW) # Turn on Relay
# 		print(f"{pump_number} Pump Activated. Dispensing on pin: {self.pump_pins[pump_number]}")

# 	def DeActivatePump(self, pump_number):
# 		# GPIO.output(self.pump_pins[pump_number], 1) # Turn off Relay
# 		GPIO.output(self.pump_pins[pump_number], initial=GPIO.HIGH) # Turn off Relay
# 		print(f"{pump_number} Pump De-Activated. Stopped Dispensing on pin: {self.pump_pins[pump_number]}")

# 	def GetOutputStatus(self):
# 		self.current = {}
# 		for pump_number in self.pump_pins.items():
# 			self.current[pump_number] = GPIO.input(self.pump_pins[pump_number])
# 		return self.current

# 	def Cleanup(self):
# 		GPIO.cleanup()

# /* keyboard modal */
# /* .keyboard-container {
#     position: absolute;
#     bottom: 10%;
#     left: 40%;
#     background-color: gray;
#     text-align: center;
#     display: flex;
#     justify-content: center;
# }

# .keyboard {
#     display: flex;
#     flex-direction: column;
#     gap: 5px;
#     padding-left: 17px;
#     padding-right: 17px;
#     padding: 7px 25px;
#     background-color: #F2F2F2;
# }

# .row {
#     display: flex;
#     gap: 5px;
# }

# .key {
#     padding: 10px 16px;
#     border: 1px solid #ccc;
#     background-color: #f9f9f9;
#     border-radius: 5px;
#     font-size: 18px;
#     text-align: center;
#     cursor: pointer;
#     user-select: none;
# }

# .key:hover {
#     background-color: #ddd;
# }

# .key.space {
#     flex: 1;
# }

# .key.capslock.active,
# .key.shift.active {
#     background-color: #4caf50;
#     color: white;
# }

# .shift,
# .enter {
#     padding: 10px 20px;
# } */

	# <script>

	# 	setTimeout(function () {
	# 		var alertmessage = document.getElementById('alertMessage')
	# 		alertmessage.classList.add('hidden');
	# 		alertmessage.classList.remove("show-message");
	# 	}, 5000);

	# 	document.addEventListener('DOMContentLoaded', function () {
	# 		const quantityData = JSON.parse(document.getElementById('quantity-data').textContent);

	# 		function updateProgress(pumpNumber, quantity) {
	# 			const progressBar = document.getElementById(`progress_${pumpNumber}`);

	# 			if (progressBar) {
	# 				const percentage = (quantity / 1000) * 100;

	# 				progressBar.style.width = `${percentage}%`;

	# 				if (quantity <= 100) {
	# 					progressBar.style.backgroundColor = 'red';
	# 				} else if (quantity <= 200) {
	# 					progressBar.style.backgroundColor = 'orange';
	# 				} else {
	# 					progressBar.style.backgroundColor = 'green';
	# 				}

	# 				// Update the percentage text inside the progress bar
	# 				progressBar.innerText = `${Math.round(percentage)}%`;
	# 				progressBar.setAttribute('aria-valuenow', Math.round(percentage));
	# 			}
	# 		}

	# 		// Loop through each pump's quantity and update the progress bar
	# 		Object.entries(quantityData).forEach(([pumpNumber, quantity]) => {
	# 			updateProgress(pumpNumber, quantity);
	# 		});
	# 	});


	# </script>
 
 
 
# def ReadStatus():
#     if not os.path.exists("status.json"): 
#         print("Error: status.json file not found. Creating a new one.")
#         return create_default_status()

#     try:
#         with open("status.json", "r") as json_data_file:
#             json_data_string = json_data_file.read().strip()

#         status = json.loads(json_data_string)
#         return status  
    
#     except (IOError, OSError):
#         print("Error: Unable to read status.json file. Creating a new one.")
#         # status = create_default_status()

#     except (ValueError, json.JSONDecodeError) as e:
#         print(f"Error: Invalid JSON in status.json. Creating a new one. Details: {e}")
#     status = create_default_status()
#     return status  
# // intervalId = setInterval(async () => {
#   //   try {
#   //     const ir_sensor_response = await fetch("/ir-sensor-detection");
#   //     const data = await ir_sensor_response.json();
#   //     console.log(data);

#   //     const proceedButton = document.querySelector(".btn-proceed");
#   //     if (!proceedButton) return;
#   //     console.log(data.sensor_results);

#   //     if (data.sensor_results === 0) {
#   //       proceedButton.disabled = true;
#   //       proceedButton.style.setProperty(
#   //         "background-color",
#   //         "#F5EFF2",
#   //         "important"
#   //       );
#   //       proceedButton.style.setProperty("color", "#D5BFCD", "important");
#   //       proceedButton.style.cursor = "not-allowed";
#   //     } else {
#   //       proceedButton.disabled = false;
#   //       proceedButton.style.cursor = "pointer";
#   //       proceedButton.style.setProperty(
#   //         "background-color",
#   //         "#E5D7DF",
#   //         "important"
#   //       );
#   //     }
#   //   } catch (error) {
#   //     console.error("Error checking IR sensor:", error);
#   //   }
#   // }, 500);

# def timenow():
#     while True:
#         current_time = datetime.now().strftime("%H:%M:%S")
#         sio.emit("current_time", current_time)
#         time.sleep(1)  

#  threading.Thread(
#         target=timenow,
#         daemon=True,
#         name=f"current-time"
#     ).start()

# import socketio
# from common import *
# from network import *
# from version import __system_id__,__system_name__

# sio = socketio.Client(
#     logger=True,
#     engineio_logger=True,
#     reconnection=True,
#     reconnection_attempts=5,
#     reconnection_delay=1,
#     reconnection_delay_max=5
# )

# CLIENT_PORT =  5000
# SERVER_PORT = 5500

# moniterData = MoniterDB()

# CONSUMPTION_FILE = "moniter_db.json"

# last_modification_file = 0

# POLLING_FALLBACK =  'true'  

# def get_server_ip():
#     cache_ip = load_ip()
#     metadata = ReadMetadata()
    
#     if cache_ip and try_connect(cache_ip):
#         return cache_ip

#     print("📡 Discovering server...")
#     while True:
#         ip = find_server()
#         if ip:
#             metadata['server-config']['ip'] = ip
#             metadata['server-config']['last_connected_at'] = datetime.datetime.now()
#             WriteMetadata()
#             save_current_ip(ip)
#             return ip
#         time.sleep(3)
        
# SERVER_IP = get_server_ip() 
# SERVER_URL = f"http://{SERVER_IP}:{SERVER_PORT}"
# print(f"Server IP {SERVER_IP} , Full Address {SERVER_URL}")

# def start_socket_client():
#     """Improved connection handler with multiple fallback options"""
#     transports = ['websocket']
#     if POLLING_FALLBACK:
#         transports.append('polling')

#     while True:
#         try:

#             print(f"[{SERVER_IP}] Connecting to {SERVER_URL} (transports: {', '.join(transports)})")
#             sio.connect(
#                 SERVER_URL,
#                 transports=transports,
#                 headers={'X-Device-ID': SERVER_IP},
#                 namespaces=['/'],
#                 wait_timeout=10
#             )
#             sio.wait()

#         except (socketio.exceptions.ConnectionError, Exception) as e:
#             print(f"[{SERVER_IP}] Connection failed: {str(e)}")
#             print(f"Retrying in 5 seconds...")
#             time.sleep(5)
            
# def watch_consumption_file(interval = 2):
#         global last_modification_file
#         while True:
#             try:
#                 current_mtime = os.path.getmtime(CONSUMPTION_FILE)
#                 if current_mtime != last_modification_file:
#                     last_modification_file = current_mtime
#                     print("[INFO] Detected JSON change, emitting data...")
#                     data = MoniterDB()
#                     sio.emit('consumption_update', {"machine_id":__system_id__,"drink_consumed":data.read()})
#             except FileNotFoundError:
#                 print("[WARN] consumption file not found")
#             except Exception as e:
#                 print(f"[ERROR] Watching file: {e}")
#             time.sleep(interval)    
# @sio.event
# def connect():
#     print(f"[{SERVER_IP}] Connected to dashboard at {SERVER_URL}")
   
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
#     print(f"[{SERVER_IP}] Disconnected from server")

# @sio.event
# def reconnect():
#     print(f"[{SERVER_IP}] Reconnected to server")

# @sio.on('sendNotification')
# def send_consumption(drinks):
#     sio.emit('sendNotification', {"machine_id":__system_id__,"data":drinks})
# import socket
# import os,time,json,requests
# import datetime

# MONITOR_CACHE_FILE = "monitor_cache.json"
# def save_current_ip(ip):
#     with open(MONITOR_CACHE_FILE,"w") as f:
#         json.dump({
#             "server_ip": ip,
#             "last_seen": datetime.datetime.now()
#         }, f,default=str, indent=4)
    
        
# def load_ip():
#     if os.path.exists(MONITOR_CACHE_FILE):
#         with open(MONITOR_CACHE_FILE,'r') as f:
#             return json.load(f).get("server_ip")
#     return None 

# def try_connect(ip, timeout=2):
#     try:
#         requests.get(f"http://{ip}:5500", timeout=timeout)
#         return True
#     except:
#         return False
    
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


# def start_threads():
#     threading.Thread(target=start_socket_client, daemon=True).start()
#     threading.Thread(target=watch_consumption_file, daemon=True).start()

# if os.environ.get("RUN_BACKGROUND") == "true":
#     start_threads()