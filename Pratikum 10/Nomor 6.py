#Program membuat sandi dari sebuah teks kemudian hasil sandi di letakkan di teks yang berbeda
#membuka file
namaSandi = input('Masukkan tempat penyimpanan file berada di mana : ')
jumlahAcak = int(input('Masukkan nilai n : '))
awal = open(namaSandi, 'r')
char = awal.read()
#mengubah menjadikan list
huruf = list(char)
fileTersandi = []
#membuat perulangan agar kata sandi bisa bergeser secara n kali
for i in huruf :
    Ascii1 = ord(i)
    if (Ascii1 == 32) :
        Ascii2 = Ascii1
    else :
        Ascii2 = Ascii1 +  jumlahAcak
        if (Ascii2 > 122) :
            Ascii = Ascii2 -26
        elif (Ascii2 > 90 and Ascii2 < 97) :
            Ascii2 = Ascii2 -26
    sandi = chr(Ascii2)
    fileTersandi = fileTersandi + [sandi]
    if not huruf :
        break
kataSandi = ''.join(fileTersandi)
hasilSandi = open('HasilSandiFile.txt', 'a')
hasilSandi.write(kataSandi)
hasilSandi.close()
        
