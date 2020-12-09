from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

filename = ""
 
def func_open() :
    global filename     
    filename = askopenfilename(parent = window, filetypes =
    (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
 
def func_exit() :
    window.quit()
    window.destroy()
 
def func_zoom() :  
    value = askinteger("확대배수", "확대할 배수를 입력하세요(2~10)", minvalue = 2, maxvalue = 10) 
    photo = PhotoImage(file = filename) 
    photo = photo.zoom(value,value)
    pLabel.configure(image = photo) 
    pLabel.image = photo
 
def func_subsample() : 
    value = askinteger("축소배수", "축소할 배수를 입력하세요(2~10)", minvalue = 2, maxvalue = 10) 
    photo = PhotoImage(file = filename) 
    photo = photo.subsample(value,value) 
    pLabel.configure(image = photo) 
    pLabel.image = photo
 
window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")
 
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)
 
mainMenu = Menu(window)
window.config(menu = mainMenu)
 
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

imageMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지 효과", menu = imageMenu)
imageMenu.add_command(label = "확대하기", command = func_zoom)
imageMenu.add_separator()
imageMenu.add_command(label = "축소하기", command = func_subsample)
 
window.mainloop()

# ## 10.22
# from tkinter import *
# from tkinter.filedialog import *

# ## 함수 선언 부분 ##
# def func_open():
#     filename=askopenfilename(parent=window,filetypes=(("GIF 파일", "*.gif"),("모든파일","*.*")))
#     photo=PhtoImage(file=filename)
#     pLabel.configure(image=photo)
#     pLabel.image= photo

# def func_exit():
#     window.quit()
#     window.destroy()

# ## 메인코드 부분 ##
# window = Tk()
# window.geometry("400x400")
# window.title("명화 감상하기")
# photo=PhotoImage()
# pLabel=Label(window,image=photo)
# pLabel.pack(expand=1,anchor=CENTER)


# mainMenu=Menu(window)
# window.config(menu=mainMenu)
# fileMenu=Menu(mainMenu)
# mainMenu.add_cascade(label="파일",menu=fileMenu)
# fileMenu.add_command(label="열기",command=func_open)
# fileMenu.add_separator()
# fileMenu.add_command(label="종료",command=func_exit)

# window.mainloop()

# ## 10.21
# from tkinter import *
# from tkinter.filedialog import *

# ## 함수 선언 부분 ##
# window = Tk()
# window.geometry("400x100")

# label1=Label(window,text="선택된 파일 이름")
# label1.pack()

# saveFp=asksaveasfile(parent=window,mode="w",defaultextension=".jpg",filetypes=(("JPG 파일", "*.jpg;*.jpeg"),("모든파일","*.*")))

# label1.configure(text=saveFp)
# saveFp.close()
# window.mainloop()

# ## 10.20
# from tkinter import *
# from tkinter.filedialog import *

# ## 함수 선언 부분 ##
# window = Tk()
# window.geometry("400x100")

# label1=Label(window,text="선택된 파일 이름")
# label1.pack()

# filename=askopenfilename(parent=window,filetypes=(("GIF 파일", "*.gif"),("모든파일","*.*")))

# label1.configure(text=str(filename))
# window.mainloop()

# ## 10.19
# from tkinter import *
# from tkinter.simpledialog import *

# ## 함수 선언 부분 ##
# window = Tk()
# window.geometry("400x100")

# label1=Label(window,text="입력된 값")
# label1.pack()

# value=askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요",minvalue=1,maxvalue=6)

# label1.configure(text=str(value))
# window.mainloop()

# ## 10.18
# from tkinter import *
# from tkinter import messagebox

# ## 함수 선언 부분 ##
# def func_open():
#     messagebox.showinfo("메뉴선택","열기 메뉴를 선택함")

# def func_exit():
#     window.quit()
#     window.destroy()

# ##메인 코드 부분
# window = Tk()

# mainMenu=Menu(window)
# window.config(menu=mainMenu)

# fileMenu=Menu(mainMenu)
# mainMenu.add_cascade(label="파일",menu=fileMenu)
# fileMenu.add_command(label="열기",command=func_open)
# fileMenu.add_separator()
# fileMenu.add_command(label="종료",command=func_exit)

# window.mainloop()
## 10.17
# from tkinter import *

# window = Tk()

# mainMenu=Menu(window)
# window.config(menu=mainMenu)

# fileMenu=Menu(mainMenu)
# mainMenu.add_cascade(label="파일",menu=fileMenu)
# fileMenu.add_command(label="열기")
# fileMenu.add_separator()
# fileMenu.add_command(label="종료")

# window.mainloop()

# ## 10.16
# from tkinter import *
# from tkinter import messagebox

# ## 함수 선언 부분 ##
# def keyEvent(event):
#     messagebox.showinfo("키보드 이벤트","눌린 키 : "+ chr(event.keycode))
# ## 메인 코드 부분 ##

# window = Tk()

# window.bind("<Key>",keyEvent)
# window.mainloop()

## 10.15
# from tkinter import *
# from tkinter import messagebox

# ## 함수 선언 부분 ##
# def clickMouse(event):
#     txt= ""
#     if event.num ==1:
#         txt += "마우스 왼쪽 버튼이 ("
#     if event.num ==3:
#         txt += "마우스 오른쪽 버튼이 ("

#     txt += str(event.y)+","+str(event.x)+")에서 클릭됨"
#     label1.configure(text=txt)
    
# ## 메인 코드 부분 ##

# window = Tk()
# window.geometry("400x400")

# label1= Label(window,text="이곳이 바뀜")

# window.bind("<Button>",clickMouse)
# label1.pack(expand=1,anchor=CENTER)
# window.mainloop()

# ## 10.14
# from tkinter import *
# from tkinter import messagebox

# ## 함수 선언 부분 ##
# def clickImage(event):
#     messagebox.showinfo("마우스","여우에서 마우스가 클릭됨")

# ## 메인 코드 부분 ##

# window = Tk()
# window.geometry("400x400")

# photo=PhotoImage(file="/Users/Kyungdong/Documents/python_choi/과제/14주차/5.gif")
# label1= Label(window,image=photo)

# label1.bind("<Button>",clickImage)
# label1.pack(expand=1,anchor=CENTER)
# window.mainloop()


# ## 10.13
# from tkinter import *
# from tkinter import messagebox

# ## 함수 선언 부분 ##
# def clickLeft(event):
#     messagebox.showinfo("마우스","마우스 왼쪽 버튼이 클릭됨")

# ## 메인 코드 부분 ##

# window = Tk()
# window.bind("<Button-1>",clickLeft)
# window.mainloop()

## 10.12
# from tkinter import *
# from time import *

# ## 전역 변수 선언 부분 ##

# fnameList= ["1.gif","2.gif","3.gif","4.gif","5.gif","6.gif","7.gif","8.gif","9.gif"]
# phtoList=[None] * 9
# num=0

# ## 함수 선언 부분 ##
# def clickNext():
#     global num
#     num +=1
#     if num>8:
#         num = 0
#     photo=PhotoImage(file="/Users/Kyungdong/Documents/python_choi/과제/14주차/"+fnameList[num])
#     pLabel.configure(image=photo)
#     pLabel.image=photo
#     name.configure(text=fnameList[num])

# def clickPrev():
#     global num
#     num -=1
#     if num<0:
#         num = 8
#     photo=PhotoImage(file="/Users/Kyungdong/Documents/python_choi/과제/14주차/"+fnameList[num])
#     pLabel.configure(image=photo)
#     pLabel.image=photo
#     name.configure(text=fnameList[num])

# ## 메인 코드 부분 ##
# window = Tk()
# window.geometry("700x500")
# window.title("사진 앨범 보기")

# btnPrev=Button(window,text="<< 이전",command=clickPrev)
# btnNext=Button(window,text="다음 >>",command=clickNext)

# photo=PhotoImage(file="/Users/Kyungdong/Documents/python_choi/과제/14주차/"+fnameList[0])
# pLabel= Label(window,image=photo)
# name = Label(window,text=fnameList[0])

# btnPrev.place(x=250,y=10)
# btnNext.place(x=400,y=10)
# pLabel.place(x=15,y=50)
# name.place(x=325,y=10)

# window.mainloop()

