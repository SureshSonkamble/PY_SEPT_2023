from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("300x300")
s = Button(top, text ="center")
s.place(x=135,y=135)
   
B = Button(top, text ="One")
B.place(x=50,y=50)

B = Button(top, text ="Two")
B.place(x=50,y=220)

B1 = Button(top, text ="Three")
B1.place(x=220,y=50)

B1 = Button(top, text ="Four")
B1.place(x=220,y=220)
top.mainloop()
