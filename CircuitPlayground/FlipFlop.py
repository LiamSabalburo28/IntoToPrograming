from adafruit_circuitplayground import cp
import time, random

prev_pos = cp.switch
while True:
   if prev_pos != cp.switch:
      cp.pixels.fill((0, 0, 0))
   prev_pos = cp.switch
   if prev_pos == False:
      for i in range(5, 10):
         cp.pixels[i] = (0, 255, 0)
   elif prev_pos == True:
      for i in range(5):
         cp.pixels[i] = (0, 255, 0)