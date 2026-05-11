from adafruit_circuitplayground import cp
import time, random

def secret_chime():
   cp.play_tone(392, 0.068)
   cp.play_tone(370, 0.068)
   cp.play_tone(311, 0.068)
   cp.play_tone(440, 0.068)
   cp.play_tone(415, 0.068)
   cp.play_tone(330, 0.068)
   cp.play_tone(415, 0.068)
   cp.play_tone(532, 1.226)

def reset(count, list):
   count = 0; list = []
   cp.pixels.fill((255, 255, 255))
   cp.play_tone(700, .25)
   cp.pixels.fill((0, 0, 0))