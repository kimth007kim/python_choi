import turtle
t=turtle.Turtle()
t.shape("turtle")

def hexagon():
    # turtle.penup()
    # turtle.goto(x,y)
    # turtle.pendown()
    for i in range(6):
        turtle.forward(50)
        turtle.left(60)

# hexagon(125,125)
# hexagon(0,0)


for i in range(6):
    turtle.forward(50)
    turtle.right(60)
    hexagon()