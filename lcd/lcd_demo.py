# https://rplcd.readthedocs.io/en/latest/getting_started.html
from RPLCD.i2c import CharLCD
import re

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

lines = [
  "abcdefghijklmnop123\r\n",
  "It works!"
]

for line in lines:
  char_count = len(re.findall('[a-zA-Z]',line))
  print(char_count)
  if char_count > 16:
    print(f"The message \'{line}\' is too long to display!")
  lcd.write_string(line)
