  # LAPORAN UTS STRUKTUR DATA 

## Nama Anggota : 
1. Malvaraina Nursalim (2501010084)
2. Pande Putu Vidya Reswara (2501010064)
3. Kadek Satya Giri Sardhula (2501010088) 

### 1. Rumusan Masalah dan Solusi
1. Rumusan Masalah 1 :
Bagaimana sistem dapat mengatasi keterbatasan kapasitas antrean agar tidak terjadi overflow (antrean penuh) dan underflow (antrean kosong)?

Solusi : 
Sistem menyediakan metode is_full() dan is_empty() sebagai mekanisme validasi sebelum melakukan operasi utama. Jika antrean penuh, sistem akan menolak penambahan data dan memberikan notifikasi kepada pengguna. Sebaliknya, jika antrean kosong, sistem juga mencegah proses pengambilan data. Pendekatan ini memastikan integritas data tetap terjaga dan mencegah error saat program dijalankan.

2. Rumusan Masalah 2 :
Bagaimana meningkatkan efisiensi penggunaan memori dalam implementasi antrean menggunakan array?

Solusi : 
Program menerapkan konsep circular queue dengan operasi modulo (% kapasitas) pada indeks depan dan belakang. Hal ini memungkinkan penggunaan kembali slot array yang telah kosong akibat proses dequeue(), sehingga tidak terjadi pemborosan memori seperti pada linear queue biasa. Dengan cara ini, sistem tetap efisien meskipun menggunakan struktur array dengan ukuran tetap.

3. Rumusan Masalah 3 :
Bagaimana sistem dapat memberikan informasi posisi dan kondisi antrean secara real-time kepada pengguna?

Solusi : 
Sistem menyediakan fungsi display() untuk menampilkan seluruh isi antrean dan peek() untuk melihat pembeli yang berada di posisi terdepan. Dengan adanya fitur ini, pengguna dapat mengetahui kondisi antrean secara langsung tanpa harus memproses seluruh data secara manual, sehingga meningkatkan transparansi dan kemudahan penggunaan sistem.

4. Rumusan Masalah 4 : 
Bagaimana sistem dapat memberikan pengalaman pengguna yang informatif dalam proses antrean tiket?

Solusi : 
Sistem dilengkapi dengan output pesan yang jelas pada setiap operasi, seperti notifikasi saat antrean penuh, kosong, maupun saat transaksi berhasil dilakukan. Hal ini membantu pengguna memahami kondisi sistem tanpa kebingungan.

### 2. Landasan Teori 
Struktur data adalah cara mengorganisasi dan menyimpan data di dalam komputer agar dapat diakses dan diproses secara efisien. Dalam ilmu Ilmu Komputer, pemilihan struktur data yang tepat sangat berpengaruh terhadap kinerja algoritma, terutama dalam hal kompleksitas waktu dan ruang. Menurut Introduction to Algorithms, struktur data tidak hanya berfungsi sebagai tempat penyimpanan, tetapi juga menentukan bagaimana operasi seperti pencarian, penyisipan, dan penghapusan dilakukan secara optimal.

Salah satu konsep penting dalam struktur data adalah queue dan stack. Queue adalah struktur data yang bekerja seperti antrian, di mana elemen ditambahkan dari belakang (rear) dan dihapus dari depan (front). Sebaliknya, stack bekerja seperti tumpukan, di mana elemen ditambahkan dan dihapus dari satu sisi saja, yaitu bagian atas (top). Konsep ini banyak digunakan dalam berbagai aplikasi, seperti manajemen proses, undo-redo pada aplikasi, dan evaluasi ekspresi matematika (Weiss, 2013).

Konsep dasar yang mendasari queue dan stack adalah FIFO (First In First Out) dan LIFO (Last In First Out). Queue menggunakan prinsip FIFO, artinya elemen yang pertama masuk akan menjadi yang pertama keluar, mirip seperti antrian di kasir. Sedangkan stack menggunakan prinsip LIFO, di mana elemen terakhir yang masuk akan menjadi yang pertama keluar, seperti tumpukan buku. Menurut Data Structures and Algorithm Analysis in C, pemahaman konsep FIFO dan LIFO sangat penting karena sering muncul dalam implementasi algoritma dan sistem.

