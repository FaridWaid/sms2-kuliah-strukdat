import stacks as st
def biner (a):
    b = st.stack()
    if a <= 0:
        print ("Angka yang anda masukkan tidak dapat dikonversi")
    else:
        while True:
            if a == 0:
                break
            elif a % 2 == 0:
                st.push(b, 0)
                a = a/2
            elif a % 2 == 1:
                st.push(b, 1)
                a = (a/2)- 0.5

        hasil = ''
        while not st.isempty(b):
            hasil = hasil + str(st.pop(b))

        return (hasil)

a = int(input('Masukkan Angka : '))
print ( "Hasil Konversi =", (biner(a)))



        
