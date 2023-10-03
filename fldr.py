import os
try:
        for i in range(1,11):
             path='D:\VSPI\www'+str(i)
             os.makedirs(path)
             print("Folder created Successfully..")
             f = open(path+'/'+'stud.txt', 'w')#open file
             p = open('suresh.txt', 'r')#open file
             data=p.read()
             f.write(data+str(i))
             f.close()
except Exception as e:
      print("File allready exit")
