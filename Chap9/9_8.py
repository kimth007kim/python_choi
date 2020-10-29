heroes= ["아이언맨","토르","헐크","스칼렛 위치"]
heroes.remove("스칼렛 위치")
print(heroes)
# heroes.remove("슈퍼맨") 에러남

heroes1=["아이언맨","토르","헐크","스칼렛 위치"]
del heroes1[0]
print(heroes1)

heroes2=["아이언맨","토르","헐크","스칼렛 위치"]
last_hero = heroes2.pop()
print(last_hero)