import random
from pyray import *

width, height = 640, 360

class Walker:
  def __init__(self):
    self.x = width // 2
    self.y = height // 2

    # We must draw into a framebuffer if we want to draw continuously without
    # using extra data structures or experiencing flickering
    # https://www.reddit.com/r/raylib/comments/i6mkh0/only_clear_background_once/
    self.frame_buffer = load_render_texture(width, height)

    begin_texture_mode(self.frame_buffer)
    clear_background(WHITE)
    end_texture_mode()

  def display(self):
    begin_texture_mode(self.frame_buffer)
    draw_pixel(self.x, self.y, VIOLET)
    end_texture_mode()

    draw_texture(self.frame_buffer.texture, 0, 0, WHITE)

  def step(self):
    r = random.random()
    if r < 0.4:
      self.x += 1
    elif r < 0.6:
      self.x -= 1
    elif r < 0.8:
      self.y += 1
    else:
      self.y -= 1

init_window(width, height, 'Walker that tends to move to the right')
set_target_fps(60)

w = Walker()

while not window_should_close():
  begin_drawing()

  w.display()
  w.step()

  end_drawing()

close_window()
