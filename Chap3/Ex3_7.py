import time

fseconds = time.time()
now_minute = time.time() // 60
minute = now_minute % 60
hour = now_minute //60 %24

print("현재 시간(영국 그리니치 시각):", hour+1, "시", minute, "분")