# 10.12
from tkinter import *
from time import *

## 전역 변수 선언 부분 ##


## 메인 코드 부분 ##
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

photo=PhotoImage(file="2.gif")
pLabel= Label(window,image=photo)

pLabel.place(x=15,y=50)

window.mainloop()
