class AntreanTiketKonser:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.queue = [None] * kapasitas
        self.size = 0
        self.depan = 0
        self.belakang = -1

    def is_full(self):
        return self.size == self.kapasitas

    def is_empty(self):
        return self.size == 0

    def enqueue(self, nama_pembeli):
        if self.is_full():
            print("\n[!] Antrean Penuh! {} tidak bisa masuk.".format(nama_pembeli))
        else:
            self.belakang = (self.belakang + 1) % self.kapasitas
            self.queue[self.belakang] = nama_pembeli
            self.size += 1
            print("[OK] {} berhasil ditambahkan ke antrean.".format(nama_pembeli))

    def dequeue(self):
        if self.is_empty():
            print("\n[!] Antrean Kosong! Tidak ada yang bisa dilayani.")
        else:
            pembeli = self.queue[self.depan]
            self.queue[self.depan] = None
            self.depan = (self.depan + 1) % self.kapasitas
            self.size -= 1
            print("[TIKET] Tiket berhasil terjual ke: {}".format(pembeli))

    def peek(self):
        if self.is_empty():
            print("\n[INFO] Antrean saat ini kosong.")
        else:
            print("[PEEK] Orang terdepan saat ini: {}".format(self.queue[self.depan]))

    def display(self):
        print("\n=== DAFTAR ANTREAN KONSER ===")
        if self.is_empty():
            print("Belum ada orang di dalam antrean.")
        else:
            current = self.depan
            for i in range(self.size):
                print("[{}] {}".format(i+1, self.queue[current]))
                current = (current + 1) % self.kapasitas
            print("=============================")

