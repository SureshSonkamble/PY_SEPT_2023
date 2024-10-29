import matplotlib.pyplot as plt
n=int(input("Enter Amount of data to add to in list"))
l=[]
for i in range(n):
    d=int(input("Enter  data to add to in list"))
    l.append(d)
print(l)
x=[]
y=[]
for i in l:
    if(i<25):
        x.append(i)
    if(i>25):
        y.append(i)
print(x)
print(y)
#plt.scatter(x, y)
#plt.show()


