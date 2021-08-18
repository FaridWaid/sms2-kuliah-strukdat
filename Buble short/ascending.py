def shorting_a(a):
    for i in range (len(a)-1,0,-1):
        print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
        for j in range (i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
            print (a)
        tes = True
        for j in range (i):
            if a[j]<=a[j+1]:
                tes = tes and True
            else:
                tes = tes and False
        if tes == True:
            print ("Data terurut =",a)
            
                
shorting_a([100,34,1,7,2,4,6,77,4,54])

