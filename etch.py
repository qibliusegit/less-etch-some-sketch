import turtle 
import time

s = turtle.Screen()
s.setup(width= 800, height=600)
turtle.listen()

coords = ""
x,y = "", ""

t = turtle.Turtle(visible = False)

t.up()
t.backward(400)
t.setheading(90)
t.backward(300)
t.pencolor('red')
t.down()
t.setheading(0)
t.fillcolor('red')

t.begin_fill()
t.forward(800)
t.setheading(90)
t.forward(100)
t.setheading(180)
t.forward(800)
t.setheading(270)
t.forward(100)
t.end_fill()

t.setheading(0)
t.forward(75)
t.begin_fill()
t.setheading(90)
t.forward(600)
t.setheading(180)
t.forward(75)
t.setheading(270)
t.forward(600)
t.setheading(0)
t.forward(75)
t.end_fill()

t.setheading(90)
t.forward(600)
t.begin_fill()
t.setheading(0)
t.forward(800)
t.setheading(270)
t.forward(100)
t.setheading(180)
t.forward(800)
t.setheading(90)
t.forward(100)
t.end_fill()

t.setheading(0)
t.forward(725)
t.begin_fill()
t.setheading(270)
t.forward(600)
t.setheading(180)
t.forward(75)
t.setheading(90)
t.forward(600)
t.setheading(0)
t.forward(75)
t.end_fill()




tu = turtle.Turtle(visible=False)
tu.up()
tu.setpos(0, 0)
tu.down()
tu.pencolor('black')

def forward():
    global coords
    global x, y 
    coords = tu.pos()
    x,y = coords
    if x <= 300:
        tu.setheading(0)
        tu.forward(10)

def backward():
    global coords
    global x, y 
    coords = tu.pos()
    x,y = coords
    if x >= -300:
        tu.setheading(0)
        tu.backward(10)

def upwards():
    global coords
    global x, y 
    coords = tu.pos()
    x,y = coords
    if y <= 180:    
        tu.setheading(90)
        tu.forward(10)
    

def downwards():
    global coords
    global x, y 
    coords = tu.pos()
    x,y = coords
    if y >= -180:
        tu.setheading(90)
        tu.backward(10)
    

def clear():
    tu.clear()


print(x, y)
turtle.onkeypress(forward, 'Right')
turtle.onkeypress(backward, 'Left')
turtle.onkeypress(upwards, 'Up')
turtle.onkeypress(downwards, 'Down')
turtle.onkeypress(clear, 'space')
turtle.done()