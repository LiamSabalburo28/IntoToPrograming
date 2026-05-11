from adafruit_circuitplayground import cp
import time, random

count = 0
while True:
   if cp.button_a:
      if count >= 9:
         count = 9
      else:
         time.sleep(.2)
         cp.pixels.fill((0, 0, 0))         
         count += 1
         for i in range(count): cp.pixels[i] = (255, 255, 255)
   if cp.button_b:
      if count >= 0:
         count = 0
      else:
         time.sleep(.2)
         cp.pixels.fill((0, 0, 0))
         count -= 1
         for i in range(count): cp.pixels[i] = (255, 255, 255)