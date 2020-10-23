import cv2
import datetime
from time import sleep
import os

folders = os.listdir('frames')

# set frame rate
FPS = 30
SKIP_FRAMES = 1
TARGET_LENGTH = 15

for folder in folders:
  files = os.listdir('frames/' + folder)

  file_name = f'video/{folder}.avi' #f'video/{files[0][:-4]} to {files[-1][:-4]}.avi'
  print(f'Making video: {file_name}')
  print(f'{len(files)} clips in {round(len(files)/FPS, 2)} s')
  writer = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*"XVID"), FPS, (640, 480))

  font = cv2.FONT_HERSHEY_SIMPLEX 
  org = (20, 420) 
  fontScale = 0.6
  color = (0, 0, 255) 
  thickness = 2

  for file in files[::SKIP_FRAMES]:
    frame_path = os.path.join('frames',folder,file)
    frame = cv2.imread(frame_path)
    #ts = f'{file[0:8]} {file[9:11]}:{file[12:14]}:{file[15:17]}'

    #img = cv2.putText(frame, ts, org, font, fontScale, color, thickness, cv2.LINE_AA)
    
    writer.write(frame)
    #os.remove('pics/'+file)
  writer.release()