'''s=[88,55,75,66]
for i in s:
    print(i)'''
s=[]
n =int(input("Enter numbers of student "))
for i in range(n):
    m=int(input("Enter  student  per %"))
    s.append(m)
print(s)
dis=[]
fst=[]
for i in s:
    if(i>75):
        dis.append(i)
    if(i<75 and i>=60):
        fst.append(i)
    
print(dis)
print(fst)
