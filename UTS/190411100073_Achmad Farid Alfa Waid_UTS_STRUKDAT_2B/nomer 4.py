import stacks as st
a=[0,1,0,0,0,1,0]
nol=0
satu=0
for i in (a):
    if i == 0:
        nol+=1
    else:
        satu+=1
y1=nol *nol
y2=satu*satu
y3=(st.size(a))*(st.size(a))
penjumlahan = y1+y2
total=y3-penjumlahan
if y3 == 0:
    print(0)
else:
    print(str(total),"/",str(y3))

