# https://rplcd.readthedocs.io/en/latest/getting_started.html
from RPLCD.i2c import CharLCD
import datetime

## Pinout
# GND - Pin 6
# VCC - Pin 4
# SDA - Pin 3
# SCL - Pin 5

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=False,
              backlight_enabled=True)

lcd.cursor_pos = (0,0)
lcd.write_string("Current Time:")

while(True):
  now = datetime.datetime.now()
  lcd.cursor_pos = (1,0)
  lcd.write_string(now.strftime("%b-%d %H:%M:%S"))

