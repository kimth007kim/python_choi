# tt1=(10,20,30,40)
# tt1.append(40)
# tt1[0]=40
# del(tt1[0])
# print(tt1)
# del(tt1)
# print(tt1)
# print(tt1[0])
# print(tt1[0]+tt1[1]+tt1[2])
# print(tt1[1:3])
# print(tt1[1:])
# print(tt1[:3])
# tt2=('A','B')
# print(tt1+tt2)
# print(tt2*3)

tt= ((1,2,3),(4,5,6),(7,8,9))
# print(tt[1][1])

## Self STUDY 7-4
for i in range (0,3):
    for k in range(0,3):
        print(tt[i][k],end=" ")
    print("")


myTuple=(10,20,30)
myList=list(myTuple)
print("myList",myList)
myList.append(40)
myTuple=tuple(myList)
print("myTuple",myTuple)
