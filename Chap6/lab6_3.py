import turtle
import random
t= turtle.Turtle()
t.shape("turtle")

for i in range(30):
    length = random.randint(1,100)
    angle = random.randint(-180,180)
    t.forward(length)
    t.right(angle)