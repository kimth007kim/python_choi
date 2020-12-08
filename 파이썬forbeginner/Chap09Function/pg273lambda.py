def outFunc(v1,v2):
    def inFunc(num1,num2):
        return num1+num2
    return inFunc(v1,v2)
print(outFunc(10,20))

def hap(num1,num2):
    res = num1+num2
    return res
print(hap(10,20))

hap2 = lambda num1,num2 : num1+num2
print(hap2(10,20))

hap3 = lambda num1= 10,num2=20: num1+num2
print(hap3())
print(hap3(100,200))


myList=[1,2,3,4,5]
def add10(num):
    return num+10

for i in range(len(myList)):
    myList[i]= add10(myList[i])
print(myList)