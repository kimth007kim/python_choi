
# 마음대로 이동하는 거북이
# 300x300 크기의 윈도 창 안에서 거북이가 마음대로
# 임의로 이동하는 거리나 각도는 random.randrange()
# 선색상도 random.random()
# 화면을 나가면 중앙으로 위치하게 하기
import turtle
import random

# 전역 변수 선언 부분
swidth,sheight,pSize,exitCount =300, 300,3,0
r,g,b,angle,dist,curX,curY = [0] * 7

# 메인 코드 부분
turtle.title("거북이 마음대로 다니기")
turtle.shape("turtle")
turtle.pensize(pSize)
turtle.setup(width = swidth+30, height= sheight +30)

while True:
    r = random.random()
    g = random.random()
    b = random.random()
    dist = random.randint(1,100)
    angle = random.randint(-180,180)
    turtle.pencolor((r,g,b))
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()

    if(-swidth/2 <= curX  and swidth/2 >= curX ) and ( -sheight/2 <= curY and sheight/2 >= curY):
        pass
    else:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        
        exitCount += 1
        if exitCount >=5:
            break
turtle.done()