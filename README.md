# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
The neopixel blinks with the color of my choice.
Here's how you make code look like code:

```python
import board
import neopixel
import time


dot = neopixel.NeoPixel(board.NEOPIXEL, 1) # connects neopixel to CircuitPython
dot.brightness = 0.1 # how bright the pixel is

print("Make it red!") # printing on monitor

while True:
    R = 0 # no red
    G = 90 # mostly green
    B = 20 # some blue
    time.sleep(1)
    dot.fill((R, G, B))
    time.sleep(1)
    dot.fill((0, 0, 0))
    print("R:",R," G:", G," B:",B)

```


### Evidence


file:///C:/Users/schen12/Pictures/Camera%20Roll/WIN_20220912_15_26_30_Pro.mp4


### Wiring
No wiring, coding for the Metro.

### Reflection
I learned that CircuitPython is very different from C++. I didn't really understand how the code worked, and had a lot fo help from my teacher. I did, however, get a better understanding of why we had to download so many files to get out code running.


## CircuitPython_Servo

### Description & Code
I can code the servo to move.
```python
"""CircuitPython Essentials Servo standard servo example"""
import time #necessary for making the sleep function (o.5)
import board #connects board to code
import pwmio 
from adafruit_motor import servo #imports the servo


pwm = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50) #line tells board where to put power


my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5): #power intervals
        my_servo.angle = angle
        time.sleep(0.05) #pauses for 0.05 seconds
    for angle in range(180, 0, -5): 
        time.sleep(0.05) #pauses for 0.05 seconds

```

### Evidence

file:///C:/Users/schen12/Pictures/Camera%20Roll/WIN_20220927_15_07_00_Pro.mp4
### Wiring
https://www.tinkercad.com/things/16a7UBZ3Cle-neat-gogo-blad/editel?tenant=circuits
### Reflection

The servo was difficult to code because I didn't know how or why I needed to download files to write functioning code.


## CircuitPython_LCD

### Description & Code
The LCD displays the count according to how many times the button is clicked.
```python
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

```

### Evidence
file:///C:/Users/schen12/Pictures/Camera%20Roll/WIN_20220923_15_34_47_Pro.mp4

### Wiring
https://www.tinkercad.com/things/d6I0Mx941Rc-tremendous-snicket-krunk/editel?tenant=circuits
### Reflection

I learned that I need to state the counter before I set the lcd and wehre to write it. I also learned that if you don't set the cursor, the numbers will be printed at random. I also had to state that the current state was equalivalent to the previous state. I had trouble with stating the integers (I didn't state enough).
## Ultra Sonic Sensor with Neopixel

### Description & Code
The neopixel changes color according to the distance away from the ultrasonic sensor.
```python
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)   #signals to the board which pins to put power to
dot = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5)

r = 0
g = 0
b = 0


while True: #loop; runs forever

    try:
        distance = sonar.distance #distance is equal to the sonar distance
        print((distance)) #printing distance; we're trying to codethe distance from the ultrasonic sensor to centimeters

        if distance < 5: #if distance is less than 5, run this code (turn red if distance is < 5)
            r = 255 #if distance is less than 5, turn light red
            g = 0
            b = 0
        elif distance > 5 and distance < 20: #if the distance is greater than 5, but less than 20, run this code
            r = simpleio.map_range(distance, 5, 20, 255, 0) #def _map(x, in_min, in_max, out_min, out_max)  in_min=5, in_max=20, out_min=255, out_min=0
            b = simpleio.map_range(distance, 5, 20, 0, 255) #def _map(x, in_min, in_max, out_min, out_max)  in_min=5, in_max=20, out_min=0, out_min=255
            g = 0 #no green in pixel
            r = int(r) #red = the integer red
            g = int(g) #green = the integer green
            b = int(b) #blue = the integer blue
        elif distance > 20 and distance < 35: #if distance is greater than 20, but less than 35
            r = 0 #no red in pixel
            b = simpleio.map_range(distance, 20, 35, 255, 0) #def _map(x, in_min, in_max, out_min, out_max)  in_min=20, in_max=35, out_min=255, out_min=0
            g = simpleio.map_range(distance, 20, 35, 0, 255) #def _map(x, in_min, in_max, out_min, out_max)  in_min=20, in_max=35, out_min=0, out_min=255
            r = int(r)
            g = int(g)
            b = int(b)
        elif distance > 35: #if distance is greater than 35
            r = 0
            b = 0
            g = 255 #only green is on
            r = int(r)
            g = int(g)
            b = int(b)
        print(r, g, b) #prints the variables red, green, blue
        time.sleep(0.05)

    except RuntimeError: #if the input is different from the code, print blue, ex. object is too far away
        print("Retrying!")
        r = 0
        g = 0
        b = 255 #automatically print blue
        time.sleep(0.1)

    print(r, g, b)
    dot.fill((r, g, b))
    time.sleep(0.05) #gives delay so doesn't run through loop infinitely

```

### Evidence
file:///C:/Users/schen12/Pictures/Camera%20Roll/WIN_20220920_14_49_41_Pro.mp4

### Wiring
https://www.tinkercad.com/things/67dsxG9fJBI-super-kup/editel?tenant=circuit

### Reflection
At first I trouble shot this project on my own, but after realizing that I had no idea was doing, and still being in Arduino mode, Chris thankfully gave me the code to the pixel. I spent an entire class period commenting the code, and figuring out what different words did, and how they effective the outputs. I learned how to better use the map() function, and the importance of the indentations. I learned that the "While True" function runs the code underneath it in a loop.

This code is initially from Gabby, who gave it to Chris (who's given Gabby credit) thanks! :)

## Motor Control with Potentiometer

### Description & Code
The motor is controlled with the potentiometer. The speed and voltage of the motor is controlled by the potentiometer.
```python
import simpleio
import board
import time
from analogio import AnalogOut, AnalogIn

motor = AnalogOut(board.A5) # assigning motor a pin
pot = AnalogIn(board.A0) # assigning potentiometer a pin

while True:
    print(simpleio.map_range(pot.value, 96, 65520, 0, 65535))
    motor.value = int(simpleio.map_range(pot.value, 96, 65520, 0, 65535)) # maps the motor value to the potentiometer
    time.sleep(0.1)
```

### Evidence

### Wiring

### Reflection

