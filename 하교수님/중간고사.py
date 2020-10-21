num = int(input("숫자를 입력해주세요"))
# num =4321
result = 0

digit1= num//1000
result= num%1000
digit2= result//100
result= result%100
digit3= result//10
result= result%10

# print("digit1:",digit1 ,"result:",result)
# print("digit2:",digit2 ,"digit3:",digit3)
sum= digit1+digit2+digit3+result
print("각자리 수의 합은",sum,"입니다." )