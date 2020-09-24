import turtle
t= turtle.Turtle()
t.shape('turtle')

while True:
    key = input("명령을 입력해주세요: ")

    if (key=="l"):
        t.left(90)
        t.forward(100)
    if (key=="r"):
        t.right(90)
        t.forward(100)
            
