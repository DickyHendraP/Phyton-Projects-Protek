#program menghitung biaya minimal bensin mobil

#import waktu
import time
import math

#variabel assigment
jarakKota=795
kapasitasTangki=50
print('Pak Budi Mengendarai Mobil dari kota A ke kota C dengan jarak 795Km' )

#operasi perhitungan
bensin=1
jarakMinimal=12
bensinDigunakan=jarakKota/jarakMinimal
tangki=bensinDigunakan-50
isiTangki=tangki/kapasitasTangki

#kasih jeda 2 detik
time.sleep(2)

#menampilkan Hasil
print('Pak Budi minimal akan Mengisi Bensin untuk sampai Ke kota C sebanyak ', math.ceil(0.325), 'kali')
