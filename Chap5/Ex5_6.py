ans = int(input("정수를 입력하시오: "))

if (ans %2 ==0 and ans %3 == 0):
    print("2와 3으로 나누어 떨어집니다.")
elif (ans %2==0 ):
    print("2로 나누어 떨어집니다.")
elif (ans %3==0 ):
    print("3로 나누어 떨어집니다.")
else:
    print("아무리 해도 안되네요 ㅠㅠ")