class bank:
    bl=100
    global bal
    bal=12000
    def show_bal(self,pin):
        if(pin==123):
            print("My balance is_:",bal)
        else:
            print("Invalid user")
   
b=bank()
print(b.bl)
p=int(input("Enter pin to view bal"))    
b.show_bal(p)

