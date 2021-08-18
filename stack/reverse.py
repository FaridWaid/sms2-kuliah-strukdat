import stacks as st
def reverseword(a):
    simpan = st.stack()
    b = ''
    for cek in range(len(a)):
        st.push(simpan,a[cek])

    hasil = ''
    while not st.isempty(simpan):
        reverse = st.pop(simpan)
        hasil = hasil + reverse
    return hasil


a = "Achmad Farid Alfa Waid"
print(reverseword(a))
        
