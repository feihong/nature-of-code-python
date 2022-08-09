from perlin_noise import PerlinNoise
from pyray import *
from utils import make_map_func

noise = PerlinNoise(seed=1)

width, height = 640, 360

map_color = make_map_func(-6, 6, 0, 255)

init_window(width, height, '2D Perlin noise')
set_target_fps(60)

frame_buffer = load_render_texture(width, height)

begin_texture_mode(frame_buffer)
clear_background(WHITE)

xoff = 0.0

for x in range(width):
  yoff = 0.0

  for y in range(height):
    bright = map_color(noise([xoff, yoff]))
    color = Color(bright, bright, bright, 255)
    draw_pixel(x, y, color)
    yoff += 0.01

  xoff += 0.01

end_texture_mode()

while not window_should_close():
  begin_drawing()
  draw_texture(frame_buffer.texture, 0, 0, WHITE)
  end_drawing()

close_window()
