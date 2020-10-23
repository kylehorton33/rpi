import cv2
import os
import time
import datetime


cap = cv2.VideoCapture(0)
start = datetime.datetime.now()

TIME_DELAY = 1

os.chdir('frames')
FRAME_FOLDER = start.strftime('%Y-%m-%d (%H.%M %p)')
os.mkdir(FRAME_FOLDER)
os.chdir(FRAME_FOLDER)

while(True):
  ret, img = cap.read()
  ts = datetime.datetime.now()
  cv2.imwrite(ts.strftime('%Y-%m-%d (%H.%M.%S %p).jpg'), img)

  time.sleep(TIME_DELAY)

  if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()