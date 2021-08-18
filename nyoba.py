print ("matriks")
def matriks (x,z):
    x=[]
    z=[]
    while True :
        a = int(input("Masukkan angka kedalam matriks 1: "))
        x.append(a)
        b = str(input("masukkan Y jika ingin menambah angka ke matriks 1: "))
        if not (b == "Y"):
            break
    while True:
        c = int(input("Masukkan angka kedalam matriks 2: "))
        z.append(c)
        d = str(input("masukkan Y jika ingin menambah angka ke matriks 2: "))
        if not (d == "Y"):
            break
    return (x,z)
print(x)
print(z)
