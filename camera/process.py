import cv2
import datetime
import os

folders = os.listdir('frames')
os.chdir('frames')

# set frame rate
FPS = 30
SKIP_FRAMES = 1
TARGET_LENGTH = 15


for folder in folders:
  files = os.listdir(folder)
  os.chdir(folder)
  sorted_files = sorted(files, key=os.path.getmtime)
  os.chdir('../..')
  file_name = f'video/{folder}.avi'
  print(f'Making video: {file_name}')
  print(f'{len(files)} clips in {round(len(files)/FPS, 2)} s')
  writer = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*"XVID"), FPS, (640, 480))

  for file in sorted_files[::SKIP_FRAMES]:
    frame_path = os.path.join('frames',folder,file)
    frame = cv2.imread(frame_path)
    print(file)

    writer.write(frame)

  writer.release()
