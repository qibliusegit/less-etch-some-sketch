import turtle as t
import time

s = t.Screen()
s.setup(width= 800, height=600)
t.listen()

coords = t.pos()
x,y = coords


def forward():
    global coords
    global x, y 
    coords = t.pos()
    x,y = coords
    if x <= 400:
        t.setheading(0)
        t.forward(10)

def backward():
    global coords
    global x, y 
    coords = t.pos()
    x,y = coords
    if x >= -400:
        t.setheading(0)
        t.backward(10)

def upwards():
    global coords
    global x, y 
    coords = t.pos()
    x,y = coords
    if y <= 300:    
        t.setheading(90)
        t.forward(10)
    

def downwards():
    global coords
    global x, y 
    coords = t.pos()
    x,y = coords
    if y >= -300:
        t.setheading(90)
        t.backward(10)
    

def clear():
    t.clear()

t.onkeypress(forward, 'Right')
t.onkeypress(backward, 'Left')
t.onkeypress(upwards, 'Up')
t.onkeypress(downwards, 'Down')
t.onkeypress(clear, 'space')
t.done()