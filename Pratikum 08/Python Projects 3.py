namaData = []
i = True

while(i == True) :
    nama = input (' Masukkan Nama : ')
    namaData.append(nama)

    selanjutnya = input('Input Nama Lagi ? (y/n) ')

    if (selanjutnya == 'y') :
        i = True

    elif (selanjutnya == 'n') :
        i = False

    else :
        print ( 'Input Invalid')
        break
print ()
namaData.sort()

for x in range(len(namaData)) :
    print(namaData[x], '(' , len(namaData[x]), 'karakter ) ' ) 
    
    
