# coffee= 0

# coffee = int(input("어떤 커피 드릴까요?(1:보통 ,2:설탕,3:블랙)"))

# print()
# print("#1. 뜨거운 물을 준비한다.")
# print("#2. 종이컵을 준비한다.")

# if coffee ==1:
#     print("#3. 보통커피를 탄다.")
# elif coffee ==2:
#     print("#3. 설탕커피를 탄다.")
# elif coffee ==3:
#     print("#3. 블랙커피를 탄다.")
# else:
#     print("#3. 아무거나 탄다.\n")

# print("#4. 물을 붓는다.")
# print("#5. 스푼으로 젓는다.")
# print()
# print("손님~ 커피 여기 있습니다.")


##전역 변수 선언 부분##
# coffee= 0

# ##함수 선언 부분##
# def coffee_machine(button): 
#     print()
#     print("#1. 뜨거운 물을 준비한다.")
#     print("#2. 종이컵을 준비한다.")

#     if coffee ==1:
#         print("#3. 보통커피를 탄다.")
#     elif coffee ==2:
#         print("#3. 설탕커피를 탄다.")
#     elif coffee ==3:
#         print("#3. 블랙커피를 탄다.")
#     else:
#         print("#3. 아무거나 탄다.\n")

#     print("#4. 물을 붓는다.")
#     print("#5. 스푼으로 젓는다.")
#     print()
# ## 메인 코드 부분##
# coffee = int(input("어떤 커피 드릴까요?(1:보통 ,2:설탕,3:블랙)"))
# coffee_machine(coffee)
# print("손님~ 커피 여기 있습니다.")

# #함수 선언 부분##

# def plus(v1,v2):
#     result = 0
#     result= v1+v2
#     return result

# #전역 변수 선언 부분 ##
# hap=0

# #메인 코드 부분##
# hap=plus(100,200)
# print("100과 200의 plus() 함수 결과는 %d" % hap)

## 함수 선언 부분 ##

# def calc(v1,v2,op):
#     result=0
#     if op == '+' :
#         result= v1+v2
#     if op == '-' :
#         result= v1-v2
#     if op == '*' :
#         result= v1*v2
#     if op == '/' :
#         result= v1/v2
        
#     return result

# ## 전역 변수 선언 부분 ##
# res= 0
# var1,var2,oper =0,0,""

# ## 메인 코드 부분 ## 
# oper =input("계산을 입력하세요(+,-,*,/):")
# var1 = int(input("첫 번째 수를 입력하세요 : "))
# var2 = int(input("두 번째 수를 입력하세요 : "))

# res = calc(var1,var2,oper)

# print("##계산기 : %d %s %d = %d" % (var1,oper,var2,res))

##함수 선언부분 ##

# def multi(v1,v2):
#     retList=[]
#     res1= v1+v2
#     res2 = v1-v2
#     retList.append(res1)
#     retList.append(res2)
#     return retList

# ## 전역 변수 선언 부분 ##
# myList = []
# hap,sub=0,0

# ##메인 코드 부분 ##
# myList = multi(100,200)
# hap=myList[0]
# sub=myList[1]
# print("multi()에서 돌려준 값 ==> %d, %d" % (hap,sub))

##함수 선언 부분 ##
def para_func(*para):
    result=0
    for num in para:
        result =result+num
    return result

##전역 변수 선언 부분 ##
hap=0

##메인 코드 부분 ##
hap = para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" %hap)
hap = para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" %hap)