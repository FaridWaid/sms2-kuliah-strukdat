import stacks as st
import deques as deq
def palindrome(kata):
    stack=st.stack
    pali=deq.deque()
    hasil=[]
    for i in kata:
        deq.addfront(pali,i)
    cek = True
    while deq.Size(pali)>1:
        if deq.removefront(pali)==deq.removerear(pali):
            cek = cek and True
        else:
            cek = cek and False
    print (cek)


        
    

a1='<html> <head> <title> Example </title> </head> <body> <h1> Hello, world </h1> </body> </html>'
a1=a1.split()
a2='<html> <head> <title> Example </title> </head> <body> <h1> Hello, world </h1> </body>'
a2=a2.split()
a3='<html> <head> <title> Example </title> </head> <body> <h1> Hello, world </h1> </body> </head>'
a3=a3.split()
a4='<html> <head> <title> Example </title> </head> <body> <h1> Hello, world </h1> </h1> </head>'
a4=a4.split()
a5='<html> <head> <title> <title> Example </title> </head> <body> <h1> Hello, world </h1> </body> </html>'
a5=a5.split()
(palindrome(a1))
(palindrome(a2))
(palindrome(a3))
(palindrome(a4))
(palindrome(a5))
