import turtle

t= turtle.Turtle()

# 거북이 함수그리기 부분
def fun():
    for i in range(150):
        t.goto(i,(i**2+1)*0.01)

# 그래프 부분
t.forward(300)
t.right(180)
t.forward(300)
t.right(90)
t.forward(300)
t.penup()
t.goto(0,0)
t.pendown()


fun()
