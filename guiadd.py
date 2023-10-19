from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()

top.geometry("200x200")
def show():
   n1 = askinteger("Input", "Input an Integer 1")
   n2 = askinteger("Input", "Input an Integer 2")
   print(n1+n2)
   ans=n1+n2;
   messagebox.showinfo("showinfo", "Sum"+str(ans))

def sqr():
   n1 = askinteger("Input", "Input an Integer 1")
   print("Sqauer of number is",n1*n1)


s = Button(top, text ="Click Me", command = show)
s.place(x=80,y=80)

s1 = Button(top, text ="Find Square", command = sqr)
s1.place(x=80,y=30)
   
top.mainloop()
