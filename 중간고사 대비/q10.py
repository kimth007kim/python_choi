import time

fseconds = time.time()//60
minute= fseconds%60
hour = fseconds //60 % 24


print("현재시간:",int(hour+1),"시",int(minute),"분")