import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object
i2c = board.I2C()
count = 0
btn = DigitalInOut(board.D7)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
cur_state = True
prev_state = True
buttonPress = 0 # making an integer for the count of the button presses to be stored in

while True:
    cur_state = btn.value # the current state is the buttons' value
    if cur_state != prev_state: # if it's not the current state, it's the previous state
        if not cur_state: # if not current state then do the following:
            buttonPress = buttonPress + 1 # the count of the button goes up by 1
            lcd.clear() # clears the screen after stating the button count
            lcd.set_cursor_pos(0, 0)

            lcd.set_cursor_pos(1, 0) # setting where the lcd is going to print the text
  
            lcd.print(str(buttonPress)) # on the lcd, print the amount of button press
        else:
            lcd.clear()
            lcd.print("BTN is up") # when the button isn't pressed state "BTN is up"

    prev_state = cur_state # previous state equals the current state
