from pyray import *

width, height = 640, 360
init_window(width, height, "Bouncing ball with no vectors")
set_target_fps(60)

x = 100
y = 100
xspeed = 1
yspeed = 3

while not window_should_close():
  if is_key_down(KEY_Q):
    break
  begin_drawing()
  clear_background(WHITE)

  x = x + xspeed
  y = y + yspeed

  if x > width or x < 0:
    xspeed *= -1
  if y > height or y < 0:
    yspeed *= -1

  draw_ellipse(x, y, 16, 16, VIOLET)

  end_drawing()

close_window()
