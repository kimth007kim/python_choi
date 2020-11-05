import turtle
t=turtle.Turtle()
def draw_olympic_symbol():
    thecircle= [[0,0,"blue"],[-120,0,"purple"],[60,60,"red"],[-60,60,"yellow"],[-180,60,"green"]]
    for x,y,c in thecircle:
        t.penup()
        t.color(c,c)
        t.goto(x,y)
        t.pendown()
        t.begin_fill()
        t.circle(30)
        t.end_fill()

draw_olympic_symbol()