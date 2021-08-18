import queues as que
def permainan (nama,hitungan):
    game=que.Queue()
    for data in nama:
        que.enque(game,data)
    print ("Urutan Awal = ",game)
    while not(que.isEmpty(game)):
        for i in range (hitungan):
            que.enque(game,que.deque(game))
            print("Proses Antrian",i,game)
        que.deque(game)
        print("Urutan Sekarang = ", game)

nama = ("Achmad","Farid","Alfa","Waid")
permainan(nama,2)
