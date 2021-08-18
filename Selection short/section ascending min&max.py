def sectionascdsc (data):
    for outerloop in range (len(data)-1):
        minflag=outerloop
        for j in range (outerloop+1,len(data)):
            if data[minflag]>data[j]:
                minflag=j
        data[outerloop],data[minflag]=data[minflag],data[outerloop]
        print("minimal =",data)
        a = ((len(data)-1)-outerloop)
        for j in range (0,a+1):
            if data[minflag]<data[j]:
                minflag=j
        data[minflag],data[a]=data[a],data[minflag]
        print("maksimal =",data)
        tes = True
        for k in range (j):
            if data[k] <= data[k+1]:
                tes = tes and True
            else:
                tes = tes and False
        if tes:
            #print("yes")
            break

data=[10,6,7,1,8,9,99,100,4,2,21,34,2,9,12]
sectionascdsc(data)
