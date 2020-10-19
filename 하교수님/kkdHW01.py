# # 변수 선언 부분
# select,answer,numStr,num1,num2=0,0,"",0,0

# # 메인 코드 부분
# select = int(input("1.입력한 수식 계산 2.두 수 사이의 합계 : "))

# if select ==1:
#     numStr = input(" *** 수식을 입력하세요 : ")
#     answer = eval(numStr)
#     print(" %s 결과는 %5.1f입니다." % (numStr,answer))
# elif select==2:
#     num1 = int(input(" *** 첫 번째 숫자를 입력하세요: "))
#     num2 = int(input(" *** 두 번째 숫자를 입력하세요: "))
#     for i in range(num1,num2+1):
#         answer=answer+i
#     print("%d+...+%d는 %d입니다. " %(num1,num2,answer))
# else:
#     print("1 또는 2만 입력해야 합니다.")

# for i in range(2,-1,-1):
#     print("%d : 안녕하세요? for 문을 공부 중입니다. ^^" %i)
# for i in range(1,6,1):
#     print("%d " % i, end=" ")

# hap=1+2+3+4+5+6+7+8+9+10
# print("1에서 10까지의 합계 : %d" %hap)

# i=0
# hap=0
# for i in range(1,11,1):
#     hap= hap+i
# print("1에서 10까지의 합계 : %d" % hap)

# i,hap=0,0

# for i in range(501,1001,2):
#     hap=hap+i
# print("500과 1000 사이에 있는 홀수의 합계 : %d" % hap)

# i,hap=0,0
# num = 0
# num =int(input("값을 입력하세요 : "))

# for i in range(1,num+1,1):
#     hap= hap+i

# print("1에서 %d까지의 합계 : %d" % (num,hap))

# for i in range(0,3,1):
#     for k in range(0,2,1):
#         print("파이썬은 꿀잼입니다. ^^(i값: %d, k값:%d)" %(i,k))

# i,k,guguLine=0,0,""
# for i in range(2,10):
#     guguLine=guguLine+(" #  %d단  # " %i)
# print(guguLine)

# for i in range(1,10):
#     for k in range(2,10):
#         print("%2dX %2d= %2d" %(k,i,i*k),end=" ")
#     print()

i,k,guguLine=0,0,""
for i in range(9,1,-1):
    guguLine=guguLine+(" #  %d단  # " %i)
print(guguLine)

for i in range(9,0,-1):
    for k in range(9,1,-1):
        print("%2dX %2d= %2d" %(k,i,i*k),end=" ")
    print()

