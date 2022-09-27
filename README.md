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
Description goes here

Here's how you make code look like code:

```python
Code goes here

```


### Evidence


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

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

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring
https://www.tinkercad.com/things/67dsxG9fJBI-super-kup/editel?tenant=circuit
### Reflection

At first I trouble shot this project on my own, but after realizing that I had no idea was doing, and still being in Arduino mode, Chris thankfully gave me the code to the pixel. I spent an entire class period commenting the code, and figuring out what different words did, and how they effective the outputs. I learned how to better use the map() function, and the importance of the indentations. I learned that the "While True" function runs the code underneath it in a loop.

This code is initially from Gabby, who gave it to Chris (who's given Gabby credit) thanks! :)

## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
