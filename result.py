m=open('File\\school.txt','w')
s='abcdefghijk'
for i in  s:
    print(i)
    open('File\\school'+i+'.txt','w')
