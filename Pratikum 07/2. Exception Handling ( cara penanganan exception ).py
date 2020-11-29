
try :
    #membuka dan mau membaca file c:/data.txt
    file = open ('c:/Users/dickyhe/Documents/GitHub/Phyton Projects/Phyton-Projects-Protek/Pratikum 07/data.txt', 'r')
    #baca baris pertama dari file
    #simpan ke dalam variable bil1 sbg integer
    bil1 = int(file.readline())
    #baca baris kedua dari file
    #simpan ke dalam variable bil2 sbg integer
    bil2 = int(file.readline())
    #hitung dari tampilkan hasil bagi
    hasil = bil1/bil2
    print(bil1 + 'dibagi', bil2 , 'sama dengan' , hasil)
#mencegah terjadi karena pembagian dengan nol
except ZeroDivisionError :
    print('Tidak boleh pembagian dengan nol')
#mencegah terjadi jika file nya tidak di temukan
except FileNotFoundError :
    print('File tidak ditemukan')

    
