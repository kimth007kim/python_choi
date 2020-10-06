import turtle

t= turtle.Turtle()
t.shape("turtle")

for i in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(200,0)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)