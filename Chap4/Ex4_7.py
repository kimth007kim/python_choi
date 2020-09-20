import turtle
t= turtle.Turtle()
t.shape("turtle")
color_list= []
c1 = input("색상 #1을 입력하시오: ")
c2 = input("색상 #2을 입력하시오: ")
c3 = input("색상 #3을 입력하시오: ")
color_list.append(c1)
color_list.append(c2)
color_list.append(c3)

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
# t.left(90)
t.forward(100)
t.pendown()

t.fillcolor(color_list[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
# t.left(90)
t.forward(100)
t.pendown()

t.fillcolor(color_list[2])
t.begin_fill()
t.circle(50)
t.end_fill()

input()