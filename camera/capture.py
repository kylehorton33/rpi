import cv2
import os
import time
import datetime
import sys


cap = cv2.VideoCapture(0)
ret, img = cap.read()
if not ret:
  exit()

start = datetime.datetime.now()

if len(sys.argv) == 2:
  TIME_DELAY = int(sys.argv[1])
else:
  TIME_DELAY = 5

os.chdir('frames')
FRAME_FOLDER = start.strftime('%Y-%m-%d (%H.%M %p)')
try:
  os.mkdir(FRAME_FOLDER)
except:
  FRAME_FOLDER += '2'
  os.mkdir(FRAME_FOLDER)

os.chdir(FRAME_FOLDER)

frame_counter = 1
while(True):
  ret, img = cap.read()
  ts = datetime.datetime.now()
  cv2.imwrite(ts.strftime('%Y-%m-%d (%H.%M.%S %p).jpg'), img)
  print(f'{ts}: Generated {frame_counter} frames\r', end="")
  frame_counter += 1

  time.sleep(TIME_DELAY)

  if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
