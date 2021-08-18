import queue as que
queue = que.Queue()
d=0
cpu=int(input("Jumlah Proses yang akan dijadwal di CPU :"))
m=[]
a=[]
for i in range (cpu):
    matriks=[]
    for i in range (1):
        b=(str(input("Nama Proses: ")))
        a=(int(input("Waktu Proses : ")))
        matriks.append(b)
        matriks.append(a)
        m.append(matriks)
a=list(reversed(m))
queue=a
print("Antrian Proses : ",queue)
c=int(input("Waktu Proses CPU = "))
print("Antrian Proses beserta Waktunya = ",a)
for i in range (que.size(a)):
    print("Iterasi ke- ",i)
    if a[que.size(a)-1][1] - c > 0:
        d+= (a[que.size(a)-1][1] - c)
        print("Proses",a[que.size(a)-1][0],"sedang diproses, dan sisa waktu proses",a[que.size(a)-1][0],"=",d)
        print("Data proses yang tersisa :",que.enque(que.denque(a)),a)
    else:
        print("Proses",a[que.size(a)-1][0],"telah selesai diproses")
        print("Data proses yang tersisa :",que.denque(a),a)
