import random
from pyray import *

width, height = 640, 360

random_counts = [0 for _i in range(20)]
length = len(random_counts)

init_window(width, height, 'Random number distribution')
set_target_fps(60)
clear_background(WHITE)

while not window_should_close():
  begin_drawing()

  random_counts[random.randint(0, length - 1)] += 1
  w = width // length
  for i in range(length):
    draw_rectangle(i * w, height - random_counts[i], w - 1, random_counts[i], VIOLET)

  end_drawing()

close_window()
