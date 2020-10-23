# https://rplcd.readthedocs.io/en/latest/getting_started.html
from RPLCD.i2c import CharLCD
import time

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=False,
              backlight_enabled=True)

while(True):
  lcd.cursor_pos = (0,0)
  lcd.write_string("Enter something")
  lcd.cursor_pos = (1,0)
  lcd.cursor_mode = 'blink'
  entry = input()
  lcd.write_string(entry)
  time.sleep(3)
