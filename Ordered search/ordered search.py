def orderedSearch(listData,key):
    for a in range (1,len(listData)):
        x = listData[a]
        b=a-1
        while b>=0 and x<=listData[b]:
            listData[b+1]=listData[b]
            b-=1
        listData[b+1]=x
    found=False
    i=0
    stop=False
    count = 0
    while not (stop) and not(found):
        if i == len(listData) or listData[i]>key:
            stop=True
        elif listData[i]==key:
            ind=i
            found=True
        i+=1
        count+=1
    if found:
        print (count)
        return ind
    
    else:
        return False

a=[9, 12, 5, 3, 15, 19, 14]
print(orderedSearch(a,12))
