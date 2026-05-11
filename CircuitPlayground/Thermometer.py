from adafruit_circuitplayground import cp
import time, random

while True:
   c = cp.temperature
   f = (c * 9/5) + 32
   cp.pixels.fill((0, 0, 0))
   while f < 78:
      cp.pixels[0] = (0, 0, 255)
      time.sleep(.1)
   while f > 78:
      cp.pixels[1] = (0, 0 , 255)
      time.sleep(.1)
   while f > 79:
      cp.pixels[2] = (0, 0, 255)
      time.sleep(.1)
   while f > 80:
      cp.pixels[3] = (0, 255, 255)
      time.sleep(.1)
   while f > 81:
      cp.pixels[4] = (255, 255, 0)
      time.sleep(.1)
   while f > 82:
      cp.pixels[5] = (255, 255, 0)
      time.sleep(.1)
   while f > 83:
      cp.pixels[6] = (255, 255, 0)
      time.sleep(.1)
   while f > 84:
      cp.pixels[7] = (255, 0, 0)
      time.sleep(.1)
   while f > 85:
      cp.pixels[8] = (255, 0, 0)
      time.sleep(.1)
   while f > 86:
      cp.pixels[9] = (255, 0, 0)
      time.sleep(.1)