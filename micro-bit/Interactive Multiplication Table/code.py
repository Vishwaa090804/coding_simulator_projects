# Python code
N = 0
k = 0
sign = 0
res = 0
N = 5
k = 1
sign = 1
res = (N * k)
basic.show_number(res)

def on_forever():
  basic.show_number((N * (k * sign)))
basic.forever(on_forever)

def on_button_pressed_a():
  global k
  k += -1
  if k < 1:
    k = 10
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
  global k
  k += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
  global sign
  sign = (sign * -1)
input.on_gesture(Gesture.Shake, on_gesture_shake)
