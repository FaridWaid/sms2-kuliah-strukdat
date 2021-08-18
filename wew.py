def anyFn(a):
    if a == 0:
        return 1
    else:
        return 2*anyFn(a-1)

print(anyFn(5))
