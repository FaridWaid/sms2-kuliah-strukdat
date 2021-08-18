#1 dimensi
#a = [0,1,2]
#b = [3,4,5]

#print (a[0]+b[0],b[1]+a[1],a[2]+b[2])


#2 dimensi
c = ([9,8,7],[6,5,4])
d = ([1,2,3],[4,5,6])
def tambah (c,d):
    mtotal =[]
    for baris in range (len(c)):
        mbaris = []
        for kolom in range (len(c[0])):
           hitung = c [baris][kolom] + d [baris][kolom]
           mbaris.append(hitung)
        mtotal.append(mbaris)
    return mtotal
print (tambah(c,d))



