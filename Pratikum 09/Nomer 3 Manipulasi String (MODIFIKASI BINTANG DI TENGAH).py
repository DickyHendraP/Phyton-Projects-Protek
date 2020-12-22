#Membuat susunan bintang dengan bentuk menengah
#Memodifikasi Bintang

def Bintang(n) :

    puncakBintang = int(n / 2 + 1)
    
    for i in range(1, n+1) :
        formasi = "*" * (1 +(i-1)*2)
        print (formasi.center(15))

        if (i == puncakBintang) :

            for i in range(puncakBintang - 1, 0, -1) :
                formasi = "*" * (1 +(i-1)*2)
                print (formasi.center(15))
            break
    
Bintang(7)
