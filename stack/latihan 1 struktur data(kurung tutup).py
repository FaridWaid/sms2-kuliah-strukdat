import stacks as st
def cek_math(rumus):
    data=st.stack()
    for ch in rumus:
        if ch=="(":
            st.push(data,ch)
        elif ch== ")" and (st.size(data)>0):
            st.pop(data)
        elif ch==")":
            st.push(data,ch)

    if st.size(data)>0:
        if st.peek(data)==")":
            print("Kelebihan )")
        else:
            print("Kelebihan (")
    else:
        print("Rumus OK")

cek_math("5*3+(4")
