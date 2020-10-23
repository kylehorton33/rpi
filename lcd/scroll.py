from RPLCD.i2c import CharLCD
import time

framebuffer = [
    'Hello!',
    '',
]

def write_to_lcd(lcd, framebuffer, num_cols):
    """Write the framebuffer out to the specified LCD."""
    lcd.home()
    for row in framebuffer:
        lcd.write_string(row.ljust(num_cols)[:num_cols])
        lcd.write_string('\r\n')

lcd = CharLCD(pin_rs=36, pin_e=38, pins_data=[31, 33, 35, 37],
              numbering_mode=GPIO.BOARD,
              cols=16, rows=2, dotsize=8,
              auto_linebreaks=True, compat_mode=True)
write_to_lcd(lcd, framebuffer, 16)

long_string = '                This string is too long to fit                '

def loop_string(string, lcd, framebuffer, row, num_cols, delay=0.2):
    padding = ' ' * num_cols
    s = padding + string + padding
    for i in range(len(s) - num_cols + 1):
        framebuffer[row] = s[i:i+num_cols]
        write_to_lcd(lcd, framebuffer, num_cols)
        time.sleep(delay)

while True:
    loop_string(long_string, lcd, framebuffer, 1, 16)