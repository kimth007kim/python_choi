import math
PI = math.pi

def circleArea(radius):
    area = (radius**2) * PI 
    print("반지름이", str(radius)+"인 원의 면적:",area)
    
def circleCircumference(radius):
    circum = radius * PI *2
    print("반지름이", str(radius)+"인 원의 둘레:",circum)

def circle(radius):
    circleArea(radius)
    circleCircumference(radius)

radius = int(input("반지름: "))
circle(radius)