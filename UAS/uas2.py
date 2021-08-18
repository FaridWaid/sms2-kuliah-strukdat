
def Un (a,b,n):
    un = 0
    kali = (n-1)* b
    akhir = a + kali
    print("U(n) = ", akhir)
    return akhir

def Sn (a,b,n):
    awal = 2 * a + (n-1) * b
    akhir = 0.5* n * awal
    print("S(n) = ", akhir)

Un(1,2,2)
Sn(1,2,2)
