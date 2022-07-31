from pyray import *

init_window(600, 400, "Hello")

while not window_should_close():
  if is_key_down(KEY_Q):
    break
  begin_drawing()
  clear_background(WHITE)
  draw_text("Hello world", 220, 200, 20, VIOLET)
  end_drawing()

close_window()
