# Car 객체안에 turtle 객체를 이용하는 프로그램을 작성하시오

from turtle import *
image="/Users/Kyungdong/Documents/python_choi/과제/12주차/car.gif"
class Car:
    def __init__(self,speed,color,model):
        self.speed=speed
        self.color=color
        self.model=model
        self.turtle=Turtle()
        self.turtle.shape(image)
    
    def drive(self):
        self.turtle.forward(self.speed)

    def left_turn(self):
        self.turtle.left(90)

register_shape(image)
myCar = Car(200,"red","E-class")
for i in range(100):
    myCar.drive()
    myCar.left_turn()