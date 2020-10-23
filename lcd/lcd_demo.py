# https://rplcd.readthedocs.io/en/latest/getting_started.html
from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

lines = [
  "Testing...\n",
  "It works!"
]

for line in lines:
  if len(line) > 16:
    print(f"The message \'{line}\' is too long to display!")
  lcd.write_string(line)