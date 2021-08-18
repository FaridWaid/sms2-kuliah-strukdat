class Kompleks:
    def __init__(self,a=0,b=0):
        self.real=a
        self.imajiner=b
    def bilangan(self):
        print("hasilnya=",self.real, "+", self.imajiner,"i")
    def addkompleks(self,bil):
        tempR=self.real+bil.real
        tempI=self.imajiner+bil.imajiner
        return Kompleks(tempR,tempI)

r1=Kompleks(12,5)
r2=Kompleks(10,7)
r3=r1.addkompleks(r2)
r1.bilangan()
r2.bilangan()
r3.bilangan()

#tugas : perkalian
