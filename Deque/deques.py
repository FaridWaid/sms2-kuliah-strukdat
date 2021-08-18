def deque():
    q=[]
    return (q)
def addfront(q,data):
    q.insert(0,data)
    return(q)
def addrear(q,data):
    q.append(data)
    return(q)
def removerear(q):
    data=q.pop()
    return(data)
def removefront(q):
    data=q.pop(0)
    return(data)
def isEmpty(q):
    return (q==[])
def Size(q):
    return (len(q))
