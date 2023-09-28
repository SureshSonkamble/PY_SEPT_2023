#read file
f = open("marks.txt", "r") #root location
#f = open("D:\\test.txt", "r")
#f = open("D:\\Files\\testfile.txt", "r")  
fl=f.read()
x = fl.split(",")
print(x)
for i in x:
    print(i)
