def konversiDesimal(bilangan,base):
    charBilangan='0123456789ABCDEF'
    if bilangan<base:
        return(charBilangan[bilangan])
    else:
        temp=bilangan//base
        ind=bilangan % base
        print(type(temp),temp,type(ind),ind)
        return(konversiDesimal(temp,base)+charBilangan[ind])

konversiDesimal(5,2)
