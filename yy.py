class Mat():
    def __init__(self):
        
    def Un (a,b,n):
        un = 0
        kali = (n-1)* b
        akhir = a + kali
        print("U(n) = ", akhir)
        return akhir

    def Sn (Un(a,b,n)):
        s = n
        kali = s * (n - 1)
        akhir2 = kali + Un(a,b,n)
        print("S(n) = ", akhir2)

Un(1,2,2)
Sn(1,2,2)
