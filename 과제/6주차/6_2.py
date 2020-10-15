import turtle

t=turtle.Turtle()

data= [100,98,32,74,52]

def draw(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font=('Times New Roman',16,'bold'))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
t.color("blue")
t.fillcolor("red")

# draw(data[1])
# draw(100)
for d in data:
    draw(d)