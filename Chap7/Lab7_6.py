import turtle
t= turtle.Turtle()

def draw(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font=('Time New Roman' ,16,'bold'))
    t.right(90)

    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

data= [120,56,309,220,156,23,98]

t.color("blue")
t.fillcolor("red")

t.pensize(3)

for i in data:
    draw(i)