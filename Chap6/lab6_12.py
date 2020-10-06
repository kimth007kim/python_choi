import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.pencolor("red")
num=1
t.stamp()
while num<=12:
    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(25)
    t.penup()
    t.forward(15)
    t.stamp()
    t.home()
    t.left(30*num)
    num= num+1