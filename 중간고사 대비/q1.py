# 반복문을 이용하여 1부터 10까지 더하는 프로그램을 작성
# n=0
# for i in range (11):
#     n+=i
# print(n)

i=1
sum =0

while i <=10:
    sum= sum+i
    print("sum[%d] = %d " %(i,sum))
    i = i+1