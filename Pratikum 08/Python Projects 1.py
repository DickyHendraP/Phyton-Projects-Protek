#Program memasukkan bilangan bulat sesuai dengan permintaan mau berapa kali
#dan setelah itu di urutkan billangan bulat tadi dari besar ke kecil
    
while True :
    try :
        n =int(input('Berupa banyak data yang ingin anda input ? (Input dalam angka) : '))
        break
    except ValueError :
        print ('Inputan Invalid')
        continue

dataku =[ ]

x = 0
while (x < n) :
    try :
        bil = int(input('Masukkan bilangan bulat yang anda inginkan : '))
        dataku.append(bil)
        x +=1
    except ValueError :
        print ('Inputan tidak valid')
dataku.sort(reverse = True)
print (dataku)
        
