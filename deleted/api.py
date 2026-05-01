from flask import  Blueprint, request,jsonify
from common import *
from version import __version__,__system_name__
import platform
import socket
from datetime import datetime
mApiExpose = Blueprint("api",__name__,url_prefix='/api')

@mApiExpose.route('/analytic/consumption/<checkInDate>',methods = ['GET'])
def monitorAnalytic(checkInDate):
    try: 
        is_default_load = request.args.get('pageload', 'false').lower() == 'true'
        monitor = MoniterDB()
        
        checkInDateFormate = datetime.strptime(checkInDate,'%Y-%m-%d %H:%M') 
        todayDate = datetime.now()
        
        conumption = monitor.read().get('insight',{})
        drinks = conumption.get('consumeDrink',{})
        if not drinks or drinks == '{}' or drinks == '[]':
            return {"status":200, "response":"No Drink"}

        filtered_drinks = []
        print(filtered_drinks)
        for drinkName, drinkData in drinks.items():
            last_consumed_string = drinkData.get('lastConsumedOn')
            if not last_consumed_string:
                continue
            try:
                last_consumed_on = datetime.strptime(last_consumed_string, "%Y-%m-%d %H:%M:%S")
            except:
                continue
            
            if is_default_load:
                print(last_consumed_on.date())
                filtered_drinks.append({
                    "drinkName": drinkName,
                    "lastConsumedOn": last_consumed_string,
                    "consumeCount": drinkData.get('consumeCount', 0)
                })
            else:
                print(filtered_drinks)
                if checkInDateFormate <= last_consumed_on <= todayDate:
                    filtered_drinks.append({
                        "drinkName": drinkName,
                        "lastConsumedOn": last_consumed_string,
                        "consumeCount": drinkData.get('consumeCount', 0)
                    })
                print(f'Within selected {checkInDateFormate.date()} filtered drinks are {filtered_drinks}')

        filtered_drinks.sort(
            key=lambda x: datetime.strptime(x['lastConsumedOn'], "%Y-%m-%d %H:%M:%S"),
            reverse=True
        )
        
        if is_default_load:
            print(is_default_load)
            filtered_drinks = filtered_drinks[:5]

        return jsonify({
            "status": 200,
            "response": filtered_drinks if filtered_drinks else "No Drink Found"
        })

    except Exception as error:
        print("Error while fetching insight:", error)
        return jsonify({
            "status":500,
            "message": f"While fetching insight got error {str(error)[:50]}"
        })

@mApiExpose.route('/analytic/ingridient',methods = ['GET'])
def monitorAnalyticIngridient():
    try:
        monitor = MoniterDB()
        ingridient = monitor.read()['ingridient']
        return jsonify({"status":200,"response":ingridient})
    except Exception as error:
        print("Error while fetching ingridient")
        return jsonify({"status":500,"message":f"While fetching ingridient got error {str(error[:50])}"})

@mApiExpose.route('/version')
def get_version():
    return jsonify({
        "system_name": __system_name__,
        "version": __version__,
    })
    
@mApiExpose.route("/system",methods=['GET'])
def systemInfo():
    return  jsonify({
        "system_name":__system_name__,
        "version":__version__,
        "os":platform.system(),
        'hostname':socket.gethostname()
    })