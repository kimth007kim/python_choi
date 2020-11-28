from turtle import *

class MyTurtle(Turtle):
    def glow(self,x,y):
        self.fillcolor("red")

turtle= MyTurtle()
turtle.shape("turtle")
turtle.onclick(turtle.glow)
