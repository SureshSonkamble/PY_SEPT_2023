class prnt:
    def p():
        print("This is parent class fun")
    def prty():
        print("$654697")

class cld(prnt):
    def c():
        print("this is chid class fun")

#prnt.p()
cld.c()
cld.p()
cld.prty()
