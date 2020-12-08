cnt=0
origin=int(input("정수를 입력해주세요 각자리의 합을 출력합니다."))
result=0
num= origin

while num>=10:
    num= num/10
    cnt=cnt+1

for i in range(cnt+1):
    d1 = origin % 10
    origin = origin //10
    result= result+d1

print(result)
