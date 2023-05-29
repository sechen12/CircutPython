# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of_Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [UltraSonicSensorwithNeopixel](#UltraSonicSensorwithNeopixel)
* [MotorControlwithPotentiometer](#MotorControlwithPotentiometer)
* [TemperatureSensor](#TemperatureSensor)
* [RotaryCode](#RotaryCode)
* [Photointerrupter](#Photointerrupter)
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
## UltraSonicSensorwithNeopixel

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

## MotorControlwithPotentiometer

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

![motorcontrolgif](https://github.com/sechen12/CircutPython/assets/112981481/a5fb1b6d-bc04-49c3-a186-3c5390c3e911)

### Wiring

![Screenshot 2022-11-01 115847](https://github.com/sechen12/CircutPython/assets/112981481/d033a18c-38b0-4b93-9123-8bbc8619e863)

### Reflection
I learned that my initial thought if the motor isn't working is to refer to my Serial Monitor. I am able to collect data, and proceed to plan my next steps. In this case, there wasn't any power going to my board at all; from there I had to check my batteries and wiring to find the root of the problem. I used a Multi Meter to check the voltage of the batteries, and sure enough, one of the batteries had a negetive charge! My teacher and I had to get rid of that particular battery, but using the Serial Monitor to check the status of how the board is communicating with the board is something I now heavily rely on.

## TemperatureSensor

### Description & Code
Use a TMP36 temperature sensor to print the values onto an LCD screen.
```python
import board
import analogio
import time
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface



# turn on lcd
lcdPower = digitalio.DigitalInOut(board.D8)
lcdPower.direction = digitalio.Direction.INPUT
lcdPower.pull = digitalio.Pull.DOWN

while lcdPower.value is False:
    print("still sleeping")
    time.sleep(0.1)

time.sleep(1)
print(lcdPower.value)
print("running")

i2c = board.I2C()



lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
TMP36_PIN = board.A0  # Analog input connected to TMP36 output.


# Function to simplify the math of reading the temperature.
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10



# Create TMP36 analog input.
tmp36 = analogio.AnalogIn(TMP36_PIN)

# Loop forever.
while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value and delay a second before looping again.
    lcd.set_cursor_pos(0, 0)
    print("Temperature: {}C {}F".format(temp_C, temp_F))

    lcd.print(("Temperature: {}C {}F".format(temp_C, temp_F)))
    lcd.print((" "))

    time.sleep(1.0)
```

### Evidence

https://user-images.githubusercontent.com/112981481/225731990-e23dd9d1-eaa7-4f6f-8de5-d98dc211c637.mp4

### Wiring
![tempaturewiring](https://user-images.githubusercontent.com/112981481/225733918-45b95248-ce2e-4b48-98c1-cc81cd542057.png)
### Reflection
Although this assignment was straightfoward in the sense that I simply had to surf the web for the appropriate code, my LCD printer was taking the power from the Aruduino, making it impossible for the words to appear. We had to use a switch to manage the flow of electricty. I learned that code is read by a series of yes's, and no's, or for Python, True and False. Code is also written with the utmost specificity; if one comma is misplaced, the entire script wil not run properly. It was crucial for us to use Google to find the proper syntax needed for a well working assignment. Code is less about the raw knowledge about the subject, but one's ability to use the resources around them.

## RotaryCode

### Description & Code
Use a Rotary encoder to program words that will appear on the LCD display.
```

import board
import digitalio
import neopixel
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

led: neopixel.Neopixel = neopixel.NeoPixel(board.NEOPIXEL, 1) # initialization of hardware
print("neopixel")

led.brightness = 0.1

button = digitalio.DigitalInOut(board.D12)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

colors = [("stop", (255, 0, 0)), ("caution", (128, 128, 0)), ("go", (0, 255, 0))]

encoder = rotaryio.IncrementalEncoder(board.D10, board.D9, 2)
last_position = None
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        lcd.clear()
        lcd.print(colors[position % len(colors)][0])
    if(not button.value):
        led[0] = colors[position % len(colors)][1]
    last_position = position
```

### Evidence

![name](https://github.com/sechen12/CircutPython/blob/master/media/trafficlight%20(1).gif?raw=true)

### Wiring

![YAYAYA](https://user-images.githubusercontent.com/112981481/228339131-dc2dd894-b310-47bd-8176-720f5c1e5d4a.png)

### Reflection
This assignment used a lot of new commands that I wasn't familiar with. I had to use a code found from the web, and peice it together with code found from different classmates'.

## Photointerrupter

### Description & Code
Show the number of interruptions in a photointerrupter displayed on an LCD.
```

import board
import time
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

i2c = board.I2C()
btn = DigitalInOut(board.D8)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)
cur_state = True
prev_state = True
buttonPress = -1
now = time.monotonic()  # Time in seconds since power on


while True: 
    if (now + 4) < time.monotonic():  # If the time less than four seconds
        print ("times up" + str(now) + " " + str(buttonPress))  #  Print what is displayed
        now = time.monotonic()  #Now is the time in seconds
        buttonPress = 0
    
    cur_state = btn.value  # The current value is the button's value
    if cur_state != prev_state:
        if not cur_state:
            buttonPress = buttonPress + 1  #  Button press, or when the photointerrupter is interrupted = button press + 1
            lcd.clear()  #  Then clear the lcd
            lcd.set_cursor_pos(0,0)  #  Positioning the cursor
            lcd.print("The number of interrupts is: " + str(buttonPress))  #  Print the number of button presses
    prev_state = cur_state
```

### Evidence

![phtointerrupter](https://user-images.githubusercontent.com/112981481/228984162-697ecc8b-5663-41b3-8715-f02eb784f018.gif)

### Wiring

![228350137-55d7ddd0-c263-4111-8555-3bfe5479992a](https://user-images.githubusercontent.com/112981481/228985026-327c69e0-a522-49af-b7df-e4ec1f174f22.png)

### Reflection

This assignmnet wasn't extremely difficult. The lcd is something we've been working with for the past few assignments, so the wiring and code was either found from previous projects, or it was already wired (or coded). The photointerrupter code is from previous interrupter code as well, so over all, the entire project was copy + paste. I didn't know how to reset the count after four seconds, so huge thanks to Sahana! I pulled her gif and wiring diagram as well 😄
