upper, lower, number, kor, etc = [0] * 5
inStr = ""
 
inStr = input("문자열을 입력하세요 : ")

for x in inStr :
    if ord('A') <= ord(x) and ord(x) <= ord('Z') :  
        upper += 1
    elif ord('a') <= ord(x) and ord(x) <= ord('z') :  
        lower += 1
    elif ord('가') <= ord(x) and ord(x) <= ord('힣') : 
        kor += 1
    elif ord('0') <= ord(x) and ord(x) <= ord('9') : 
        number += 1
    else : 
        etc += 1
print("대문자 : %d 소문자 : %d 숫자 : %d 한글 : %d 기타 : %d " % (upper, lower, number, kor, etc))