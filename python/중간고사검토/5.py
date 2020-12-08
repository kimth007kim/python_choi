import time

now=time.time()
tm = time.localtime(now)

print(tm)
year=tm.tm_year
month=tm.tm_mon
day=tm.tm_mday
hour=tm.tm_hour
minute=tm.tm_min
second=tm.tm_sec

if hour>12:
    hour= hour-12
    print("지금은",year,"년",month,"월",day,"일 오후",hour,"시",minute,"분",second,"초입니다.")
else:
    print("지금은",year,"년",month,"월",day,"일 오전",hour,"시",minute,"분",second,"초입니다.")