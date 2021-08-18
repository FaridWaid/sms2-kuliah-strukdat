data = [3, 5, 9, 12, 14, 15, 19]

for i in range (1,len(data)):
    key = data[i]
    print(key)
    j=i-1
    count=0
    while j>=0 and key<=data[j]:
        data[j+1]=data[j]
        j-=1
        print(j,"=",data)
    data[j+1]=key
    count+=1
    print(data)
print(count)
