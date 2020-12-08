mySet1={1,2,3,3,3,4}
print(mySet1)

salesList=['삼각김밥','바나나','도시락','삼각김밥','삼각김밥','도시락','삼각김밥']
print(set(salesList))

mySet1={1,2,3,4,5}
mySet2={4,5,6,7}
print(mySet1 & mySet2)
print(mySet1 | mySet2)
print(mySet1 - mySet2)
print(mySet1 ^ mySet2)

print(mySet1.intersection(mySet2))
print(mySet1.union(mySet2))
print(mySet1.difference(mySet2))
print(mySet1.symmetric_difference(mySet2))
