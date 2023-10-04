class bank:
     
    def show_bal(p):
        if(p==123):
            print("My Balance: 12000")
        else:
            print("Invalid user")
    def binfo():
        print("This is Axis Bank")
        
pin=int(input("Enter pin nunmber to view bal"))
bank.show_bal(pin)
