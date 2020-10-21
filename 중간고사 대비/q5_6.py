num = int(input("정수를 입력하시오: "))

if num %2==0 and num %3==0:
    print("2와 3으로 나누어 떨어집니다.")
elif num %2==0 and num %3!=0:
    print("2로 나누어 떨어집니다.")
elif num %2!=0 and num %3==0:
    print("3으로 나누어 떨어집니다.")
else:
    print("2와 3둘 중 아무것도 나누어 떨어지지 않습니다.")