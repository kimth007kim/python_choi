####1번

import random
 
count1,count2,count3,count4,count5,count6= 0,0,0,0,0,0 

for i in range (0,1000):
    a = random.randrange(1,7) 
    if a == 1:
        count1 +=1
    elif a == 2:
        count2 +=1
    elif a == 3:
        count3 +=1
    elif a == 4:
        count4 +=1
    elif a == 5:
        count5 +=1
    elif a == 6:
        count6 +=1

print("주사위 1 : %d 번" %count1)
print("주사위 2 : %d 번" %count2)
print("주사위 3 : %d 번" %count3)
print("주사위 4 : %d 번" %count4)
print("주사위 5 : %d 번" %count5)
print("주사위 6 : %d 번" %count6)


####2번
import random

def getNumber():
    return random.randrange(1,46)

lotto = []
num=0

while True:
    num =getNumber()
    if lotto.count(num)==0:
        lotto.append(num)
    if len(lotto)>=6:
        break

print("이번주 로또 번호는 ", end='')
lotto.sort()
print("[",end='')
for i in range(0,6):
    if i >= 5:
        print("%d " %lotto[i],end='')
    else:
        print("%d, " %lotto[i],end='')
print("]",end='')


#### 4번

from tkinter import *
from time import *


fnameList= ["jeju1.gif","jeju2.gif","jeju3.gif","jeju4.gif","jeju5.gif"]
phtoList=[None] * 5
num=0

def clickNext():
    global num
    num +=1
    if num>4:
        num = 0
    photo=PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    name.configure(text=fnameList[num])

def clickPrev():
    global num
    num -=1
    if num<0:
        num = 4
    photo=PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    name.configure(text=fnameList[num])

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev=Button(window,text="<< 이전",command=clickPrev)
btnNext=Button(window,text="다음 >>",command=clickNext)

photo=PhotoImage(file=fnameList[0])
pLabel= Label(window,image=photo)
name = Label(window,text=fnameList[0])

btnPrev.place(x=250,y=10)
btnNext.place(x=400,y=10)
pLabel.place(x=15,y=50)
name.place(x=325,y=10)

window.mainloop()