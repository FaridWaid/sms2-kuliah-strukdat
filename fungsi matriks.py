def jumlahmatrik (m1,m2):
    if len (m1) == len (m2):
        hasil=[]
        for i in range(len(m1)):
            hasil.append(m1[i]+m2[i])
        return hasil
    else:
        return ("ukuran tidak sama")


m1 = [[1,2],[3,4]]
m2 = [[4,5],[6,7]]

print (jumlahmatrik(m1,m2))


#fungsi penjumlahan matriks 2 dimensi
#fungsi perkalian matriks 2 dimensi
#fungsi bikin matriks 2 dimensi
