#Program Memodifikasi dari nomer 2
#Program untuk mencari data Mahasiswa Berdasarkan Nim nya
#Membuat input an untuk menuliskan nim
McrNim = input("Masukkan NIM yang mau dicari : ")
#Membuka file
file = open("file.txt", "r")
isiFile = file.readlines()
#Membuat perulangan untuk mencari file
data = 'ada'
for i in range(len(isiFile)) :
    if (McrNim in isiFile[i]):
        data = 'ada'
        mengganti = isiFile[i].replace('\n', '')
        mengubahSplit = mengganti.split('|')
        break
    else :
        data = 'tidak ada'
        continue
if (data == 'ada') :
    print("Data Mahasiswa :")
    print("NIM         : ", mengubahSplit[0])
    print("Nama      : ", mengubahSplit[1])
    print("Alamat    :", mengubahSplit[2])
        
else :
    print ("Data mahasiswa tidak ditemukan")
