# coffee=0

coffee= int(input("어떤 커피를 드릴까요?(1:보통,2:설탕,3:블랙)"))

print()
print("#1. 뜨거운 물을 준비한다. ")
print("#2. 종이컵을 준비한다. ")

if coffee==1:
    print("#3. 보통 커피를 탄다.")
elif coffee==2:
    print("#3. 설탕 커피를 탄다.")
elif coffee==3:
    print("#3. 블랙 커피를 탄다.")
else:
    print("#3. 아무거나 탄다.\n")

print("#4. 물을 붓는다.. ")
print("#5. 종이컵을 준비한다. ")
print()
print("손님~ 커피 여기 있습니다.")
