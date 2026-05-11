from adafruit_circuitplayground import cp
import time, random

while True:
    if cp.button_a:
        cp.pixels.fill((0, 255, 0))
        time.sleep(.367)
        cp.pixels.fill((0, 0, 0))
        time.sleep(.367)