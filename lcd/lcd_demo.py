# https://rplcd.readthedocs.io/en/latest/getting_started.html
from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=False,
              backlight_enabled=True)

lines = [
  "abcdefghijklmnop123",
  "It works! but you can't see the rest of the text"
]

for i,line in enumerate(lines):
  char_count = len(line)
  #print(char_count)
  if char_count > 16:
    print(f"The message on LINE {i} is too long to display!")
    print(f"Only displaying:\t\'{line[0:16]}\'")
    print(f"Should see:\t\t\'{line}\'")
  lcd.cursor_pos = (i,0)
  lcd.write_string(line)
