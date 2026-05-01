import time
import subprocess # Use this instead of webbrowser
import os
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def RFID():
    reader = SimpleMFRC522()
    allowed_cards  = {
        114974733805,
        114974733806,
        114974733807,
        114974733808,
        114974733809,
        114974733810,
    }

    inventory_url = "http://localhost/inventory"
    default_url = "https://www.google.com"
    print("Waiting for an RFID tag...")

    last_tag_id = None

    # --- NEW BROWSER LOGIC ---
    # Explicitly tell the OS to use the primary display screen
    my_env = os.environ.copy()
    my_env["DISPLAY"] = ":0" 

    try:
        while True:
            try:
                tag_id, text = reader.read()
                print(f"\nTag ID detected: {tag_id}")
            except Exception as e:
                print(f"Error reading RFID tag: {e}")
                continue

            if tag_id == last_tag_id:
                print("Same tag detected again. Ignoring to prevent multiple triggers.")
                continue

            last_tag_id = tag_id
            
            if tag_id in allowed_cards:
                target_url = inventory_url
                print(f"Tag ID {tag_id} recognized. Opening {target_url} page.")
            else:
                target_url = default_url
                print(f"Tag ID {tag_id} not recognized. Opening {target_url} page.")
                last_tag_id = None
                continue
            
            # Force Chromium to open the URL in a new tab
            subprocess.Popen(['/usr/bin/chromium', target_url], env=my_env)
            time.sleep(3)
            last_tag_id = None
            print("\nReady for the next tag...")
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
    finally:
        GPIO.cleanup()
