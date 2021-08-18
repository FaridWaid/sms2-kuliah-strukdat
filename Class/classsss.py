#class Robot:
#    def settingAttribute(self,w,t):
#        temp=100
#        self.warna=w
#        self.tinggi=t
#    def introducing(self):
#        print("warna=",self.warna,"tinggi=",self.tinggi)
#
#r1=Robot()
#r2=Robot()

              
#constructions
class Robot:
    def __init__(self,w,t):
        temp=100
        self.warna=w
        self.tinggi=t
    def introducing(self):
        print("warna=",self.warna,"tinggi=",self.tinggi)

r1=Robot("red",170)
r1.introducing()
