import sys

global hak,name
global kor,math,eng
global clkoravg,clmathavg,clengavg,myavg,clavg

def read_student():
    global hak
    global name
    global kor,math,eng
    global mysum

    hak = int(input("학번을 입력하시오 : "))
    if hak== -1:
        return(-1)

    name= input("이름을 입력하시오 :")
    
    kor = int(input("국어점수 :"))
    result = iscorrect_score(kor)
    if result == -1:
        print("올바르지 않은 국어 점수",kor)
        return(-2)

    math = int(input("수학점수 :"))
    result = iscorrect_score(math)
    if result == -1:
        print("올바르지 않은 수학 점수",math)
        return(-2)

    eng = int(input("영어점수 :"))
    result = iscorrect_score(eng)
    if result == -1:
        print("올바르지 않은 국어 점수",eng)
        return(-2)
    
    mysum = kor+math+eng
    

    return 0

def print_student():

    print("-"*40)
    print("학번 :",hak, "이름: ", name, 
        "국어 :", kor, ckor, ekor,
        "수학 :", math, cmath, emath,
        "영어 :", eng, ceng, eeng,
        "평균 :", myavg)

def print_class():
    global clkoravg,clmathavg,clengavg,myavg,clavg

    clkoravg=clkorsum/no_of_std
    clmathavg=clmathsum/no_of_std
    clengavg= clengsum/no_of_std
    clavg = (clkoravg + clmathavg+ clengavg)/3
    
    print("-"*40)
    print("학급 전체 평균 : %.2f" %clavg)
    print("국어 평균 : %.2f 수학 평균 : %.2f 영어 평균 : %.2f" %(clkoravg,clmathavg,clengavg))
    print("-"*40)

def iscorrect_score(score):
    if score<0 or score>100:
        return -1
        
def compute_score(score):
    if score >=90 and score<=100:
        return 'A'
    elif score >=80 and score<=89:
        return 'B'
    elif score >=70 and score<=79:
        return 'C'
    elif score >=60 and score<=69:
        return 'D'
    else:
        return 'F'

def e_compute_score(score):
    if score >=90 and score<=100:
        return 4.0
    elif score >=80 and score<=89:
        return 3.0
    elif score >=70 and score<=79:
        return 2.0
    elif score >=60 and score<=69:
        return 1.0
    else:
        return 0.0

def s_init():
    global clkorsum, clmathsum, clengsum
    global clkoravg,clmathavg,clengavg
    global no_of_std

    no_of_std=0
    clkorsum = clmathsum = clengsum = 0.0
    clkoravg = clmathavg = clengavg = 0.0

# 시작

s_init()

for i in range(3):
    result=read_student()
    if result == -1:
        if no_of_std == 0:
            print("0명의 학생입니다.")
            break
        else:
            break
    elif result == -2:
        print("점수 오류")
        sys.exit()

    ckor = compute_score(kor)
    cmath = compute_score(math)
    ceng = compute_score(eng)
    

    ekor = e_compute_score(kor)
    emath = e_compute_score(math)
    eeng = e_compute_score(eng)

    myavg= (ekor+emath+eeng)/3

    clkorsum += ekor
    clmathsum += emath
    clengsum += eeng

    no_of_std += 1
    print_student()
    # for 문
if no_of_std !=0:
    print_class()