nlist =[]
result=0
for i in range(5):
    num= int(input("정수를 입력해주세요: "))
    result+=num
    nlist.append(num)

avg= result/len(nlist)
print("평균=",avg)