Implementasi queue dan stack dapat dilakukan menggunakan array maupun linked list. Pada array, struktur dibuat dengan ukuran tetap sehingga lebih sederhana tetapi kurang fleksibel jika data bertambah. Sedangkan pada linked list, struktur bersifat dinamis karena menggunakan node yang saling terhubung, sehingga lebih fleksibel dalam penggunaan memori. Berdasarkan penelitian dalam Journal of Computer Science and Information Systems, pemilihan antara array dan linked list biasanya disesuaikan dengan kebutuhan aplikasi, terutama terkait efisiensi memori dan kecepatan akses data.

### 3. Desain Sistem dan Implementasi
Pseudocode dari sistem tersebut adalah 

MULAI PROGRAM

INPUT kapasitas antrean
BUAT antrean kosong dengan kapasitas tersebut

SELAMA program berjalan:

TAMPILKAN menu:
1. Tambah antrean
2. Layani pembeli
3. Lihat antrean depan
4. Tampilkan semua antrean
5. Keluar

INPUT pilihan user

JIKA pilih 1:
INPUT nama pembeli
JIKA antrean penuh:
TAMPILKAN "Antrean penuh"
JIKA tidak:
MASUKKAN nama ke antrean
TAMPILKAN "Berhasil masuk antrean"

JIKA pilih 2:
JIKA antrean kosong:
TAMPILKAN "[!] Antrean Kosong! Tidak ada yang bisa dilayani."
JIKA tidak:
AMBIL orang paling depan dari antrean
TAMPILKAN "Tiket diberikan ke (nama)"

JIKA pilih 3:
JIKA antrean kosong:
TAMPILKAN "[INFO] Antrean saat ini kosong."
JIKA tidak:
TAMPILKAN orang paling depan

JIKA pilih 4:
JIKA antrean kosong:
TAMPILKAN "Belum ada orang di dalam antrean.
"
JIKA tidak:
TAMPILKAN semua isi antrean dari depan ke belakang

JIKA pilih 5:
TAMPILKAN "Program selesai"
BERHENTI

JIKA pilihan salah:
TAMPILKAN "Pilihan tidak valid"

SELESAI


### 4. Kesimpulan
Kesimpulan dari hasil implementasi sistem antrean tiket konser ini adalah bahwa rumusan masalah yang dibuat sebelumnya sudah cukup terjawab. Sistem mampu mengatur antrean pembeli dengan urut, bisa mendeteksi ketika antrean penuh atau kosong, dan juga bisa menampilkan data antrean dengan jelas. Jadi, secara umum program sudah berjalan sesuai dengan tujuan yang diharapkan.

Dari segi teori, sistem ini sudah sesuai dengan konsep dasar struktur data queue yang menggunakan prinsip FIFO (First In First Out), yaitu yang datang duluan akan dilayani duluan. Selain itu, penggunaan circular queue juga membantu supaya memori lebih efisien, karena slot yang kosong bisa dipakai lagi tanpa harus menambah kapasitas baru. Jadi bisa dibilang implementasi program ini sudah sesuai dengan teori yang dipelajari.

Manfaat penggunaan queue pada kasus ini cukup terasa, karena sistem antrean jadi lebih rapi, adil, dan mudah dikelola. Setiap pembeli tidak bisa menyerobot antrean dan semua berjalan sesuai urutan. Walaupun stack tidak digunakan langsung di program ini, konsepnya tetap penting untuk dipahami karena digunakan di kasus lain. Dari sini bisa disimpulkan bahwa struktur data seperti queue sangat membantu dalam membuat sistem yang teratur dan efisien, terutama untuk kasus antrean seperti ini.


## PPT
https://canva.link/u76bxqtc3re7xlx

