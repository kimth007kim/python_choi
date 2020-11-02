import random

counters = [0,0,0,0,0,0]

t= int(input("몇번 돌립니까?"))
for i in range(t):
    value =random.randint(0,5)
    counters[value]= counters[value]+1

print("주사위가 1인 경우는",counters[0])
print("주사위가 2인 경우는",counters[1])
print("주사위가 3인 경우는",counters[2])
print("주사위가 4인 경우는",counters[3])
print("주사위가 5인 경우는",counters[4])
print("주사위가 6인 경우는",counters[5])
