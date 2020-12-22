#Membuat Pengacakan sebuah karakter

import random

def randomizedString(z, n) :

    listRandom = []

    for i in range (n) :
        x = list(random.sample(z, len(z)))
        y = ''.join(x)

        if (y in listRandom) :
            continue
        else :
            listRandom.append(y)
            print(y)

teks = input("Silahkan masukkan teks yang ingin anda acak : ")
n = int(input("Berapa banyak hasil yang akan di acak nanti ? "))

randomizedString(teks,n)

