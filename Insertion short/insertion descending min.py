data = [10,5,7,4,11,65,2]

for i in range (1,len(data)):
    a=0
    key = data[i]
    print("key=",key)
    j=i-1
    while j>=0 and key>=data[j]:
        data[j+1]=data[j]
        j-=1
        print(a,"=",data)
        a+=1
    data[j+1]=key
    print(data)
