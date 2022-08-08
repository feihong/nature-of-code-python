from perlin_noise import PerlinNoise
from pyray import *

width, height = 640, 360
noise = PerlinNoise(seed=8888)

class ValueMapper:
  def __init__(self, input_start, input_end, output_start, output_end):
    self.slope = (output_end - output_start) / (input_end - input_start)
    self.input_start = input_start
    self.output_start = output_start

  def __call__(self, value):
    return round(self.output_start + self.slope * (value - self.input_start))


# Range of Perlin noise is not actually [-1, 1]
mapx = ValueMapper(-0.5, 0.5, 0, width)
mapy = ValueMapper(-0.5, 0.5, 0, height)

class Walker:
  def __init__(self):
    self.x = width // 2
    self.y = height // 2

    self.tx = 0
    self.ty = 10000

  def display(self):
    draw_ellipse(self.x, self.y, 16, 16, VIOLET)

  def step(self):
    xnoise = noise(self.tx)
    ynoise = noise(self.ty)
    self.x = mapx(xnoise)
    self.y = mapy(ynoise)
    print(xnoise, ynoise)

    self.tx += 0.01
    self.ty += 0.01

init_window(width, height, 'Perlin noise walker')
set_target_fps(60)

w = Walker()

while not window_should_close():
  begin_drawing()

  clear_background(WHITE)
  w.display()
  w.step()

  end_drawing()

close_window()
