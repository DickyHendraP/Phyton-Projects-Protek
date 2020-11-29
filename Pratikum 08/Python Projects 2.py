#memodifikasi program projects nomer 1 di lpratikum 8
#dengan menambahkan rata rata jumlah input an
def dataStat(x) :
    d = sum(x) / len(x)
    e = max(x)
    f  = min(x)

    dataku = [d, e, f]

    return dataku

while True :
    try :
        n = int(input('Berapa banyak data yang ingin anda input nanti di program ini? (Input dalam angka) : ' ))
        break
    except ValueError :
        print ('Inputan Invalid')
        continue
dataku = []
z = 0
while (z<n) :
    try :
        bilangan = int(input('Masukkan bilangan bulat yang sesuai yang anda inginkan berapa : '))
        dataku.append(bilangan)
        z +=1
    except ValueError :
        print ('Inputan tidak Valid')
diPrintDataku = dataStat(dataku)
print(diPrintDataku)
    
