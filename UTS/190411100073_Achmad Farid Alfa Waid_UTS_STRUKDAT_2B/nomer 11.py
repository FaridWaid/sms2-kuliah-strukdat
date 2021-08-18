import deques as deq
def palindrome(kata):
    pali=deq.deque()
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
print(palindrome(a1))


