#program Modifikasi bintang dari kecil ke besar
#menjadi dari besar ke kecil

#membuat variable terlebih dahulu
kolom = 4
baris = 5

i = 0
#membuat perulangan
while (i < baris) :
   j = 0
   while (j <= kolom) :
       print('* ', end='')
       j += 1
   print( ' ' )
   i += 1
   kolom -= 1

