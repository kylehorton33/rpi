# https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

## Pinout
# Vcc - Pin 2 (GPIO 5V)
# TRIG - Pin 16 (GPIO 23)
# ~ output of ECHO through a voltage bridge
# ECHO - R1 1k - Pin 18 (GPIO 24) - R2 2k - Pin 6 (GPIO GND)
# GND - Pin 6 (GPIO GND)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print("Distance measurement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.0001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == 0:
  pulse_start = time.time()

while GPIO.input(ECHO) == 1:
  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start
distance= round(pulse_duration * 17150, 2)

print(f"Distance: {distance} cm")

GPIO.cleanup()
