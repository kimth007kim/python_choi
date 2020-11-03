import turtle
import random
t=turtle.Turtle()
color = ["yellow","red","purple","blue"]

def draw_square(x,y,c):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

for c in color:
    xpo=random.randint(-300,300)
    ypo=random.randint(-300,300) 
    draw_square(xpo,ypo,c)