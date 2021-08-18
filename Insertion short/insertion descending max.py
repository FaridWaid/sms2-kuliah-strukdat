data = [10,5,7,4,11,65,2]

for i in range (-2,-len(data)-1,-1):
    a=0
    key = data[i]
    print("key =",key)
    j=i+1
    while j<=-1 and key<=data[j]:
        key>=data[j]
        data[j-1]=data[j]
        j+=1
        print(a,"=",data)
        a+=1
    data[j-1]=key
    print(data)
