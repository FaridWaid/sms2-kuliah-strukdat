def anyFn(a,b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a+anyFn(a,b-1)

print(anyFn(2,8))
