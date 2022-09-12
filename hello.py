import board
import neopixel
import time


dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1 

print("Make it red!")

while True:
    R = 0
    G = 90
    B = 20
    time.sleep(1)
    dot.fill((R,G, B))
    time.sleep(1)
    dot.fill((0, 0, 0))
    print("R:",R," G:", G," B:",B)
