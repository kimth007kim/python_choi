from tkinter import *

def change_img():
    path= inputBox.get()
    img=PhotoImage(file=path)
    imageLabel.configure(image=img)


window=Tk()
photo= PhotoImage(file="jg.jpg")
imageLabel= Label(window,image=photo)
imageLabel.pack()

inputBox = Entry(window)
inputBox.pack()

button=Button(window,text='Submit',command=change_img)
button.pack()

window.mainloop()