#Program untuk membuat penjumlahan data dari sebuah file text
#membuka file
start = open('BilanganPenjumlahan.txt', 'r')
finish = open('HasilPenjumlahan.txt', 'a')
file = start.readlines()
#membuat perulangan untuk menjumlahkan data
for i in range(len(file)) :
    bil = file[i]
    bil1, bil2 = bil.split('|')
    bil3 = int(bil1) + int(bil2)
    bil4 = str(bil3)
    finish.write(bil4)
    finish.write('\n')
#menutup file
finish.close()
#meletakkan hasil pejumlahan data di sebuah text
hasil = open('HasilPenjumlahan.txt', 'r')
print(hasil.read())
#menutup file
hasil.close
