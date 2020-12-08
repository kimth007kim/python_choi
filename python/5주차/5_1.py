import random
time = random.randint(1,24)
sunny = random.choice([True,False])
print("좋은 아침입니다. 지금 시각은", str(time),"시 입니다.")
if sunny==True:
    print("현재 날씨가 화창합니다.")
    if time>=6 and time<=9:
        print("종달새가 노래한다.")
    else:
        print("종달새가 노래하지 않는다.")
else:
    print("현재 날씨가 화창하지 않습니다.")
    print("종달새가 노래하지 않는다.")