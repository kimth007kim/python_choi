yr  = int(input("연도를 입력해주세요"))

if((yr % 4 ==0 and yr % 100 != 0) or yr % 400 == 0):
    print(yr,"년은 윤년입니다.")
else:
    print(yr,"년은 윤년이 아닙니다.")
 