def shorting(a,b):
    a=stack1+stack2
    for i in range (len(a)-1,0,-1):
        print ("Proses ke ",len(a)-i,"Jumlah Iterasi =",i)
        for j in range (i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
            print (a)
        tes = True
        for j in range (i):
            if a[j]<=a[j+1]:
                tes = tes + True
            else:
                tes = tes + False
        if tes == True:
            print ("Data terurut =",a)
            
                
stack1=[100, 92, 90, 49, 45, 30, 11, 10, 8, 4, 2]
stack2=[87, 56, 51, 40, 38, 32, 30, 25, 18, 12, 7, 5, 1]
shorting(stack1,stack2)

