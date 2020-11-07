year = int(input("년도를 입력해주세요 윤년을 계산합니다."))

if (year % 4==0 and year % 100 !=0) or year % 400==0:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")