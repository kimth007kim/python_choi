import turtle
import random

t= turtle.Turtle()
t.shape("turtle")


for i in range(10):
    num = random.randint(1,100)
    angle= random.randint(-180,180)
    t.forward(num)
    t.right(angle)