import turtle
t=turtle.Turtle()
t.shape("turtle")
num = int(input("몇각형을 그릴까요: "))
for i in range(num):
    t.forward(100)
    t.left(360/num)