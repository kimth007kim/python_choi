import turtle

turtle.title("거북이로 두 숫자 비트 논리곱(&) 연산하기")

a = int(input("첫번째 숫자를 입력해주세요: "))
b = int(input("두번째 숫자를 입력해주세요: "))
turtle.up()
turtle.shape("turtle")

bina = bin(a)
binb = bin(b)
ans= bina & binb

if 
print("bina:" ,bina)
print("binb:" ,binb)

# 비트 논리곱을 구현하려고 숫자를 2개 입력받아서 각 숫자에 대한 2진수와 비트 논리곱결과 2진수를 출력하기