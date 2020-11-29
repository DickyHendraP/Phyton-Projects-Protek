sayur2an = ['Bayam' , 'Kangkung', 'Wortel' , 'Selada']

def tambahSayur() :
    sayur = input('Masukkan nama sayur yang ingin ditambahkan :  ' )
    sayur2an.append(sayur)
    return sayur2an

def menghapusSayur() :
    sayurMenghapus = input('Masukkan nama sayur yang ingin dihapus : ')
    sayur2an.remove(sayurMenghapus)
    return sayur2an

def sayurRead() :
    print (sayur2an)

print ('Apa yang Program bisa lakukan untukmu : ')
print ('A. Tambah data sayur')
print ('B. Hapus data sayur')
print ('C. Tampilkan data sayur')
print ('D. Keluar')


while True:
    print ()
    pilihan = input('Pilihan Anda : ')

    if  ( pilihan == 'A' or pilihan == 'a') :
        tambahSayur()
    elif (pilihan == 'B' or pilihan == 'b') :
        menghapusSayur()
    elif (pilihan == 'C' or pilihan == 'c') :
        sayurRead()
    elif (pilihan == 'D' ) :
        break
    else :
        print ('Inputan Invalid')
        continue





    
