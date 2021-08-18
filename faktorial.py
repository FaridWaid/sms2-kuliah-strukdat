#def faktorial(n):
    #if n < 2:
        #return 1
    #else:
        #return n * faktorial(n-1)
#n = int(input("Masukkan angka"))
#print (faktorial(n))


#pengurutan faktorial dari terkecil sampai terbesar
#a=int(input("Masukkan Angka"))
#hasil = 1
#for i in range (1, a+1):
    #hasil *= i
#print ("nilainya adalah", hasil)


a = int(input("Masukkan bilangan: "))
faktorial=1
for i in range (a+1,1,-1):
    faktorial *= i
print("nilainya adalah:", faktorial)
