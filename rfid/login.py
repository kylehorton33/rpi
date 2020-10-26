import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import datetime

reader = SimpleMFRC522()

users = {
  148475360341: "user1",
  727376181428: "user2",
}

while(True):
  print("scan badge to login")
  try:
          id, text = reader.read()
          now = datetime.datetime.now()

          if id in users:
            print(f"Scanned {users[id]} at {now}")
          elif id:
            print("user not recognized")
