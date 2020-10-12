import turtle

# 전역 변수 부분
a,b,num=0,0,0
swidth,sheight=1000,300
curX,curY=0,0

# 메인 코드 부분
if __name__ ==  "__main__" :
    turtle.title("거북이로 두 숫자 비트 논리곱(&) 연산하기")
    turtle.shape("turtle")
    turtle.setup(width = swidth +50 , height = sheight+ 50)
    turtle.screensize(swidth,sheight)
    turtle.penup()
    turtle.left(90)

    def binarynum (bin,num):
        curX= swidth/2
        for i in range(len(bin)-2):
            turtle.goto(curX,curY)
            if num &1:
                turtle.color('red')
                turtle.turtlesize(2)
            else:
                turtle.color('blue')
                turtle.turtlesize(1)
            turtle.stamp()
            curX -= 50
            num >>=1

    a = int(input("첫번째 숫자를 입력해주세요: "))
    b = int(input("두번째 숫자를 입력해주세요: "))
    bina = bin(a)
    binb = bin(b)
    result = a& b
    resultbin = bin(result)
       

    curY= 50
    binarynum(bina,a)
    curY=0
    binarynum(binb,b)
    curY=-50
    binarynum(resultbin,result)



turtle.done()

# 비트 논리곱을 구현하려고 숫자를 2개 입력받아서 각 숫자에 대한 2진수와 비트 논리곱결과 2진수를 출력하기