import math

PI=math.pi
radius = 5
def Circle(radius):
    circleArea(radius)
    circleCircumference(radius)

def circleArea(radius):
    area= radius**2*PI
    print("반지름이 "+str(radius)+"인 원의 면적: "+str(area))
def circleCircumference(radius):
    circum= 2*radius*PI
    print("반지름이 "+str(radius)+"인 원의 면적: "+str(circum))

Circle(radius)