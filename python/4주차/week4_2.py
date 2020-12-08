# 2.  명령어 ‘l’을 받으면 거북이가 왼쪽으로 100 픽셀 이동하고
#     ‘r’을 받으면 거북이를 오른쪽으로 100 픽셀 이동하는 프로그램을 작성하라. 

import turtle

t= turtle.Turtle()
t.shape("turtle")

key = input("명령을 입력해주세요: ")
if key == "l":
    t.left(90)
    t.forward(100)
if key == "r":
    t.right(90)
    t.forward(100)