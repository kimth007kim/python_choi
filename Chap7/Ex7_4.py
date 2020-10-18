import turtle

t=turtle.Turtle()
t.shape("turtle")
cnt=1

def draw_line():
    t.forward(100)
    t.backward(100)

for i in range(12):
    t.left(30)
    draw_line()