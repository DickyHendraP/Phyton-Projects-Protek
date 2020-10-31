#Modifikasi Program untuk menampilkan bilangan bulat dari 0 sampai dengan 100 yang ganjil
#bisa menampilkan banyaknya bilangan bulat dari 0 sampai 100 yang ganjil

#Membuat Variable i=1 dan k=0
k=0
i=1
##membuat perulangan jika i masih di kurang dari 100 maka akan masuk mencetak i
#dan i di tambah dengan 2
#dengan begitu maka yang di cetak adalah angka ganjil semua dari 1 sampai dengan 99
#variable k di sini berfungsi untuk mengitung berapa banyak jumlah bilangan genap
while (i <=100):
    print(i) 
    i=i + 2
    k=k+1
#membuat tampilan output untuk mengetahui bilangan genap ada berapa
print('Jumlah bilangan ganjil : '+ str(k))
