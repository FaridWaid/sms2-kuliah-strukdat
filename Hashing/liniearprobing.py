def remainderFunction (data,num):
    return (data%num)

def createHashTable(num):
    temp=[]
    for i in range(num):
        temp.append('none')
    return(temp)
def putData(data,table):
    for i in range(len(data)):
        ind=remainderFunction(data[i],len(table))  
        table[ind]=data[i]
    return(table)

def searchHash(data,table):
    hashVal=remainderFunction(data,len(table))
    if data==table[hashVal]:
        return True
    else:
        return False
    
def linearProbing(ind,hashTable,data):
    count=ind
    found=False
    
    while (count!=ind-1) and not(found):
        
        if hashTable[count]=='none':
            found=True
            hashTable[count]=data
            
        else:
            count=count+1
            if count==len(hashTable)-1:
                count=0
    return(hashTable)

def putData3(a,hashTable,functionName):
    
    for i in range(len(a)):
       
        if functionName=='reminder':
            ind=remainderFunction(a[i],len(hashTable))   
            
        elif functionName=='midSq':
            ind=midSqFunction(a[i],len(hashTable))  
        
       
        if hashTable[ind]=='none':
            hashTable[ind]=a[i]
        else:
            hashTable=linearProbing(ind,hashTable,a[i])    
        
    return(hashTable)


a=[54, 26, 93, 17, 77, 31]
hashTable=createHashTable(11)
print(hashTable)
hashTable=putData3(a,hashTable,'midSq')
print(hashTable)
