# Python code
#
isPrime = 0
num = 0
i = 0
num = 5
basic.show_number(num)

def on_forever():
  pass
basic.forever(on_forever)

def on_button_pressed_a():
  global i
  global isPrime
  i = 2
  isPrime = 1
  while i * i <= num:
    if num % i == 0:
      basic.show_number(i)
      basic.show_number((num / i))
      isPrime = 0
    i = (i + 1)
  if isPrime == 1:
    basic.show_string("prime Number")
input.on_button_pressed(Button.A, on_button_pressed_a)
