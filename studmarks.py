mrk=open('stud_marks.txt','w')
n=int(input("Enter Number of student"))
for i in range(n):
    data=input("Enter marks")
    print (mrk.write(data))#read file
    
mrk.close()
print("Success")
