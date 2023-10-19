from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("500x400")

def msgi():
    messagebox.showinfo("showinfo", "Information")
def msgw():
    messagebox.showwarning("showwarning", "Warning") 
def msge():
    messagebox.showerror("showerror", "Error") 
def msgq():
    messagebox.askquestion("askquestion", "Are you sure?") 

def msgc():
    messagebox.askokcancel("askokcancel", "Want to continue?") 

s = Button(top, text ="Info",command=msgi)
s.place(x=200,y=75)
s2 = Button(top, text ="Warning",command=msgw)
s2.place(x=200,y=125)
s3 = Button(top, text ="Error",command=msge)
s3.place(x=200,y=175)
s3 = Button(top, text ="Question",command=msgq)
s3.place(x=200,y=225)
s3 = Button(top, text ="cancle",command=msgc)
s3.place(x=200,y=275)

   
top.mainloop()
