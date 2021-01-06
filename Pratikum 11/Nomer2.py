#Program untuk menyimpan data pinjaman buku (maksimal pengembilan 7 hari)

#Mengimport datetime dan os
from datetime import  *
import os

#membuat ketentuan menulis teks dan membuat teks
if (os.path.exists('dataDiriPeminjamanBuku.txt')) :
    fileTeksMode = 'a'
else :
    fileTeksMode = 'w'
fileTeks = open('dataDiriPeminjamanBuku.txt', fileTeksMode)

#membuat perulangan untuk menulis data diri peminjaman buku di teks
while True :

    kode = input('Masukkan Kode Member   : ')
    nama = input('Masukkan Nama Member : ')
    judul = input('Masukkan Judul Buku          : ')

    hariPeminjaman = date.today()
    hariDikembalikan = hariPeminjaman + timedelta(days = 7 )

    dataDiriPeminjam = [kode, nama, judul, str(hariPeminjaman), str(hariDikembalikan), '\n']
    fileTeks.write('|'.join(dataDiriPeminjam))

    #Membuat perulangan jika ingin menambahkan data diri peminjaman buku
    ulang = input('Ulangi lagi (y/n) : ')

    if (ulang == 'y' or ulang == 'Y') :
        continue
    elif (ulang == 'n' or ulang == 'N') :
        break
    else :
        print('masukkan input yang benar')

#menutup file teks
fileTeks.close()
