class gcntr:
    sname='sonkamble'
    def __gctr__(self,sname):
        self.sname=sname
class pcntr(gcntr):
    pname="Daulat"
    def __pcntr__(self,pname,sname):
        self.pname=pname
class cntr(pcntr):
    name="Suresh"
    def __cntr__(self,name,pname,sname):
        self.name=name

#g=gcntr()
#print("My surname is :",g.sname)
#p=pcntr()
#print("My parent is :",p.pname,p.sname)
c=cntr()
print("My Full name is :",c.name,c.pname,c.sname)

