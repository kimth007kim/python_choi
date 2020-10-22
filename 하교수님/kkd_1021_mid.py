
# 1. a < b인 두 정수 a, b를 입력 받아 그 수 사이의 소수를 모두 출력하는 프로그램을 작성하세요.

print("a와 b 사이의 정수를 구합니다.")
a = int(input("정수 a를 입력해주세요: "))
b = int(input("정수 b를 입력해주세요: "))

if a<b and a>=2:
    for i in range(a,b+1):
        for j in range(2,i+1):
            if i%j==0:
                break
        if i==j and i>1:
            print(j,end=" ")
elif a>b:
    print("a 가 b보다 큽니다. b 가 더 큰수가 되도록 입력해주세요")
elif a<2:
    print("a 가 2보다 작습니다. 2나 2보다 큰수를 a로 지정해주세요")

print() # 다음문제를 위한 여백입니다.

# 2. 자신의 학번 끝 4자리를 입력받아 모두 더하는 프로그램을 작성하시오.
# 실행 예시) 
# 1243 엔터
# 1+2+4+3 = 10 

num = int(input("학번 뒤 4자리 숫자를 입력해주세요: "))

if num>=1000 and num<10000:
    result = 0

    digit1= num//1000
    result= num%1000
    digit2= result//100
    result= result%100
    digit3= result//10
    result= result%10

    tot= digit1+digit2+digit3+result
    print("%d+%d+%d+%d= %d" %(digit1,digit2,digit3,result,tot))
else:
    print("네자리만 입력해주세요!")
