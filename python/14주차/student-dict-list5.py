# -*- coding: utf-8 -*-

import sys

students=dict()

kor_sum=0.0
eng_sum=0.0
math_sum=0.0
kor_avg =0.0
eng_avg=0.0
math_avg=0.0
class_avg=0.0
count=0

def read_student():

    global students,count
    filep = open("C://2020_0210/datafile.txt","r")
    for line in filep:
        line = line.rstrip()
        field= line.split()
        std_nbr=int(field[0])

        if std_nbr == -1:
            if count == 0:
                print("학생 수가 0명입니다.")
                continue
            else:
                break
        name =field[1]
        sex=field[2]
        kor=int(field[3])

        if kor> 100 or kor<0:
            print("국어 점수 오류 :",end='')
            sys.exit()
        eng=int(field[4])
        if eng> 100 or eng<0:
            print("국어 점수 오류 :",end='')
            sys.exit()
        math=int(field[5])
        if math> 100 or math<0:
           print("국어 점수 오류 :",end='')
           sys.exit()

       
        students[std_nbr]= {"name":name,"sex":sex,"kor":kor,"ckor":'',"fkor":0.0,"eng":eng,"ceng":'',"feng":0.0,"math":math,"cmath":'',"fmath":0.0,"sum":0,"avg":0.0}
        count+=1
    # students[name]={"국어":kor , "수학":math, "영어":eng,"합계":0, "평균":0.0}
    # print(students)
    # print(students.keys(),students.values())

def print_student():

    for list in sorted(students.keys()):
        print( "학번 : %d 이름 : %s" %(list,students[list][0]))
        print(" 국어 : %d %.1f %c" %(students[list][1],students[list][2],students[list][3]))
        print(" 수학 : %d %.1f %c" %(students[list][4],students[list][5],students[list][6]))
        print(" 영어 : %d %.1f %c" %(students[list][7],students[list][8],students[list][9]))
        print(" 평균 학점 : %.2f\n"%(students[list][10]))

        print(" 학급 국어 학점 : %.2f 학급 영어 평균: %.2f 학급 수학 평균: %.2f"%(kor_avg,eng_avg,math_avg))
        print(" 학급 전체 평균 : %.2f"%(class_avg))

def compute_score():
    global kor_sum,eng_sum,math_sum
    global kor_avg,eng_avg,math_avg,class_avg

    for list in sorted(students.keys()):
        k_score,kc_score= trans_score(students[list]["kor"])
        e_score,ec_score= trans_score(students[list]["eng"])
        m_score,mc_score= trans_score(students[list]["math"])
        
        students[list]["fkor"]=k_score
        students[list]["feng"]=e_score
        students[list]["fmath"]=m_score

        students[list]["ckor"]=kc_score
        students[list]["ceng"]=ec_score
        students[list]["cmath"]=mc_score

        avg =(students[list]["kor"]+students[list]["feng"]+students[list]["fmath"])/3
        students[list]["avg"]=avg

        kor_sum= kor_sum+students[list]["fkor"]
        eng_sum= eng_sum+students[list]["feng"]
        math_sum= math_sum+students[list]["fmath"]

    kor_avg=kor_sum/float(count)
    eng_avg=eng_sum/float(count)
    math_avg=math_sum/float(count)
    class_avg=(kor_avg+eng_avg+math_avg)/3

def trans_score(score):
    if score >=90 and score <=100:
        return 4.0,'A'
    elif score >=80 and score <=89:
        return 3.0,'B'
    elif score >=70 and score <=79:
        return 2.0,'C'
    elif score >=60 and score <=69:
        return 1.0,'D'
    else:
        return 0.0,'F'


read_student()
compute_score()
print_student()