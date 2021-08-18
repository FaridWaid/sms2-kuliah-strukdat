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
        
    

ulang= "y"
while ulang == "y":
    kata=(str(input("Masukkan Kata yang di cek: ")))
    palindrome(kata)
    ulang=(str(input("Apakah anda ingin mencoba lagi?(y/n): ")))

