import turtle
t= turtle.Turtle()
t.shape("turtle")

size= int(input("크기를 얼마로 짓지요?: "))

t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)

t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)

input()