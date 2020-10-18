def add(a,b):
    result = a+b
    print( "(" , str(a) + " + " , str(b) + ") " , "=" ,result)
def sub(a,b):
    result = a-b
    print( "(" , str(a) + " - " , str(b) + ") " , "=" ,result)
    
def mul(a,b):
    result = a*b   
    print( "(" , str(a) + " * " , str(b) + ") " , "=" ,result)

def div(a,b):
    if a>b:
        if b==0:
            print("0으로 나눌수 없습니다.")
        else:
            result = a/b
            print( "(" , str(a) + " ÷ " , str(b) + ") " , "=" ,result)
            
    elif a<b:
        if a==0:
            print("0으로 나눌수 없습니다.")
        else:
            result = b/a
            print( "(" , str(b) + " ÷ " , str(a) + ") " , "=" ,result)
            

n1= int(input("첫번째 수를 입력해주세요: "))
n2= int(input("두번째 수를 입력해주세요: "))
gg = input("식을 입력하세요")

if gg=="add":
    add(n1,n2)
elif gg == "sub":
    sub(n1,n2)
elif gg == "mul":
    mul(n1,n2)
elif gg == "div":
    div(n1,n2)
else:
    print("그런식은 없습니다.")
    