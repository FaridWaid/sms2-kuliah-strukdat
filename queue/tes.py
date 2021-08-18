def createQueue():
    q=[]
    return (q)
def enqueue(q,data):
    q.insert(0,data)
    return(q)
def dequeue(q):
    data=q.pop()
    return(data)
def isEmpty(q):
    return (q==[])
def size(q):
    return (len(q))



def jumlahcpu(baris,kolom):
    m=[]
    for i in range (baris):
        matriks=[]
        for i in range ((kolom)):
            b=(str(input("Nama Proses: ")))
            a=(int(input("Waktu Proses : ")))
            matriks.append(b)
            matriks.append(a)
        m.append(matriks)
    return list(reversed(m))
cpu=int(input("Jumlah Proses yang akan dijadwal di CPU :"))
print("Antrian Proses : ",jumlahcpu(cpu,1))
m=[m+jumlahcpu(cpu,1)]
queue=createQueue()
c=int(input("Waktu Proses CPU = "))
print("Antrian Proses beserta Waktunya = ",m)
for i in range (len(baris,kolom)):
    print("Iterasi ke- ",i)
    if m[size(m)-1][1] - c > 0:
        d= d+ (m[size(m)-1][0]-c)
        print("Proses",m[size(m)-1][0],"sedang diproses, dan sisa waktu proses",m[size(m)-1][0],"=",d)
        print(enqueue(queue,dequeue(m)))
    else:
        print("Proses C telah selesai diproses")
        dequeue(m)
        print(m)

