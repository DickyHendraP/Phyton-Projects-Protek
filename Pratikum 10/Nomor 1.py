#Program Menjumlahkan bilangan Genap dan Ganjil
#Membuka file
file = open('IsiFileAngka.txt', 'r')
#Membaca File
IsiFileAngka = file.readlines()
#Menghitung Jumlah angka Genap dan Ganjil
angkaGenap = []
angkaGanjil = []
for i in range(len(IsiFileAngka)):
    if ('\n' in IsiFileAngka[i] == True):
        IsiFileAngka[i].replace('\n', '')

        if (int(IsiFileAngka[i])%2 == 0):
            angkaGenap.append(IsiFileAngka[i])
        else :
            angkaGanjil.append(IsiFileAngka[i])
    else :
        if (int(IsiFileAngka[i])%2 == 0) :
            angkaGenap.append(IsiFileAngka[i])
        else :
            angkaGanjil.append(IsiFileAngka[i])
#Menampilkan bilangan Genap dan Ganjil
print ("Banyaknya bilangan Genap : {0}".format(len(angkaGenap)))
print ("Banyaknya bilangan Genap : {0}".format(len(angkaGanjil)))
