americano = 2000
cafelate = 3000
capucino = 3500

x = int(input("아메리카노 판매 개수: "))
y = int(input("카페라떼 판매 개수: "))
z = int(input("카푸치노 판매 개수: "))

sum=(americano*x)+(cafelate*y)+(capucino*z)
print("총 매출은 ",sum," 입니다.")