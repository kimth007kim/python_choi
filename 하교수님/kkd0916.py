# 201532003 김경동

# import turtle

# turtle.shape('turtle')
# turtle.forward(200)
# turtle.right(72)
# turtle.forward(200)
# turtle.right(72)
# turtle.forward(200)
# turtle.right(72)
# turtle.forward(200)
# turtle.right(72)
# turtle.forward(200)
# turtle.right(72)

# import turtle
# import random

# # 함수 선언 부분
# def screenCLickLeft(x,y):
#     global r,g,b
#     turtle.pencolor((r,g,b))
#     turtle.pendown()
#     turtle.goto(x,y)

# def screenRightClick(x,y):
#     turtle.penup()
#     turtle.goto(x,y)

# def screenMidClick(x,y):
#     global r,g,b
#     tSize = random.range(1,10)
#     turtle.shapesize(tSzie)
#     r = random.random()
#     g = random.random()
#     b = random.random()

# pSize = 10
# r,g,b = 0.0,0.0,0.0

# turtle.title('거북이로 그림그리기')
# turtle.shape('turtle')
# turtle.pensize(pSize)

# turtle.onscreenclick(screenCLickLeft,1)
# turtle.onscreenclick(screenMidClick,2)
# turtle.onscreenclick(screenRightClick,3)

# turtle.done()


import turtle
import random

# 함수 선언 부분
def screenCLickLeft(x,y):
    global r,g,b
    tDegree = random.randrange(0,360)
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    turtle.left(tDegree)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.fillcolor((r,g,b))
    turtle.stamp()

def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)

 

pSize = 10
r,g,b = 0.0,0.0,0.0

turtle.title('거북이로 그림그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenCLickLeft,1)
turtle.onscreenclick(screenRightClick,3)

turtle.done()
