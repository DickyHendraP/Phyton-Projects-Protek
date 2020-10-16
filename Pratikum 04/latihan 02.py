#program menghitung biaya bensin mobil

#import waktu
import time

#variabel assigment
jarakKota=795
print('Pak Budi Mengendarai Mobil dari kota A ke kota C dengan jarak 795Km' )

#operasi perhitungan
bensin=1
jarakMinimal=12
bensinDigunakan=jarakKota/jarakMinimal

#kasih jeda 2 detik
time.sleep(2)

#menampilkan Hasil
print('Pak Budi akan menghabiskan Bensin', str(bensinDigunakan) +' Liter')
print('untuk Perjalanan dari kota A ke Kota C')
print('Hati-Hati Pak Budi')
