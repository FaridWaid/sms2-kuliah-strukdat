angka = int(input("Masukkan angka : "))
if angka == 0:
    print("Angka: " + str(angka) + " Bukan Bilangan Prima")
else:
    if angka == 1:
        print("Angka: " + str(angka) + " Bukan Bilangan Prima")
    else:
        if angka == 2:
            print("Angka: " + str(angka) + " adalah Bilangan Prima")
        else:
            cek = 2
            while cek <= angka:
                if cek == angka:
                    print("Angka: " + str(angka) + " Adalah Bilangan Prima")
                else:
                    if angka % cek == 0:
                        print("Angka: " + str(angka) + " Bukan Bilangan Prima, karena angka: " + str(angka) + " bisa dibagi dengan angka: " + str(cek) + ", Hasilnya: " + str(float(angka) / cek))
                        cek = angka
                cek = cek + 1



