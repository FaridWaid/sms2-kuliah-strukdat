def multiplyMat(a, b):
    hasil = []
    for i in range(len(a)):
        simpan = []
        for j in range(len(a[0])):
            s = 0
            for k in range(len(a)):
                s = s + (a[i][k] * b[k][j])
            simpan.append(s)
        hasil.append(simpan)
    return hasil


x = [[1, 2], [3, 4]]
y = [[4, 3], [2, 1]]

print(multiplyMat(x, y))
