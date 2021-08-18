import stacks as st
def cek (x):
    stack = st.stack()
    tes = 0
    for cek in x:
        if cek == "(" or cek == "{" or cek == "[":
          st.push(stack, cek)
        elif cek == ")" or cek == "}" or cek == "]":
            if st.isempty(stack):
              return("kelebihan kurung tutup")
              tes = 1
              break
            elif st.peek(stack) == "(" and cek == ")":
                st.pop(stack)
            elif st.peek(stack) == "{" and cek == "}":
                st.pop(stack)
            elif st.peek(stack) == "[" and cek == "]":
                st.pop(stack)
            else:
                return("kesalahan kurung tutup")
                tes = 1
                break
    if st.isempty(stack) and tes ==0:
        return("DONE")
    elif not st.isempty(stack) and tes == 0:
        return("Kelebihan kurung buka")
x=input("masukkan") 
print(cek(x))
