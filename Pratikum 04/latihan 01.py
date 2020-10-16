#program Rental Mobil Jaya Abadi

#iimport modul time
import time

#perkenalan
print('====Selamat Datang di Rental Mobil Jaya Abadi===')
nama=input('Hallo...Nama saya Dicky Pemilik Rental Mobil Jaya Abadi, Nama Anda Siapa?')
print('Silahkan...' + nama, ', untuk Harga Tarif dan Berapa Lama Mobil di Sewa kan bisa di lihat dulu')

#kasih jeda 2 deitk
time.sleep(2)

#variable assigment
jamMulai=6
menitMulai=00
print('Mobil mulai di sewa pada pukul 06:00')

jamSelesai=23
menitSelesai=50
print('Mobil dikembalikan pada pukul 23:50')

#operasi perhitungan
jamSewa=jamSelesai-jamMulai
menitSewa=menitSelesai-menitMulai
lamaSewa=jamSewa+menitSewa/60
totalSewa=int(lamaSewa)
totalBiaya=200000 + (10000*(totalSewa-12))

#kasih jeda 2 detik
time.sleep(2)

#tampilkanhasil
print('Biaya yang akan di keluarkan untuk Rental Mobil adalah : '+ str(totalBiaya))
