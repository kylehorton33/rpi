from RPLCD.i2c import CharLCD
import time
import speech_recognition as sr
import sys
import datetime

# Hide Errors
sys.tracebacklimit = 0

r = sr.Recognizer()
mic = sr.Microphone()


lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=False,
              backlight_enabled=True)

def write_to_lcd(lcd, framebuffer, num_cols):
    """Write the framebuffer out to the specified LCD."""
    lcd.home()
    for row in framebuffer:
        lcd.write_string(row.ljust(num_cols)[:num_cols])
        lcd.write_string('\r\n')


def loop_string(string, lcd, framebuffer, row, num_cols, delay=0.2):
    padding = ' ' * num_cols
    s = padding + string + padding
    for i in range(len(s) - num_cols + 1):
        framebuffer[row] = s[i:i+num_cols]
        write_to_lcd(lcd, framebuffer, num_cols)
        time.sleep(delay)

def get_audio():
  print("getting audio...")
  with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

  response = {
    "success" : True,
    "error" : None,
    "transcription" : None
  }

  try:
    response["transcription"] = r.recognize_google(audio)
    return response["transcription"]
  except sr.RequestError:
    # API was unreachable or unresponsive
    response["success"] = False
    response["error"] = "API unavailable"
    print(response)
    return 0
  except sr.UnknownValueError:
    # speech was unintelligible
    response["error"] = "Unable to recognize speech"
    print(response)
    return 0


framebuffer = [
    'Recorded:',
    '',
]

while(True):
  lcd.clear()
  lcd.cursor_pos = (0,0)
  lcd.write_string("Press r+Enter...")

  entry = input("")
  if entry == 'r':
    lcd.clear()
    lcd.cursor_pos = (0,0)
    lcd.write_string("Recording...")

    response = get_audio()
    print(response)
    if response:
      loop_string(response, lcd, framebuffer, 1, 15)
      with open('logs/audio.txt','a') as f:
        f.write(f'{datetime.datetime.now()},{response}\n')

    entry = None



