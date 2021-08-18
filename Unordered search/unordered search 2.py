def unOrderedSearch2(listData,key):
    i=0
    more=[]
    count=0
    while i<len(listData):
        if listData[i]==key:
            more.append(i)
            found=True
        i+=1
    if found:
        return more
    else:
        return False

a=[9, 12, 5, 3, 15, 19, 14]
print(unOrderedSearch2(a,12))
