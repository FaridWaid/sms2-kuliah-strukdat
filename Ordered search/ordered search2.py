def orderedSearch2(listData,key):
    for a in range (1,len(listData)):
        x = listData[a]
        b=a-1
        while b>=0 and x<=listData[b]:
            listData[b+1]=listData[b]
            b-=1
        listData[b+1]=x
        print(listData)
    found=False
    i=0
    stop=False
    more=[]
    while not (stop):
        if listData[i]>key:
            stop=True
        elif listData[i]==key:
            ind=i
            more.append(i)
            found=True
        i+=1
    if found:
        return more
    else:
        return False

a=[54,25,73,12,15,2,30,25,12,45,25,100,34,5,6,7,25]
print(orderedSearch2(a,25))
