#Program memodifkasi dari program penyadian teks menjadi teks yang bisa di baca
#membuka file
kataSandi = open('HasilSandiFile.txt', 'r')
membaca = kataSandi.read()
#membuat  jumlah inputan
jumlahInput = int(input('Masukkan nilai n : '))
#menjadikan sebuah list
terjemahkan = list(membaca)
karakterTerjemahan = []
#membuat perulangan agar bisa mengubah sandi menjadi kalimat yang bisa di baca
for x in terjemahkan :
    a = ord(x)
    if (a == 32) :
        d = a
    else :
        d = a - jumlahInput
        if (d < 65) :
            d = d + 26
        elif (90 < d and d < 97) :
            d = d + 26
    Terjemahan = chr(d)
    karakterTerjemahan.append(Terjemahan)
kalimatTerjemahan = ''.join(karakterTerjemahan)
hasilTerjemahan = open('HasilTerjemahanFile.txt', 'w',)
hasilTerjemahan.write(kalimatTerjemahan)
hasilTerjemahan.close()



  
    
    
