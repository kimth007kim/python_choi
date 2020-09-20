import time
now = time.time()
thisYear = int(1970 + now//(365*24*3600))
print("올해는 "+ str(thisYear)+"입니다.")

age = int(input("몇 살이신지요?"))
total = 2050- thisYear+ age
print("2050년에는", str(total),"입니다.")
