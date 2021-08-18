def unOrderedSearch(listData,key):
    found=False
    i=0
    while i<len(listData) and not(found):
        if listData[i]==key:
            ind=i
            found=True
        i+=1
    if found:
        return ind
    else:
        return False

a=[54,25,73,12,15,2,30]
print(unOrderedSearch(a,25))
