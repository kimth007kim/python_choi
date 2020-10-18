import turtle
import random

t=turtle.Turtle()
t.shape("turtle")

# 배경색깔: 하늘색
s= turtle.Screen()
s.bgcolor('skyblue')


def many(t):
    for i in range(t):
        x= random.randint(-150,500)
        snowman(x,100)
# 눈사람 그리는 함수
# 여러번 호출 하고 랜덤한 위치에 그림
def snowman(x,y):
    t.fillcolor("white")
    t.begin_fill()
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(50)
    t.end_fill()

    t.penup()
    t.goto(x-50,y/2)
    t.pendown()
    t.left(120)
    t.forward(100)
    t.right(120)

    t.penup()
    t.goto(x+50,y/2)
    t.pendown()
    t.left(60)
    t.forward(100)
    t.right(60)

    t.penup()
    t.goto(x,y-50)
    t.begin_fill()
    t.pendown()
    t.circle(40)
    t.end_fill()

    t.penup()
    t.goto(x,y-170)
    t.begin_fill()
    t.pendown()
    t.circle(70)
    t.end_fill()    

# 눈사람 테스트
# t.fillcolor("white")
# t.begin_fill()
# t.penup()
# t.goto(100,100)
# t.pendown()
# t.circle(50)
# t.end_fill()



# t.penup()
# t.goto(50,50)
# t.pendown()
# t.left(120)
# t.forward(100)
# t.right(120)

# t.penup()
# t.goto(150,50)
# t.pendown()
# t.left(60)
# t.forward(100)
# t.right(60)


# t.penup()
# t.goto(100,50)
# t.begin_fill()
# t.pendown()
# t.circle(40)
# t.end_fill()


# t.penup()
# t.goto(100,-70)
# t.begin_fill()
# t.pendown()
# t.circle(70)
# t.end_fill()
many(5)
input()
