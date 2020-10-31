#Modifikasi Program game
#Program game tebak angka dengan skenario seperti ini.
#-	Komputer akan memilih sebuah bilangan bulat secara random, antara 0 s/d 100.
#-	Bilangan tersebut tersimpan dalam memori komputer
#-	Tugas pemain adalah menebak bilangan yang dipilih komputer tersebut
#-	Untuk menebak bilangan, pemain mengentri beberapa bilangan
#-	Komputer memberikan respon ‘Bilangan tebakan Anda terlalu besar’ jika bilangan yang dientri pemain lebih besar
#              dari bilangan yang dipilih komputer, atau ‘Bilangan tebakan Anda terlalu kecil’ jika bilangan yang dientri pemain
#              lebih kecil dari bilangan yang dipilih komputer. 

print('Hai...nama saya Mr. DickyHendraP, Saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!! ')
#membuat tampilan input 
ta=int(input('Tebakan Anda : '))
#membuat variable untuk di pakai di pengrangan poin
kurangpoin=0
#membuat perulangan
#jika perulangan terjadi karena nilai yang di masukkan memenuhi syarat perulangan
#dan membuat jika salah mendapatkan poin, terus nanti di kurangin poin benar 100
while True:
    if(ta<10):
        print('Heheheheh.....Bilangan tebakan anda terlalu kecil')
        ta=int(input('Tebakan Anda : '))
        kurangpoin+=2
    elif(ta>10):
        print('Hehehehehe.....Bilangan tebakan anda terlalu besar')
        ta=int(input('Tebakan Anda : '))
        kurangpoin+=2
    elif(ta==10):
        print('yeeee...Bilangan tebakan anda benar')
        score=100-kurangpoin
        print('Score anda : ' + str(score))
        break
        
