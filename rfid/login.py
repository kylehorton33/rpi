import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import datetime
import time

reader = SimpleMFRC522()

users = {
  148475360341: "kate",
  727376181428: "kyle",
}

while(True):
  print("scan badge to login")
  try:
    id, text = reader.read()
    now = datetime.datetime.now()

    if id in users:
      print(f"\n\tHello, {users[id]}")
      print(f"\tScanned {users[id]} at {now}\n")
      time.sleep(2)
    elif id:
      print("\n\tUser not recognized")
      time.sleep(2)
  except:
    print("\tsomething went wrong...")
    time.sleep(2)
    exit()