import RPi.GPIO as GPIO
import time
import os
import psutil  

FAN_PIN = 18  
MAX_TEMP = 75 
MAX_CPU = 70 

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)

def get_cpu_temp():
    res = os.popen('vcgencmd measure_temp').readline()
    return float(res.replace("temp=","").replace("'C\n",""))

def get_cpu_usage():
    return psutil.cpu_percent(interval=1) 

def main():
    try:
        while True:
            temp = get_cpu_temp()
            cpu = get_cpu_usage()

            print(f"Temp: {temp}°C | CPU: {cpu}%")

            if temp > MAX_TEMP or cpu > MAX_CPU:
                GPIO.output(FAN_PIN, True)   # Fan ON
            else:
                GPIO.output(FAN_PIN, False)  # Fan OFF

            time.sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        
if __name__=="__main__":
    main()