import turtle as t
import time

s = t.Screen()
s.setup(width= 800, height=600)
t.listen()


def forward():
    t.forward(10)

def backward():
    t.backward(10)

def up():
    t.up()
    t.left(90)
    t.down()
    t.forward(10)
    t.setheading(0)

def down():
    t.up()
    t.left(90)
    t.down()
    t.backward(10)
    t.setheading(0)

def clear():
    t.clear()

t.onkeypress(forward, 'Right')
t.onkeypress(backward, 'Left')
t.onkeypress(up, 'Up')
t.onkeypress(down, 'Down')
t.onkeypress(clear, 'space')

t.done()