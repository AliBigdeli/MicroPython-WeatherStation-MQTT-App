import neopixel

class Colors:
  yellow = (255, 100, 0)
  orange = (255, 50, 0)
  green = (0, 255, 0)
  blue = (0, 0, 255)
  red = (255, 0, 0)
  black = (0,0,0)
  white = (255,255,255)
  
class PixelCtrl:
  def __init__(self,led_pin,num_pixels=2):
    self.pixels_obj = neopixel.NeoPixel(led_pin,num_pixels)
    
  def fill(self,color):
      self.pixels_obj.fill(color)
      self.pixels_obj.fill(color)
      self.pixels_obj.write()
  
  def off(self):
    self.pixels_obj.fill(Colors.black)
    self.pixels_obj.fill(Colors.black)
    self.pixels_obj.write()
  
  def on(self):
    self.pixels_obj.fill(Colors.white)
    self.pixels_obj.fill(Colors.white)
    self.pixels_obj.write()