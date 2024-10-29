#file create and write
f = open('gayatri.txt', 'w')#open file
data=input("Enter marks")
print (f.write(data))#read file
f.close()
print("Success")

------------------------------------
f = open("demofile.txt", "r")
print(f.read())

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

f = open("demofile.txt", "r")
print(f.read(5))
f = open("demofile.txt", "r")
print(f.readline()) #Read one line of the file:
------------------------------------
Read two lines of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
#read file
f = open("marks.txt", "r") #root location
#f = open("D:\\test.txt", "r")
#f = open("D:\\Files\\testfile.txt", "r")  
fl=f.read()
x = fl.split(",")
print(x)
for i in x:
    print(i)