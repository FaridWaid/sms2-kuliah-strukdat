def anyFn(a,b):
    if b == 0:
        return 1
    else:
        return a*anyFn(a,b-1)

print(anyFn(2,4))
