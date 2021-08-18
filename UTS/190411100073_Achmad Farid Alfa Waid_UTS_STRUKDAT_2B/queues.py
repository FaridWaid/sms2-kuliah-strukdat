def Queue():
    q=[]
    return (q)
def enque(q,data):
    q.insert(0,data)
    return(q)
def deque(q):
    data=q.pop()
    return(data)
def isEmpty(q):
    return (q==[])
def Size(q):
    return (len(q))
