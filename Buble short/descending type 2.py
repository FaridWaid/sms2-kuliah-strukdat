def shorting_d2(a):
    for i in range (len(a)-1,0,-1):
        print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
        for j in range (i):
            if a[j] < a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
            print ("=",a)
        b = len(a)-1
        tes = True
        for j in range (i):
            if a[j+1] <= a[j]:
                tes = tes and True
            else:
                tes = tes and False
        if tes:
            return(a)



            
                
shorting_d2([100,34,1,7,2,4,6,77,4,54,67,34,23,68,90,21,45])

