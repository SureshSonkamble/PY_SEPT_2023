class prnt1:
    def p1(self):
        print("This is parent one")
class prnt2:
    def p2(self):
        print("This is parent two")
class prnt3:
    def p3(self):
        print("This is parent three")        
class clrnd(prnt1,prnt2,prnt3):
     def c(self):
         pass

c=clrnd()
c.p2()
c.p1()
c.p3()
