m1=[]
m2=[]
def matriks1(baris,kolom):
    for i in range (baris):
        matriks=[]
        for j in range (kolom):
            a=(int(input("Masukkan Angka kedalam  matriks 1: ")))
            matriks.append(a)
        m1.append(matriks)
    return m1

def matriks2 (baris,kolom):
    for i in range (baris):
        matriks=[]
        for j in range (kolom):
            b=int(input("Masukkan ANgka kedalam matriks 2: "))
            matriks.append(b)
        m2.append(matriks)
    return m2

print("Matriks 1=",matriks1(2,2))
print("Matriks 2=",matriks2(2,2))
