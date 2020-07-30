from tkinter import *
from tkinter.filedialog import asksaveasfile
from git_clone import *
#All def

def gitclone():
    git_clone(E.get())

window = Tk()
window.title('Git Cloner')
window.geometry("350x350")
lb1 = Label(window,text="Url:")
lb1.place(x=50,y=20)
E = Entry(window)
E.place(x=80,y=20)
bt1 = Button(window,text="Clone NOW!",command=gitclone)
bt1.place(x=100,y=45)
window.mainloop()