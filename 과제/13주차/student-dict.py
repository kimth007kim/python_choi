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

    students[name]={"kor":kor , "math":math, "eng":eng,"sum":0, "avg":0.0}
    print(students)
    print(students.keys(),students.values())

def print_student():

    for key in students.keys():
        print("Name :", key)
        print(" Kor :", students[key]["kor"])
        print(" Math :", students[key]["math"])
        print(" Eng :", students[key]["eng"])
        print(" Sum :", students[key]["sum"], "Avg :",students[key]["avg"])

def compute_score():
    global students

    for key in students.keys():
        print("Name : ",key)
        print(" Kor :", students[key]["kor"])
        print(" Math :", students[key]["math"])
        print(" Eng :", students[key]["eng"])
        students[key]["sum"]=students[key]["kor"]+students[key]["math"]+students[key]["eng"]
        students[key]["avg"]= students[key]["sum"]/3

for i in range(3):
    read_student()
    compute_score()
    print_student()