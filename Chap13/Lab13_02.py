from turtle import *
class Ball:
    def __init__(self,color,size,speed):
        #공의 위치
        self.x=0
        self.y=0

        #공의 속도 벡터
        self.xspeed=speed
        self.yspeed=speed

        #공의 크기
        self.size=size

        #공의 색상
        self.color=color

        self.turtle=Turtle()
        self.turtle.shape("circle")
        self.turtle.color(color,color)
        self.turtle.resizemode("user")
        self.turtle.shapesize(size,size,10)

    #메소드 정의
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.turtle.goto(self.x,self.y)

ball = Ball("red",2,1)
for i in range(100):
    ball.move
    