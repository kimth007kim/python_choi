
# -*- coding: utf-8 -*-

global name
global kor,math,eng
global students
global avg,sum

students=dict()
def read_student():
    global name
    global kor,math,eng
    global students

    name=input("이름을 입력하시오 :")
    kor =int(input("국어점수:"))
    math =int(input("수학점수:"))
    eng =int(input("영어점수:"))

    students[name]={"국어":kor , "수학":math, "영어":eng,"합계":0, "평균":0.0}
    print(students)
    print(students.keys(),students.values())

def print_student():

    for key in students.keys():
        print("이름 :", key,end="")
        print(" 국어 :", students[key]["국어"])
        print(" 수학 :", students[key]["수학"])
        print(" 영어 :", students[key]["영어"])
        print(" 합계 :", students[key]["합계"], "평균 :",students[key]["평균"])

def compute_score():
    global students

    for key in students.keys():
        print("이름 : ",key)
        print(" 국어 :", students[key]["국어"])
        print(" 수학 :", students[key]["수학"])
        print(" 영어 :", students[key]["영어"])
        students[key]["합계"]=students[key]["국어"]+students[key]["수학"]+students[key]["영어"]
        students[key]["평균"]= students[key]["합계"]/3

for i in range(3):
    read_student()
    compute_score()
    print_student()