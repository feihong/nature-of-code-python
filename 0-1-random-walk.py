import random
from pyray import *

width, height = 640, 360

class Walker:
  def __init__(self):
    self.x = width // 2
    self.y = height // 2

  def display(self):
    draw_circle(self.x, self.y, 2, VIOLET)

  def step(self):
    choice = random.randint(0, 3)
    if choice == 0:
      self.x += 1
    elif choice == 1:
      self.x -= 1
    elif choice == 2:
      self.y += 1
    elif choice == 3:
      self.y -= 1

init_window(width, height, 'Traditional random walk')
set_target_fps(60)

w = Walker()
clear_background(WHITE)

while not window_should_close():
  begin_drawing()


  w.display()
  w.step()

  end_drawing()

close_window()
