import random

num = int(input("복권 번호를 입력하시요(0에서 99사이): "))
lotto= random.randint(0,99)
print("당첨번호는",lotto,"입니다.")
n1= lotto//10
n2= lotto%10

l1= num//10
l2=num%10

if n1==l1 and n2 ==l2:
    print("상금은 100만원입니다.")
elif (n1==l1 and n2 !=l2) or (n1!=l1 and n2 ==l2):
    print("상금은 50만원입니다.")
else:
    print("상금은 없습니다.")
