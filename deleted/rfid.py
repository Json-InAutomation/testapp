import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import webbrowser
reader = SimpleMFRC522()
card_detected = False

def start_rfid(on_card_detected):
    global card_detected
    try:
        while True:
            uid, text = reader.read_no_block()
            
            if uid:
                card_detected  = True
                print(f"Card detected {uid}")
                on_card_detected(uid)
                time.sleep(1.5)  
            else:
                card_detected = False
            time.sleep(0.3)
            
    except Exception as e:
        print(f'RFID Error {e}')
    finally:
        GPIO.cleanup()
        

