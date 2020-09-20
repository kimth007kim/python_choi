import turtle
t= turtle.Turtle()
t.shape('turtle')

plist= []

x1= int(input("x1:"))
plist.append(x1)
y1= int(input("y1:"))
plist.append(y1)
x2= int(input("x2:"))
plist.append(x2)
y2= int(input("y2:"))
plist.append(y2)
x3= int(input("x3:"))
plist.append(x3)
y3= int(input("y3:"))
plist.append(y3)


t.goto(plist[0],plist[1])
t.goto(plist[2],plist[3])
t.goto(plist[4],plist[5])