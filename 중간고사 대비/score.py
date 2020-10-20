global name
global kor
global math
global eng 
global avg
global summ

def read_student():
    global name
    global kor
    global math
    global eng

    name = input("이름을 입력하시오 :")
    kor = int(input("국어점수 :"))
    math = int(input("수학점수 :"))
    eng = int(input("영어점수 :"))
    
def print_student():

    print("이름: ", name, "국어 :", kor, ckor,
         "수학 :", math, cmath ,
         "영어: ", eng, ceng)
# def print_student():

#     print("이름: ",name,"국어 :",kor, "수학 :",math,"영어 :",eng,"합 :",summ, "평균 :",avg)

# def compute_score():
#     global avg
#     global summ

#     summ = kor+eng+math
#     avg=summ/3

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

for i in range(3):
    read_student()
    # compute_score()
    ckor = compute_score(kor)
    cmath = compute_score(math)
    ceng = compute_score(eng)
    print_student()