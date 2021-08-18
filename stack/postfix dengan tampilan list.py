import stacks as st
x="{[23+56] *[12- 2]:[10 +20]}"
stack = st.stack()
kurung=[]
hasil=[]
a=''
for cek in x:
    if cek == '0' or cek=='1' or cek=='2' or cek=='3' or cek=='4' or cek=='5' or cek=='6' or cek=='7' or cek=='8' or cek=='9':
        hasil.append(cek)
    else:
        if cek == "(" or cek == "{" or cek == "[":
            kurung.append(cek)
        elif cek=="+" or cek=="-" or cek==":" or cek=="*":
            st.push(stack,cek)
        elif cek==")" or cek=="]" or cek=="}":
            a=a+str(st.pop(stack))
            hasil.append(a)
            a=''
else:
    a=a+str(st.pop(stack))
    hasil.append(a) 
print(hasil)
