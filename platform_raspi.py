#!/usr/bin/env python3
# *****************************************
# PiTender RaspberryPi Interface Library
# *****************************************
#
# Description: This library supports controlling the PiTender outputs via
#  Raspberry Pi GPIOs
#
# *****************************************

# *****************************************
# Imported Libraries
# *****************************************

import RPi.GPIO as GPIO
import time
from common import *
control_logger = CustomLogger(
                    name="CONTROL",
                    out_file="control.out.log",
                    err_file="control.err.log")

class PumpControl:
	def __init__(self, settings):
		# Init GPIO's to default values / behavior
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		self.pump_pins = {}
		for pump_number, pin_number in settings['assignments'].items():
			GPIO.setup(pin_number, GPIO.OUT, initial=1)
			self.pump_pins[pump_number] = pin_number
			print(f"Pin number {pin_number} initialized as output for {pump_number}.  Set to 1. ")
			control_logger.info(f"Pin number {pin_number} initialized as output for {pump_number}.Set to 1. ")

	def ActivatePump(self, pump_number):
		GPIO.output(self.pump_pins[pump_number], 0) # Turn on Relay
		print(f"{pump_number} Pump Activated. Dispensing on pin: {self.pump_pins[pump_number]}")
		control_logger.info(f"{pump_number} Pump Activated. Dispensing on pin: {self.pump_pins[pump_number]}")

	def DeActivatePump(self, pump_number):
		GPIO.output(self.pump_pins[pump_number], 1) # Turn off Relay
		print(f"{pump_number} Pump De-Activated. Stopped Dispensing on pin: {self.pump_pins[pump_number]}")
		control_logger.info(f"{pump_number} Pump De-Activated. Stopped Dispensing on pin: {self.pump_pins[pump_number]}")

	def GetOutputStatus(self):
		self.current = {}
		for pump_number in self.pump_pins.items():
			self.current[pump_number] = GPIO.input(self.pump_pins[pump_number])
		return self.current

	def Cleanup(self):
		GPIO.cleanup()

class SensorSignal:
    def __init__(self, settings):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.ir_sensor_pin = settings["ir_sensor"]["gpio_pin"]
        GPIO.setup(self.ir_sensor_pin, GPIO.IN) 

    def detectObject(self, settings):
        stripControl = LEDStripControl('OneStripNeopixel.py')
        try:
            while True:
                if GPIO.input(self.ir_sensor_pin) == GPIO.LOW:
                    stripControl.startStrip()
                    settings["ir_sensor"]["detection"] = True
                    settings["ir_sensor"]["isDetected"] = 1
                else:
                    stripControl.stopStrip()
                    settings["ir_sensor"]["detection"] = False
                    settings["ir_sensor"]["isDetected"] = 0

                WriteSettings(settings)
                time.sleep(0.1)
                return settings 

        except KeyboardInterrupt:
            print("Detection stopped")

        finally:
            GPIO.cleanup()
       