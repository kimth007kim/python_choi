import random
coin =0
while True:
    coin = random.randint(1,2)
    print(coin)
    t= int(input("앞면일까요1 뒷면일까요2"))
    if(coin == t):
        print("정답")
    else:
        print("땡")