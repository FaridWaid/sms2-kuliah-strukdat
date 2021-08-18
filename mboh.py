import stacks as st
def postfix (x):
    stack = st.stack()
    kurung=[]
    hasil=''
    a=''
    for cek in x:
        if cek == '0' or cek=='1' or cek=='2' or cek=='3' or cek=='4' or cek=='5' or cek=='6' or cek=='7' or cek=='8' or cek=='9':
            hasil+=str(cek)
        else:
            if cek == "(" or cek == "{" or cek == "[":
                kurung.append(cek)
            elif cek=="+" or cek=="-" or cek=="*" or cek==":":
                st.push(stack,cek)
                hasil+=" "
            elif cek==")" or cek=="]" or cek=="}":
                for i in range (st.size(stack)):
                    hasil+=" "
                    a=a+str(st.pop(stack))
                    hasil+=str(a)
                    a=''
    if not st.isempty(stack):
        hasil+=" "
        a=a+str(st.pop(stack))
        hasil+=str(a)
    if st.isempty(stack):
        return hasil
    else:
        return "Tidak Dapat Dioperasikan"
x=[(5+6)*(20-14)]
print(postfix(x))
