# numList=[]
# for num in range(1,6):
#     numList.append(num)
# print(numList)

# numList=[num for num in range(1,6)]
# print(numList)
numList=[num* num for num in range(1,6)]
print(numList)

numList=[num for num in range(1,21) if num %3 ==0]
print(numList)