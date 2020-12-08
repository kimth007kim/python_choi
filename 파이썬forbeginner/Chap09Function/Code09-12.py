##함수 선언 부분 ##
def para_func(*para):
    result=0
    for num in para:
        result = result +num
    return result
    
## 전역 변수 선언 부분 ##
hap=0

## 메인 코드 부분 ##
hap = para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" %hap)
hap = para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" %hap)

hap= para_func(10,20,30,40,50,60,70,80,90,100)
print(hap)

def dic_func(**para):
    for k in para.keys():
        print("%s--> %d명입니다." %(k,para[k]))

dic_func(트와이스=9,소녀시대=7,걸스데이=4,블랙핑크=4)