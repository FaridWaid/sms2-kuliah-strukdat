import stacks as st
def evaluatePost(x):
    tambah = ["+", "-"]
    kali = ["*", ":"]
    simpan1 = ""
    simpan = st.stack()
    for cek in x:
        if cek == '0' or cek=='1' or cek=='2' or cek=='3' or cek=='4' or cek=='5' or cek=='6' or cek=='7' or cek=='8' or cek=='9':
            simpan1 += cek
        c = st.size(simpan)
        if cek == "+":
            a = float(simpan[c-2] + simpan[c-1])
            st.pop(simpan)
            st.pop(simpan)
            st.push(simpan, a)

        elif cek == "-":
            a = float(simpan[c-2] - simpan[c-1])
            st.pop(simpan)
            st.pop(simpan)
            st.push(simpan, a)

        elif cek == "*":
            a = float(simpan[c-2] * simpan[c-1])
            st.pop(simpan)
            st.pop(simpan)
            st.push(simpan, a)

        elif cek == ":":
            a = float(simpan[c-2] / simpan[c-1])
            st.pop(simpan)
            st.pop(simpan)
            st.push(simpan, a)

        elif cek == " ":
            if st.size(simpan1) != 0:
                b = int(simpan1)
                st.push(simpan, b)
                simpan1 = ""

    return float(simpan[0])
x=(" 5 6 + 20 14 - *")
print (evaluatePost(x))
