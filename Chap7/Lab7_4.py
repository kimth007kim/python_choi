import turtle

def drawit(x,y):
    t.goto(x,y)
    
t = turtle.Turtle()
t.shape("turtle")
t.pensize(10)    



s= turtle.Screen()
s.onscreenclick(drawit)
s.onkey(t.penup, "Up")
s.onkey(t.pendown,"Down")
s.listen()

input()