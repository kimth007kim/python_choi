# print("a와 b 사이의 정수를 구합니다.")
# a = int(input("정수 a를 입력해주세요: "))
# b = int(input("정수 b를 입력해주세요: "))

a=8
b=15

if a<b and a>=2:
    for i in range(a,b+1):
        for j in range(2,i+1):
            if i%j==0:
                break
        if i==j and i>1:
            print(j,end=" ")
elif a>b:
    print("a 가 b보다 큽니다. b 가 더 큰수가 되도록 입력해주세요")
