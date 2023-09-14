print("1.ADD")
print("2.SUB")
print("3.MUL")
print("4.DIV")
n1=int(input("Enter number one :"))
n2=int(input("Enter number  two :"))
ch=int(input("Entre your choice"))
if(ch>0 and ch<5):
    if(ch==1): 
        print("Add=",n1+n2)
    elif(ch==2):
        print("SUB=",n1-n2)
    elif(ch==3):
        print("MUL=",n1*n2)
    elif(ch==4):
        print("DIV=",n1/n2)
else:
    print("Invalid Choice...")





        
