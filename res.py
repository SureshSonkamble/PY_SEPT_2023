s1=int(input("Enter number one"))
s2=int(input("Enter number two"))
s3=int(input("Enter number three"))
if(s1>=0 and s1<=100  and s2>=0 and s2<=100 and s3>=0 and s3<=100):
    ttl=s1+s2+s3
    p=ttl/3
    print("ttl=",ttl)
    print("per",p)  
else:
    print("Invalid Marks")
if(p>=75):
    print("A+")
elif(p<75 and p>=60):
    print("A")
elif(p<60 and p>=50):
    print("B")
elif(p<50 and p>=40):
    print("C")
else:
    print("FAIL")

    



    


    
  
    
