import random
from pyray import *

width, height = 640, 360

class Walker:
  def __init__(self):
    self.x = width // 2
    self.y = height // 2
    self.points = set()

  def display(self):
    for point in self.points:
      draw_circle_v(point, 1.0, VIOLET)

  def step(self):
    stepx = random.randint(-1, 1)
    stepy = random.randint(-1, 1)
    self.x += stepx
    self.y += stepy
    self.points.add(Vector2(self.x, self.y))

init_window(width, height, 'Traditional random walk')
set_target_fps(60)

w = Walker()

while not window_should_close():
  begin_drawing()

  clear_background(WHITE)
  w.display()
  w.step()

  end_drawing()

close_window()
