#Membuat tabel list data diri Mahasiswa
#Dengan ;
#- Gunakan split() untuk memecah string dalam list ke dalam beberapa substring
# - Untuk mengubah urutan tanggal lahir, juga terlebih dahulu dipecah dengan split()

mahasiswa = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

listBaru = []

for i in range(len(mahasiswa)) :
    x = mahasiswa[i].split(':')
    listBaru.append(x)

    y = listBaru[i][2].split('-')
    y.reverse()

    yJoin = '/'.join(y)
    listBaru[i][2] = yJoin

print ('=' * 65)
print ("NIM".ljust(10), "NAMA MAHASISWA".ljust(20), "TGL LAHIR".ljust(20), "TEMPAT LAHIR".ljust(10))
print ('-' * 65)

for i in range(len(listBaru)) :
       print (listBaru[i][0].ljust(10), listBaru[i][1].ljust(20), listBaru[i][2].ljust(20), listBaru[i][3].ljust(10))
