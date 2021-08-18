def towers(n,awal,bantuan,tujuan):
    if n==1:
        print("Piringan - 1 dari-", awal,"ke-",tujuan)
    else:
        towers(n-1,awal,tujuan,bantuan)
        print("Piringan -",n, "dari-",awal,"ke-", tujuan)
        towers(n-1,bantuan,awal,tujuan)

towers(4,"A","B","C")
