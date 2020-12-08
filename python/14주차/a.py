# 10.12
from tkinter import *
from time import *

## 전역 변수 선언 부분 ##

fnameList= ["1.gif","2.gif","3.gif","4.gif","5.gif","6.gif","7.gif","8.gif","9.gif"]
phtoList=[None] * 9
num=0

## 함수 선언 부분 ##
def clickNext():
    global num
    num +=1
    if num>8:
        num = 0
    photo=PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    name.configure(text=fnameList[num])

def clickPrev():
    global num
    num -=1
    if num<0:
        num = 8
    photo=PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image=photo
    name.configure(text=fnameList[num])

## 메인 코드 부분 ##
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
