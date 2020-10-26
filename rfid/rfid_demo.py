## https://pimylifeup.com/raspberry-pi-rfid-rc522/

## Pinout
# SDA connects to Pin 24.
# SCK connects to Pin 23.
# MOSI connects to Pin 19.
# MISO connects to Pin 21.
# GND connects to Pin 6.
# RST connects to Pin 22.
# 3.3v connects to Pin 1.

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()