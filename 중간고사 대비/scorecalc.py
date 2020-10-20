import sys

global hak,name
global kor,math,eng
global ekor,emath,eeng
global ckor,cmath,ceng
global clkorsum,clmathsum,clengsum
global clkoravg,clmathavg,clengavg,clavg
global no_of_std
global mysum,myavg

def read_student():
    global hak,name
    global kor,math,eng

    hak= int(input("학번을 입력하시오: "))
    if hak == -1:
        return(-1)
    name= input("이름을 입력하시오:") 

    kor= int(input("국어 점수를 입력하시오: "))
    result=iscorrect_score(kor)
    if result == -1:
        print("올바르지 않은 국어 점수",kor)
        return(-2)
    math= int(input("수학 점수를 입력하시오: "))
    result=iscorrect_score(math)
    if result == -1:
        print("올바르지 않은 수학 점수",math)
        return(-2)
    eng = int(input("영어 점수를 입력하시오: "))
    result=iscorrect_score(eng)
    if result == -1:
        print("올바르지 않은 영어 점수",eng)
        return(-2)


def iscorrect_score(score):
    if score<0 or score>100:
        return -1

def print_student():
    print("-"*40)
    print("학번 :",hak,"이름 :",name,"국어 :",kor,ckor,ekor,"수학 :",math,cmath,emath,"영어 :",eng,ceng,eeng,"평균 : %2f" %(myavg))

def print_class():
    global clkoravg,clmathavg,clengavg,clavg
    clkoravg=clkorsum/no_of_std
    clmathavg=clmathsum/no_of_std
    clengavg=clengsum/no_of_std
    clavg= (clkoravg+clmathavg+clengavg)/3

    print("학급 전체 평균 : %2f" %(clavg))
    print("학급 국어 수학 영어 평균 : %2f %2f %2f" %(clkoravg,clmathavg,clengavg))
    print("-"*40)

def compute_score(score):
    if score >=90 and score<=100:
        return('A',4.0)
    elif score >=80 and score<=89:
        return('B',3.0)
    elif score >=70 and score<=79:
        return('C',2.0)
    elif score >=60 and score<=69:
        return('D',1.0)
    else:
        return('F',0.0)


def s_init():
    global clkorsum,clmathsum,clengsum
    global clkoravg,clmathavg,clengavg
    global no_of_std


    no_of_std=0
    clkorsum=clmathsum=clengsum=0.0
    clkoravg=clmathavg=clengavg=0.0

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

    ckor,ekor=compute_score(kor)
    cmath,emath=compute_score(math)
    ceng,eeng=compute_score(eng)

    clkorsum+=ekor
    clmathsum+=emath
    clengsum+=eeng

    mysum= ekor+emath+eeng
    myavg = mysum/3

    print_student()
    no_of_std+=1

if no_of_std !=0:
    print_class()




