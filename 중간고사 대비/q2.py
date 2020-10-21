# 구구단 프로그램을 작성하라: 반복문 중첩

# x,y=0,0

# for x in range(2,10):
#     for y in range(1,10):
#         print( x,"x",y,"=",x*y)
#     print()

i= 1
j= 1

while i<=9:
    while j<=9:
        print("%d * %d = %d " %(i,j,i*j))
        j=j+1
    print("\n")
    j=1
    i=i+1