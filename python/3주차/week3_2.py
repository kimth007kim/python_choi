money= int(input("투입한 돈: "))
price = int(input("물건 값: "))

change =  money-price

print("거스름돈: ",change)

coin500= change //500
change = change % 500
coin100 = change //100
change = change % 100
coin10 = change //10

print("500원 동전의 개수: ",coin500)
print("100원 동전의 개수: ",coin100)
print("10원 동전의 개수: ",coin10)
