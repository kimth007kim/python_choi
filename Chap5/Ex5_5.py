import random

x= random.randint(1, 100)
y= random.randint(1, 100)
# print("x=",x)
# print("y=",y)

while x<y:
    y= random.randint(1,100)
    # print("y=",y)

ans = x-y
# print("ans = ",ans)
usrans = int(input(str(x)+" - "+str(y)+"= "))
if( ans == usrans):
        print("정답입니다.")
while ans != usrans:
    if ans == usrans:
        print("정답입니다.")
    else:
        print("오답입니다.")
        usrans = int(input("다시입력해주세요: "))
        if ans == usrans:
            print("정답입니다.")
             