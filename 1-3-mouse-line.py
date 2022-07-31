"""
We don't bother with translate. Note that Vec2 components are floats and must
be converted to ints before being passed to draw_line.
"""
from pyray import *

width, height = 640, 360
init_window(width, height, "Draw a line from the center to the mouse")
set_target_fps(60)
center_x, center_y = width // 2, height // 2

while not window_should_close():
  begin_drawing()
  clear_background(WHITE)

  vec = get_mouse_position()
  draw_line(center_x, center_y, round(vec.x), round(vec.y), VIOLET)

  end_drawing()

close_window()
