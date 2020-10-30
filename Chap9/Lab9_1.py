import random 

quotes=[]

quotes.append("그라운드안에 내가 있고 내안에 그라운드가 있다.")
quotes.append("월드컵은 경험하는 자리가 아니라 증명하는 자리다.")
quotes.append("닮고 싶은 사람은 있지만, 되고 싶은 사람은 없다.")
quotes.append("힘든가? 하지만 오늘 걸으면 내일은 뛰어야한다.")
quotes.append("나는 기록을 보지 않는다. 다만 기록이 나를 볼 뿐이다.")
quotes.append("무언가를 변화시키기 위해서는 나 자신부터 바꿔야한다.")


today=random.choice(quotes)

print("#"*39)
print("############# 오늘의 속담 #############")
print(today)
print("#"*39)