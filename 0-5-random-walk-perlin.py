from perlin_noise import PerlinNoise
from pyray import *
import utils

width, height = 640, 360
noise = PerlinNoise(seed=8888)

# Range of Perlin noise is not actually [-1, 1]
# https://stackoverflow.com/questions/18261982/output-range-of-perlin-noise
mapx = utils.make_map_func(-0.5, 0.5, 0, width)
mapy = utils.make_map_func(-0.5, 0.5, 0, height)

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
    # print(xnoise, ynoise)

    self.x = mapx(xnoise)
    self.y = mapy(ynoise)

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
