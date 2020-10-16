#program grafik mahasiswa PTIK 2020

import time
print('====Program Membuat Diagram Jumlah Mahasiswa===')
time.sleep(1)
print('Silahkan Isi Berapa Jumlah Mahasiswa...')
#input data mahasiswa
lakiLaki=int(input('Berapa Jumlah Mahasiswa Laki-laki di Jurusan PTIK UNS?'))
perempuan=int(input('Berapa Jumlah Mahasiswa Perempuan di Jurusan PTIK UNS?'))
#membagi berapa jumlah mahasiswa yang sudah di input
lk=int(lakiLaki/10)
pr=int(perempuan/10)
#menampilkan grafik
print('Laki-laki='+'*'*(lk))
print('perempuan='+'*'*(pr))
print('Berikut di atas adalah data grafik Mahasiswa dan Mahasiswi PTIK UNS 2020')
