class bank:
    #bl=100
    cnt=0
    ex=0
    global bal
    bal=12000
    def show_bal(self,pin):
        if(pin==123):
            b.ex=b.ex+1
            print("My balance is_:",bal)
        else:
            b.cnt=b.cnt+1
            print("Invalid user")
   
b=bank()
#print(b.cnt)
n=0
while(n<3):
    p=int(input("Enter pin to view bal"))    
    b.show_bal(p)
    if(b.ex==1):
        exit()
    n=b.cnt
    print(n)

