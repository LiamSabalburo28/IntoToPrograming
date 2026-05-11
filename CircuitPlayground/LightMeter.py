from adafruit_circuitplayground import cp
import time, random

while True:
   x = 30
   while cp.light <= x:
      if x == cp.light:
         for i in range(10 - x // 3):
            cp.pixels[i] = (255, 255, 255)
         for i in range(9, 10-(x // 3), -1):
            cp.pixels[i] = (0, 0, 0)
      else:
         x -= 3