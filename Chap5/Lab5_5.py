import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)

if coin ==0:
    print("앞면입니다.")
if coin ==1:
    print("뒷면입니다.")
print("게임이 종료되었습니다.")