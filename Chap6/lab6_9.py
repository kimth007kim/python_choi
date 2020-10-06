# 숫자 맞추기 게임

import random

ans = random.randint(1,100)
num = int(input("숫자를 입력하시오: "))
cnt= 1
while  ans!= num:
    if ans>num:
        print("낮음")
    elif ans<num:
        print("높음")
    num = int(input("숫자를 입력하시오: "))
    cnt = cnt+1
print("축하합니다. 시도횟수= ",cnt)