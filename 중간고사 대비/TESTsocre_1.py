import sys
global name,hak,kor,math,eng
global clkoravg,clmathavg,clengavg

def read_student():
    global name,hak
    global kor,math,eng

    hak= int(input("학번을 입력헤주세요"))
    if hak== -1: 
        return -1
    name= input("이름을 입력하여 주세요")

    kor = int(input("국어 성적을 입력해주세요"))
    result=iscorrect_score(kor)
    if result ==-1:
        print("올바르지 않은 성적입니다.")
        return -2
    math = int(input("수학 성적을 입력해주세요"))
    result=iscorrect_score(math)
    if result ==-1:
        print("올바르지 않은 성적입니다.")
        return -2
    eng = int(input("영어 성적을 입력해주세요"))
    result=iscorrect_score(eng)
    if result ==-1:
        print("올바르지 않은 성적입니다.")
        return -2

def print_student():
    print("-"*40)
    print()

def print_class():
    print()

def compute_score(score):
    if score>= 90 and score<=100:
        return('A',4.0)
    if score>= 80 and score<=89:
        return('B',3.0)
    if score>= 70 and score<=79:
        return('C',2.0)
    if score>= 60 and score<=69:
        return('D',1.0)
    else:
        return('F',0.0)

def iscorrect_score(score):
    if score>100 or score<0:
        return -1

def s_init():
    global clkoravg,clmathavg,clengavg
    global clkorsum,clmathsum,clengsum
    global no_of_std
    clkoravg=clmathavg=clengavg=0.0
    clkorsum=clmathsum=clengsum=0.0
    no_of_std=0

s_init()
while True:
    result = read_student()
    if result == -1:
        if no_of_std==0:
            print("학생이 0명입니다.")
            break
        else:
            break
    elif result ==-2:
        print("정수 오류")
        sys.exit()

    ekor,ckor =compute_score(kor)
    emath,cmath =compute_score(math)
    eeng,ceng =compute_score(eng)

    clkorsum+=ekor