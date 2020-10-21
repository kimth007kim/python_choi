import random

x= random.randint(1,100)
y= random.randint(1,100)

if y>x:
    result= y-x
    num= int(input(str(y)+" - "+str(x) + " = "))
    if result ==num:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
else:
    result= x-y
    num= int(input(str(x) + " - "+str(y)+ " = "))
    if result ==num:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")