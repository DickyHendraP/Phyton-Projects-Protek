#Program untuk mencari data peminjaman buku berdasarkan kode number yang tersimpan di dalam teks
#Program akan  otomatis akan mengeluarkan  denda 2000/hari jika terlambat mengembalikan buku

#mengimport datetime dan import  program Nomer 1
from datetime import *
import Nomer1

#membuat  untuk membaca file
fileTeks = open('dataDiriPeminjamanBuku.txt', 'r')
isiTeks = fileTeks.readlines()

#membuat untuk inputan
kodeBuku = input('Masukkan Kode Member : ')

#membuat perulangan untuk mencari data peminjaman buku
for x in range(len(isiTeks)) :
    if (kodeBuku in isiTeks[x]) :
        membagi = isiTeks[x].split('|')
        statusBuku = 'ada'
        break
    
    else :
        statusBuku = 'tidak ada'
        continue

#membuat percabangan agar bisa menemukan data peminjaman buku
if (statusBuku == 'ada'):
    print('Data Peminjam Buku')
    print('Kode Member   : ', membagi[0])
    print('Nama Member  : ', membagi[1])
    print('Judul Buku          : ', membagi[2])
    print('Tanggal Mulai Peminjaman         : ', membagi[3])
    print('Tangal Pengambilan Maksimal    : ', membagi[4])
    print('Tanggal Pengembalian Buku        : ', datetime.date(datetime.now()))

    #membuat rumus agar bisa mencetak denda jika terlambat mengembalikan buku
    telatPengembalian = Nomer1. diffDate(membagi[4])
    dendaTelat = 2000 * abs(telatPengembalian)

    #membuat percabangan pengambilan buku terlambat atau tidak
    if(telatPengembalian >= 0 ) :
        print('Terlambat : 0 hari')
        print('Denda       : 0')
    else :
        print('Terlambat : ', abs(telatPengembalian))
        print('Denda       : ', dendaTelat)
else :
    print('Peminjaman Buku Tidak Ada')
            


        
