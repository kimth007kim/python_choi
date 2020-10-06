import random

while True:
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
    ans = number1+number2

    print(number1,"+",number2,"=",end=" ")
    userans= int(input())
    if ans==userans:
        print("잘했어요!!")
    else:
        print("다음번에는 잘할 수 있죠?")
