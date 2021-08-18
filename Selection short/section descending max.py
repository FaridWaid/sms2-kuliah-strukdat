data=[10,6,7,1,8,9,99,100,4,2,21,34,2,9,12]
for outerloop in range (len(data)-1):
    minflag=outerloop
    for j in range (outerloop+1,len(data)):
        if data[minflag]<data[j]:
            minflag=j
    data[outerloop],data[minflag]=data[minflag],data[outerloop]
    print(data)
