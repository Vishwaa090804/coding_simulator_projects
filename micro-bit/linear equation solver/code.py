# Linear Equation Solver: ax + b = c

a = 1
b = 0
c = 0
state = 0  # 0=set a, 1=set b, 2=set c, 3=show x

def show_current():
    global state, a, b, c
    if state == 0:
        basic.show_string("a")
        basic.show_number(a)
    elif state == 1:
        basic.show_string("b")
        basic.show_number(b)
    elif state == 2:
        basic.show_string("c")
        basic.show_number(c)
    else:
        if a == 0:
            basic.show_string("Err")
        else:
            x = (c - b) // a
            basic.show_number(x)

def on_forever():
    show_current()
basic.forever(on_forever)

def on_button_pressed_a():
    global state, a, b, c
    if state == 0:
        a -= 1
        if a < -9:
            a = 10
    elif state == 1:
        b -= 1
        if b < -9:
            b = 10
    elif state == 2:
        c -= 1
        if c < -9:
            c = 10
    elif state == 3:
        state = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global state, a, b, c
    if state == 0:
        a += 1
        if a > 10:
            a = -9
    elif state == 1:
        b += 1
        if b > 10:
            b = -9
    elif state == 2:
        c += 1
        if c > 10:
            c = -9
    elif state == 3:
        state = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global state
    if state < 3:
        state += 1
    else:
        state = 0
input.on_gesture(Gesture.Shake, on_gesture_shake)
