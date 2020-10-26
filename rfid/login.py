import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import datetime
import time
import csv

reader = SimpleMFRC522()

with open('users/users.csv', mode='r') as infile:
    csv_reader = csv.reader(infile)
    users = {rows[0]:rows[1] for rows in csv_reader}

while(True):
  print("scan badge to login")
  try:
    id_, text = reader.read()
    now = datetime.datetime.now()

    if id_ in users:
      print(f"\n\tHello, {users[id_]}")
      print(f"\tScanned {users[id_]} at {now}\n")
      time.sleep(2)
    elif id:
      print("\n\tUser not recognized")
      time.sleep(2)

  finally:
    print("\tsomething went wrong...")
    time.sleep(2)
    GPIO.cleanup()