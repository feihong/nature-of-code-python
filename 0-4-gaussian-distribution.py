import random
from pyray import *

width, height = 640, 360

init_window(width, height, 'Gaussian distribution')
set_target_fps(60)

frame_buffer = load_render_texture(width, height)
begin_texture_mode(frame_buffer)
clear_background(WHITE)
end_texture_mode()

violet = Color(VIOLET[0], VIOLET[1], VIOLET[2], 10)

while not window_should_close():
  begin_drawing()

  begin_texture_mode(frame_buffer)
  x = int(random.gauss(320, 60))
  draw_ellipse(x, 180, 16, 16, violet)
  end_texture_mode()
  draw_texture(frame_buffer.texture, 0, 0, WHITE)

  end_drawing()

close_window()
