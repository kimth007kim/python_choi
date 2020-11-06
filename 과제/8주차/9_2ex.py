import random

counters=[0,0,0,0,0,0]
times= int(input("주사위를 몇번 굴려볼까요?"))

for i in range (times):
    value = random.randint(0,5)
    counters[value]=counters[value]+1

for i in range(6):
    print("주사위가 ",i+1,"인 경우는 ", counters[i])