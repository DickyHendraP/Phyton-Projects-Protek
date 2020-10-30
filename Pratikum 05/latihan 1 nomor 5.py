#Modifikasi Program menentukan gaji pokok dan gaji bersih karyawan dengan berdasarkan golongan
#Golongan	Gaji Pokok	Potongan
#-A	               Rp 10.000.000	2.5%
#-B	               Rp 8.500.000	2.0%
#-C	               Rp 7.000.000	1.5%
#-D	               Rp 5.500.000	1.0%
#-	Tunjangan istri/suami	: 10% dari gaji pokok (jika statusnya menikah)
#-	Tunjangan anak		: 5% dari gaji pokok untuk setiap anak (jika memiliki anak)
#  				  dan statusnya menikah

#membuat input terlebih dahulu
kode = input('Masukkan kode karyawan    : ')
nama = input('Masukkan nama karyawan   : ')
golongan = input('Masukkan golongan             : ')
statusmenikah = input('Masukkan status (1: Sudah Menikah, 2: Belum Menikah): ')

#membuat statement jika mempunyai anak dan tidak mempunyai anak
if (statusmenikah=='1'):
    jumlahanak = int(input('Masukkan jumlah anak         : '))
    menikahbelum = 'Sudah Menikah'
    tunjanganmenikah = 10/100
    tunjangananak = 5/100*jumlahanak
else:
    jumlahanak = 0 
    menikahbelum = 'Belum Menikah'
    tunjanganmenikah = 0
    tunjangananak = 0
      
print ('===============================')

#membuat tampilan output hasil dari input
print ('STRUK RINCIAN GAJI KARYAWAN')
print ('Nama Karyawan                   : ' + nama + ' (kode : ' + kode + ')')
print ('Golongan                              : ' + golongan)
print ('Status Menikah                     : ' + menikahbelum)
print ('Jumlah Anak                         : ' + str(jumlahanak) + ' Anak')
print ('---------------------------------------------------')

##membuat statement perhitungan jumlah potongan dan gaji bersih dan tunjangan
if (golongan=='A' or  golongan=='a'):
    gajipokok=10000000
    potongan=2.5
    jumlahtunjanganmenikah=tunjanganmenikah*gajipokok
    jumlahtunjangananak=tunjangananak*gajipokok
    gajikotor=gajipokok+jumlahtunjanganmenikah+jumlahtunjangananak
    jumlahpotongan=gajikotor*potongan/100
    gajibersih=gajipokok-jumlahpotongan
elif (golongan=='B' or  golongan=='b'):
    gajipokok=8500000
    potongan=2.0
    jumlahtunjanganmenikah=tunjanganmenikah*gajipokok
    jumlahtunjangananak=tunjangananak*gajipokok
    gajikotor=gajipokok+jumlahtunjanganmenikah+jumlahtunjangananak
    jumlahpotongan=gajikotor*potongan/100
    gajibersih=gajipokok-jumlahpotongan
elif (golongan=='C' or  golongan=='c'):
    gajipokok=7000000
    potongan=1.5
    jumlahtunjanganmenikah=tunjanganmenikah*gajipokok
    jumlahtunjangananak=tunjangananak*gajipokok
    gajikotor=gajipokok+jumlahtunjanganmenikah+jumlahtunjangananak
    jumlahpotongan=gajikotor*potongan/100
    gajibersih=gajipokok-jumlahpotongan
elif (golongan=='D' or  golongan=='d'):
    gajipokok=5500000
    potongan=1.0
    jumlahtunjanganmenikah=tunjanganmenikah*gajipokok
    jumlahtunjangananak=tunjangananak*gajipokok
    gajikotor=gajipokok+jumlahtunjanganmenikah+jumlahtunjangananak
    jumlahpotongan=gajikotor*potongan/100
    gajibersih=gajipokok-jumlahpotongan

#membuat tampilan output dari perhitungan di statement di atas
print ('Gaji Pokok                            : Rp ' + str(gajipokok))
print ('Tunjangan Istri/Suami         : Rp ' + str(jumlahtunjanganmenikah))
print ('Tunjangan anak                   : Rp ' + str(jumlahtunjangananak))

print ('--------------------------------------------------- +')
print ('Gaji Kotor                             : Rp ' + str(gajikotor))
print('Potongan ( ' + str(potongan) + '%)                 : Rp ' + str(jumlahpotongan))

print ('--------------------------------------------------- -')
print ('Gaji Bersih                            : Rp ' + str(gajibersih))








