def shorting_d(a):
    for i in range (len(a)-1,0,-1):
        print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
        b = len(a)-1
        for j in range (i,0,-1):
            if a[b] > a[b-1]:
                a[b-1],a[b] = a[b],a[b-1]
            print (len(a)-j,"=",a)
            b = b - 1
  
                
shorting_d([100,34,1,7,2,4,6,77,4,54,67,34,23,68,90,21,45])

