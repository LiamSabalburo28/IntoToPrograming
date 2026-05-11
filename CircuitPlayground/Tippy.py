from adafruit_circuitplayground import cp
import time, random

while True:
   if x > 0:
      for i in range(1, 4):
         cp.pixels.fill((0, 0, 0))
         cp.pixels[i] = (0, 255, 0)
   elif x < 0:
      for i in range(6, 9):
         cp.pixels.fill((0, 0, 0))
         cp.pixels[i] = (255, 0, 0)