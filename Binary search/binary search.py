def binsearch(listData,key):
    for a in range (1,len(listData)):
        x = listData[a]
        b=a-1
        while b>=0 and x<=listData[b]:
            listData[b+1]=listData[b]
            b-=1
        listData[b+1]=x
        print(listData)
    found=False
    first=0
    last=len(listData)-1
    more=[]
    while first<=last and not (found):
        mid = (first+last)//2
        if listData[mid]==key:
            more.append(mid)
            found = True
        if key>listData[mid]:
            first=mid+1
        elif key<listData[mid]:
            last=mid-1
    if found:
        return more
    else:
        return False

a=[9, 12, 5, 3, 15, 19, 14]
print(binsearch(a,12))
