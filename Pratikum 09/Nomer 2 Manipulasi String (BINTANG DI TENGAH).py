#Membuat susunan bintang dengan bentuk menengah

def Bintang(n) :
    for i in range(n) :
        perhitungan = i + 1
        bintangUnik = "*" * (i + perhitungan)
        print(bintangUnik.center(15))
Bintang (4)
