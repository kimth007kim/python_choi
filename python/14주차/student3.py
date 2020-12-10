import sys

students=dict()
kor_sum=0.0
eng_sum=0.0
math_sum=0.0
kor_avg=0.0
eng_avg=0.0
math_avg=0.0
class_avg=0.0
count=0


def read_students():
    global count
    outfile= open("C://2020_0210/datafile.txt","w")
    while True:
        std_num= input("학번:")
        if std_num==-1:
            if count==0:
                print("학생수 0명")
                continue
            else:
                break
        name = input("이름: ")
        sex = input("성별 (m/f): ")
        kor = int(input("국어 성적"))
        if kor>100 or kor<0:
            print("잘못된 국어성적 %d",kor)
            sys.exit()
        eng = int(input("영어 성적"))
        if kor>100 or kor<0:
            print("잘못된 영어성적 %d",kor)
            sys.exit()
        math = int(input("수학 성적"))
        if kor>100 or kor<0:
            print("잘못된 수학성적 %d",kor)
            sys.exit()

        outfile.write(std_num)
        outfile.write(" ")
        outfile.write(name)
        outfile.write(" ")
        outfile.write(sex)
        outfile.write(" ")
        outfile.write(str(kor))
        outfile.write(" ")
        outfile.write(str(eng))
        outfile.write(" ")
        outfile.write(str(math))
        outfile.write(" ")
        outfile.write("\n")
        count+=1

    outfile.close()    
    

def fread_students():
    global count,students
    filep= open("C://2020_0210/datafile.txt","w")
    for line in filep:
        line=line.rstrip()
        field= line.split()
        wcount=0

        for word in field:
            if wcount==0:
                std_num=word
            elif wcount==1:
                name=word
            elif wcount==2:
                sex=word
            elif wcount==3:
                kor=int(word)
            elif wcount==4:
                eng=int(word)
            else:
                math=int(word)
            wcount+=1

        students[std_num]={"name":name,"sex":sex,"kor":kor,"ckor":'',"fkor":0.0,"eng":eng,"ceng":'',"feng":0.0,"math":math,"cmath":'',"fmath":0.0,"avg":0.0,"sum":0}
        count+=1
        wcount=0
        


def compute_score():
    global kor_sum,eng_sum,math_sum
    global kor_avg,eng_avg,math_avg,class_avg

    for keyval in sorted (students.keys()):
        k_score,kc_score= trans_score(students[keyval]["kor"])
        e_score,ec_score= trans_score(students[keyval]["eng"])
        m_score,mc_score= trans_score(students[keyval]["math"])

        students[keyval]["fkor"]=k_score
        students[keyval]["feng"]=e_score
        students[keyval]["fmath"]=m_score
        
        students[keyval]["ckor"]=kc_score
        students[keyval]["ceng"]=ec_score
        students[keyval]["cmath"]=mc_score

        avg= (students[keyval]["fkor"]+students[keyval]["feng"]+students[keyval]["fmath"])/3
        students[keyval]["avg"]=avg

        kor_sum=kor_sum+ students[keyval]["fkor"]
        eng_sum=eng_sum+ students[keyval]["feng"]
        math_sum=math_sum+students[keyval]["fmath"]
    
    kor_avg=kor_sum/count
    eng_avg=eng_sum/count
    math_avg=math_sum/count
    class_avg=(kor_avg+eng_avg+math_avg)/3
    




def print_students():
    print()

def trans_score(score):
    if score>=90 and score<=100:
        return 4.0,'A'
    elif score>=80 and score <=89:
        return 3.0,'B' 
    elif score>=70 and score <=79:
        return 2.0,'C' 
    elif score>=60 and score <=69:
        return 1.0,'D' 
    else:
        return 0.0,'F' 
    
    



read_students()
fread_students()
compute_score()
print_students()