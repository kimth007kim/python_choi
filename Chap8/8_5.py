from turtle import Screen, Turtle
from random import choice
# os.chdir()


screen=Screen()
image1="/Users/Kyungdong/Documents/pythob_choi/Chap8/rabbit.gif"
image2="/Users/Kyungdong/Documents/pythob_choi/Chap8/turtle.gif"

screen.addshape(image1)
screen.addshape(image2)

turtle =Turtle()
t1=turtle.Turtle()
t1.shape(image1)

t2=turtle.Turtle()
t2.shape(image2)

# import os
# print(os.getcwd())
# os.chdir("C:\\python_choi\Chap8")
# print(os.getcwd())