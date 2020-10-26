import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import datetime
import time

reader = SimpleMFRC522()

import csv

with open('users/users.csv', mode='r') as infile:
    reader = csv.reader(infile)
    users = {rows[0]:rows[1] for rows in reader}

id = 0
while not id:
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
  id = 0
  else:
    print("\tsomething went wrong...")
    time.sleep(2)
    pass