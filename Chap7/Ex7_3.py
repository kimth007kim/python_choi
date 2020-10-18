import turtle

t=turtle.Turtle()

# 그래프 그리기
t.forward(300)
t.right(180)
t.forward(300)
t.right(90)
t.forward(300)
t.right(180)
t.forward(300)
t.right(90)

# 거북이 그리는 함수 부분

def fun():
    for i in range(150):
        t.goto(i,((i**2)+1)*0.01)

fun()
