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

# ss='파이썬최고!'

#sslen=len(ss)
# for i in range(0,sslen):
    # print(ss[i]+'$',end='')

# inStr,outStr="",""
# i=0
# inStr=input("문자열 입력: ")

# for i in range(0,len(inStr)):
#     out += inStr[len(inStr)-(i+1)]

# print("거꾸로 출력 : %s" % outStr)

# ss= '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠 ^^'
# ss.count('공부')
# print(ss.find('공부'),ss.rfind('공부'),ss.find('없다'))
# print(ss.index('공부'),ss.rindex('공부'),ss.index('공부',5))
# print(ss.starstwith('파이썬'),ss.start('파이썬',10),ss.endwith('^^'))

# ss= input("입력 문자열==>")
# print("출력 문자열 ==>", end=" ")

# if ss.startswith('(') ==False:
#     print("(",end=' ')

# print(ss,end=' ')

# if ss.endwith(')')==False:
#     print(")", end= '')

# inStr= " 한글 Python 프로그래밍 "
# outStr=""

# for i in range(0,len(inStr)):
#     if inStr[i] != ' ':
#         outStr += inStr[i]

# print("원래 문자열 ==>" + '[' + inStr + ']')
# print("공백 삭제 문자열 ==> " + '[' + outStr+ ']')

# ss=input("날짜(연/월/일==>")

# ssList=ss.split('/')

# print("입력한 날짜의 10년후 ==>", end= '')
# print(str(int(ssList[0])+10)+"년",end='')
# print(ssList[1]+"월",end='')
# print(ssList[2]+"일")

# import turtle
# import random
# from tkinter.simpledialog import *

# inStr=''
# swidth,sheight= 400,400
# tX,tY,txtSize=[0]*3

# if __name__ =="__main__":
#     turtle.title('거북2')
#     turtle.shape('turtle')
#     turtle.setup(width= swidth+50,height =sheight+50)
#     turtle.screensize(swidth,sheight)
#     turtle.penup()

#     inStr= asktring('','문자열 입력')

#     for ch in inStr:
#         tX= random.randrange(-swidth/2,swidth/2)
#         tY= random.randrange(-sheight/2,sheight/2)
#         r= random.random(); g= random.random(); b= random.random()
#         txtSize=random.randrange(10,50)

#         turtle.pencolor((r,g,b))
#         turtle.goto(tX,tY)
#         turtle.write(ch,font=('돋움',txtSize,'bold'))
#     turtle.done()