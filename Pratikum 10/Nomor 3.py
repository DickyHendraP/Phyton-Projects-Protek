#Program Memofifikasi dari nomor 2
#Program akan diperoleh variable bertipe data ditionari
#Membuka file
file = open("file.txt" , "r")
#Membaca file secara per baris
data = file.readlines()
#Membuat dictionari kosong
dataMHS = {}
for i in range(len(data)) :
    Mhs = data[i]
    #Memisah data 
    a,b,c = Mhs.split('|')
    a,b,c= a,b,c.replace('\n', '')
    #Membuat Dictionari
    dataMahasiswa = {'nim' : a, 'nama' : b, 'alamat' : c}
    dataMHS[a] = dataMahasiswa
print(dataMHS)
#Menutup file
file.close
