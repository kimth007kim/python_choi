import random

num = random.randint(1,99)
your = int(input("복권번호를 입력하시오(0~99): "))
print("당첨번호는", num, "입니다.")

a1 = num//10
a2 = num%10
b1 = your//10
b2 = your%10

if (num == your):
   print("상금은 100만원입니다.")
elif (a1 == b1 or a1 == b2 or a2 == b1 or a2 == b2):
   print("상금은 50만원입니다.")
else:
   print("상금은 없습니다.")
