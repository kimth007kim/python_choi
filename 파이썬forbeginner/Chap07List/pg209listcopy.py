# 얕은 복사 현상
oldList=['짜장면','탕수육','군만두']
newList= oldList
print(newList)
oldList[0]='짬뽕'
oldList.append('깐풍기')
print(newList)

# 깊은 복사
oldList=['짜장면','탕수육','군만두']
newList= oldList[:]
print(newList)
oldList[0]='짬뽕'
oldList.append('깐풍기')
print(newList)
