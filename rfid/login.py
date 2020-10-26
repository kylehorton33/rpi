import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

while(True):
  print("scan badge to login")
  try:
          id, text = reader.read()
          if id == 148475360341:
            print("user1")
          else if id == 727376181428:
            print("user2")
          else if id:
            print("user not recognized")
  finally:
          GPIO.cleanup()