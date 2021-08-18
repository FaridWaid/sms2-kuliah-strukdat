import stacks as st
def heksa (des):
    data=st.stack()
    while des >=0:
        a = des%8
        if des == 0:
            break
        else:
            st.push(data,a)
        des = des//8
    balik = ''
    while not st.isempty(data):
        balik = balik + str(st.pop(data))
    return (balik)
des=int(input('masukkan angka desimal: '))
print(heksa(des))
