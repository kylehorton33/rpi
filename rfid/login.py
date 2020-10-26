import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import datetime
import time

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
      time.sleep(2)
    elif id:
      print("User not recognized")
      time.sleep(2)
  except:
    print("something went wrong...")
    time.sleep(2)
    exit()