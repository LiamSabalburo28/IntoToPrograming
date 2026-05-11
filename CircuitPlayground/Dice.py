from adafruit_circuitplayground import cp
import time, random

while True:
   if cp.button_a:
      cp.pixels.fill((0, 0, 0))
      roll = random.randint(0, 10)
      for i in range(roll):
         if roll == 0:
            cp.pixel.fill((0, 0, 0))
         cp.pixels[i] = (255, 255, 255)
      time.sleep(.2)
   if cp.button_b:
      cp.pixels.fill((0, 0, 0))