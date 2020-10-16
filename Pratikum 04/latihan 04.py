#program perjalanan pak amir ke kota A, B, C

import time
print('====Pak Amir akan pergi dari kota A, B dan ke kota C====')
#variabel assigment
jarakAB=125
jarakBC=256
kecepatanAB=62
kecepatanBC=70
jamAB=6
menitAB=00
menitIstirahatB=45

#operasi perhitungan
#di bagi terlebih dahulu 
waktuAB=jarakAB/kecepatanAB
waktuBC=jarakBC/kecepatanBC
menitIstirahat=0.75 #45 menit adalah 0.75 jam
#di jumlahkan semua dari hasil pembagian dan menit istirahat nya
semuaMenit=waktuAB+waktuBC+menitIstirahat
#selanjutkan hasil penjumlahan di kalikan dengan 60 menit
hasilMenit=semuaMenit*60
#mecari hasil bagi dan di jadikan jam nanti nya
jam=int(hasilMenit//60)
#mencari hasil sisa bagi  dan di jadikan sebagai menit nanti nya
menit=int(hasilMenit%60)
#setelah ketemu jam dan menit nya, jadikan string terlebih dahulu
totalJM=str(jam)+str('.')+str(menit)
#untuk 6 sendiri itu adalah waktu saat berangkat, dan di kalikan float agar berubah bentuk jadi bilangan rill
totalSampai=6+float(totalJM)
time.sleep(1)
print('Pak Amir akan sampai ke kota C tepat pada Pukul ' + str (totalSampai))


