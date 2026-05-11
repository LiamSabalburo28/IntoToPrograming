from adafruit_circuitplayground import cp
import time, random

while True:
   cp.pixels.fill((255, 0, 0))
   cp.play_tone(500, .5)
   cp.pixels.fill((0, 0, 255))
   cp.play_tone(900, .5)