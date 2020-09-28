import turtle

t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","도형을 입력하시오: ")
if s == "사각형":
    degree=90
    s = turtle.textinput("","가로: ")
    w= int(s)
    s = turtle.textinput("","세로: ")
    h= int(s)
    t.forward(w)
    t.left(degree)
    t.forward(h)
    t.left(degree)
    t.forward(w)
    t.left(degree)
    t.forward(h)
    t.left(degree)
elif s== "삼각형":
    degree= 120
    s = turtle.textinput("","길이: ")
    h= int(s)
    t.forward(h)
    t.left(degree)
    t.forward(h)
    t.left(degree)
    t.forward(h)
    t.left(degree)

elif s=="원":
    s = turtle.textinput("","반지름 길이: ")
    t.circle(int(s))
    