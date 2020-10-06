# 1부터 10까지 while 문을 사용해서 계산

# total=0
# i=1
# while i < 11:
#     total+=i 
#     i=i+1
# print(total)

#사각형그리기 while문으로

import turtle
t= turtle.Turtle()
t.shape("turtle")

i=1
while i<=4:
    t.forward(100)
    t.left(90)
    i= i+1
