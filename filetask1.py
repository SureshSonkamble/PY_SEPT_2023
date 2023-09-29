import matplotlib.pyplot as plt
import numpy as np
#read file
f = open("stud_marks.txt", "r") #root location
fl=f.read()
x = fl.split(" ")
print(x)
cnt=0
l=[]
for i in x:
    l.append(int(i))
    print(int(i))
 
y = np.array(l)
plt.pie(y)
plt.show() 
