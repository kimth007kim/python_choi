from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    messagebox.showinfo("키보드 이벤트","눌린 키: "+ chr(event.keycode))


window = Tk()

#window.geometry("400x400")

label1=Label(window,text="이곳이 바뀜")

window.bind("<Key>",keyEvent)

window.mainloop()
