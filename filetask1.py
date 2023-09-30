import matplotlib.pyplot as plt
import numpy as np
#read file
f = open("stud_marks.txt", "r") #root location
fl=f.read()
x = fl.split(" ")
print(x)
l=[]
d=0
f=0
s=0
fl=0
gd=["O","A","B","D"]
for i in x:
    print(int(i))
    #l.append(int(i))
    if(int(i)>=75):
        d=d+1
    if(int(i)<75 and int(i)>=60):
        f=f+1
    if(int(i)<60 and int(i)>=50):
        s=s+1
    if(int(i)<40):
        fl=fl+1    
    
l=[d,f,s,fl] 
y = np.array(l)
plt.figure(figsize=(8,10))
plt.pie(y,labels=gd,explode=[0.2,0,0,0],shadow=True,colors=['pink','red','blue','green'],autopct="%2.1f%%")
plt.legend(title="Student Performance")
plt.show() 
