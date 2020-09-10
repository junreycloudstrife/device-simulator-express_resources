"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

from adafruit_circuitplayground import cp

while True:
    color = int(255 * cp.light / 320)
    cp.pixels[0] = (color, color, color)
    cp.pixels[1] = (color, color, color)
    cp.pixels[2] = (color, color, color)
    cp.pixels[3] = (color, color, color)
    cp.pixels[4] = (color, color, color)
    cp.pixels[5] = (color, color, color)
    cp.pixels[6] = (color, color, color)
    cp.pixels[7] = (color, color, color)
    cp.pixels[8] = (color, color, color)
    cp.pixels[9] = (color, color, color)
