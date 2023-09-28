#read file
f = open("dumy.txt", "r") #root location
fl=f.read()
x = fl.split(" ")
print(x)
cnt=0
for i in x:
    if(i=='and'):
        cnt=cnt+1
print(cnt)
