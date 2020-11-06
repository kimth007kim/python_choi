# coding:utf-8
num=0
result=0
list=[] 
while num<5:
    s1= int(input("정수를 입력하세요"))
    list.append(s1)
    num= num+1
    result =result+s1

avg =result/len(list)

print("평균=",avg)

