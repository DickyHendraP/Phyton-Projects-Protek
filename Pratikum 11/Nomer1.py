#Program untuk menghitung selisih hari

#Mengimport datetime
from datetime import *

#membuat function
def diffDate (x) :
    membagi = x.split('-')
    listHari = []
    #membuat perulangan  untuk menghitung hari
    for y in membagi :
        listHari.append(int(y))

    hari = date(listHari[0], listHari[1], listHari[2])
    hariIni = datetime.date(datetime.now())

    selisihHari = hari - hariIni
    hasilSelisih = abs(selisihHari.days)
    #menyimpan hasil perhitungan hari
    return hasilSelisih

#mencoba Program untuk menghitung selisih hari
'''
print(diffDate('2021-01-20'))
print(diffDate('2020-12-20'))
print(diffDate('2022-09-10'))
'''
#membuat program jika user yang harus menginput tahun, bulan, dan tanggal
'''
#Membuat Input dan mengatasi jika input tidak sesuai
try :
    hariSekarang = input('Ketikkan tanggal yang sesuai dengan kenginan anda, dengan Format (yyyy-mm-dd) : ')
    diff = diffDate(hariSekarang)
    #Membuat Output dari hasil perhitungan selisih
    print ('Selisih dengan tanggal yang di input adalah : ', diff, 'hari')
except ValueError :
    print('Jangan ada spasi/tidak valid')
'''
