from adafruit_circuitplayground import cp
import time, random

while True:
   x, y, z = cp.acceleration
   shake_threshold = 30.0
   if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
      for i in range(10):
         rx = random.randint(0, 255)
         ry = random.randint(0, 255)
         rz = random.randint(0, 255)
         cp.pixels[i] = (rx, ry, rz)