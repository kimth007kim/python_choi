from tkinter import *
from tkinter.filedialog import *


window = Tk()
window.geometry("400x100")

label1=Label(window,text="선택된 파일 이름")
label1.pack()

saveFp=asksaveasfile(parent=window,mode="w",defaultextension=".jpg",filetypes=(("JPG 파일","*.jpg;*.jpeg"),("모든 파일","*.*")))

label1.configure(text=str(saveFp))
window.mainloop()
