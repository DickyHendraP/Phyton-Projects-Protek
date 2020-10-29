#Program menentukan gaji pokok dan gaji bersih karyawan dengan berdasarkan golongan
#Golongan	Gaji Pokok	Potongan
#-A	               Rp 10.000.000	2.5%
#-B	               Rp 8.500.000	2.0%
#-C	               Rp 7.000.000	1.5%
#-D	               Rp 5.500.000	1.0%

#membuat input terlebih dahulu
kode = input('Masukkan kode karyawan    : ')
nama = input('Masukkan nama karyawan   : ')
golongan = input('Masukkan golongan             : ')

#membuat tampilan output untuk mengetahui struck gaji karyawan dengan nama dan golongan 
print ('==============================')
print ('STRUK RINCIAN GAJI KARYAWAN')
print ('Nama Karyawan                   : ' + nama + '   (kode  : ' + kode + ')')
print ('Golongan                              : ' + golongan)
print ('-------------------------------------------------')

#membuat statement perhitungan jumlah potongan dan gaji bersih
if (golongan=='A' or  golongan=='a'):
    gajipokok = 10000000
    potongan = 2.5
    jumlahpotongan = gajipokok*potongan/100
    gajibersih = gajipokok-jumlahpotongan
elif (golongan=='B' or  golongan=='b'):
    gajipokok = 8500000
    potongan = 2.0
    jumlahpotongan = gajipokok*potongan/100
    gajibersih = gajipokok-jumlahpotongan
elif (golongan=='C' or  golongan=='c'):
    gajipokok =7000000
    potongan =1.5
    jumlahpotongan = gajipokok*potongan/100
    gajibersih = gajipokok-jumlahpotongan
elif (golongan=='D' or  golongan=='d'):
    gajipokok = 5500000
    potongan = 1.0
    jumlahpotongan = gajipokok*potongan/100
    gajibersih = gajipokok-jumlahpotongan

#membuat tampilan output dari perhitungan di statement di atas
print ('Gaji Pokok                            : Rp ' + str(gajipokok))
print ('Potongan ( ' + str(potongan) + '%)                 : Rp ' + str(jumlahpotongan))
print ('-------------------------------------------------')
print ('Gaji Bersih                            : Rp ' + str(gajibersih))







