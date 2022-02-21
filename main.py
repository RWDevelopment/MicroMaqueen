from microbit import *
import neopixel
import utime

class MaqMicroBit

  def __init__(self):
    i2c.init()
    self.np = neopixel.NeoPixel(pin15, 4)
    pin1.write_digital(0)
