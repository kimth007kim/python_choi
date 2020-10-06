num = int(input("정수를 입력해주세요 팩토리얼을 계산합니다: "))

sum=1
for i in range(1,num+1):
    sum= sum*i
print(num, "!은","",sum,"이다.")