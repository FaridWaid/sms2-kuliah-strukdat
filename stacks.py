def stack():
    l = []
    return (l)

def push(l, value):
    l.append(value)

def pop(l):
    value = l.pop()
    return (value)

def peek(l):
    return l[len(l)-1]

def isempty(l):
    return l == []

def size(l):
    return len(l)