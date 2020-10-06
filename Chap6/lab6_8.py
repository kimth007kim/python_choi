cont= "yes"
total = 0
# num =  int(input("숫자를 입력하시오: "))
while cont == "yes":
    num =  int(input("숫자를 입력하시오: "))
    total = total + num
    cont = input("계속?(yes/no): ")
print("합계는 : ",total)