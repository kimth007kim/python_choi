price=2350
money= 5000

total=money-price
# print(total)
coin500= total//500
total= total-coin500*500
# print(coin500)
coin100= total//100
total= total-coin100*100
# print(coin100)
coin10= total//10
total= total-coin100*10
# print(coin10)

print("500원짜리",coin500,"개,","100원짜리",coin100,"개,","10원짜리",coin10,"개")