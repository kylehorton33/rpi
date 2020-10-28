import sys

fp = open('/dev/hidraw0', 'rb')
tStr = ''
while True:
  buffer = fp.read(8)
  for c in buffer:
    tStr = tStr + c

print(tStr + "\n")