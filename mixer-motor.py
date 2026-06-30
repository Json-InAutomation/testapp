#!/usr/bin/env python3

import time

from platform_raspi import *
from common import *

def run_mixer(duration=10):
    settings = ReadSettings()
    platform = PumpControl(settings)

    mixer_pump = "pump_16"

    try:
        print(f"Starting mixer ({mixer_pump}) for {duration} seconds...")
        platform.ActivatePump(mixer_pump)

        time.sleep(duration)

    except KeyboardInterrupt:
        print("Interrupted by user.")

    finally:
        platform.DeActivatePump(mixer_pump)
        print("Mixer stopped.")

if __name__ == "__main__":
    run_mixer(10)