import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import datetime
import time

reader = SimpleMFRC522()

try:
  id, text = reader.read()
  now = datetime.datetime.now()


except:
  print("\tsomet
