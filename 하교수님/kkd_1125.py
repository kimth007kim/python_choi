# from tkinter import *

# window =Tk()
# window.mainloop()

# from tkinter import *
# from tkinter import messagebox

# def myF():
    # if ck.get()==0:
    #     messagebox.showinfo('','버튼 꺼짐')
    # else:
    #     messagebox.showinfo('','버튼 켜짐')

# def myF2():
    # if var.get() ==1:
    #     label1.configure(text='파이썬')
    # elif var.get() ==2:
    #     label2.configure(text='C++')
    # else:
    #     label3.configure(text='자바')

# window =Tk()
# window.title("윈도창 연습")
# window.geometry("400x400")
# window.resizable(width=FALSE ,height =FALSE)

# window.mainloop()

# from tkinter import *
# window =Tk()

# label1 =Label(window, text="COOKBOOK~~ Python을")
# label2 =Label(window, text="열심히",font=("궁서체",30),fg="blue")
# label3 =Label(window, text="공부 중입니다.",bg="magenta",width=20,height=5, anchor =SE)

# photo= PhotoImage(file='gif/dog.gif')
# photo2= PhotoImage(file='gif/cat.gif')

# label4=Label(window, image=photo)
# label5=Label(window, image=photo2)

# b1=Button(window, text='파이썬 종료', fg = 'red', bg='yellow',command=quit)
# b2=Button(window,image-photo,command=myF)

# ck=IntVar()
# cb1=Checkbutton(window,text='클릭하셈', variable=ck, command=myF)

# var=IntVar()
# rb1=Radiobutton(window,text='파이썬',variable=var,value=1,command=myF2)
# rb2=Radiobutton(window,text='C++',variable=var,value=2,command=myF2)
# rb3=Radiobutton(window,text='자바',variable=var,value=3,command=myF2)

# label6=Label(window,text='선택 언어 : ',fg='red')
# rb1.pack()
# rb2.pack()
# rb3.pack()
# label6.pack()

# b1.pack()
# label1.pack()
# label2.pack()
# label3.pack()
# label4.pack(side=RIGHT)
# label5.pack(side=LEFT)

# window.mainloop()

from tkinter import *
from tkinter import messagebox

btnList=[""]*15
fnameList=["froyo.gif","gingerbread.gif","honeycomb.gif","icecream.gif","jellybean.gif","kitkat.gif","lolipop.gif","mashmallow.gif","nougat.gif","icecream.gif","jellybean.gif","kitkat.gif","lolipop.gif","mashmallow.gif","nougat.gif"]

photoList=[None]*15
i,k=0,0
xPos,yPos=5,5
num=0

window=Tk()
window.geometry("240x400")

for i in range(0,15):
    photoList[i]=PhotoImage(file ="gif/"+fnameList[i])
    btnList[i]=Button(window,image=photoList[i])

for i in range(0,5):
    for k in range(0,3):
        btnList[num].place(x = xPos , y= yPos)
        num +=1
        xPos += 80
    xPos= 5
    yPos += 80

window.mainloop()