from pyray import *

width, height = 640, 360
init_window(width, height, "Draw a line from the center halfway to the mouse")
set_target_fps(60)
center_x, center_y = width // 2, height // 2

while not window_should_close():
  begin_drawing()
  clear_background(WHITE)

  vec = get_mouse_position()
  draw_line(
    center_x,
    center_y,
    round(center_x - (center_x - vec.x) / 2),
    round(center_y - (center_y - vec.y) / 2),
    VIOLET)

  end_drawing()

close_window()
