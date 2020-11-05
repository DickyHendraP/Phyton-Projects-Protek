#latihan soal 3 materi function
#Faktorial
def faktorial (n) :
    faktorialN = 1
    while (n > 0):
        faktorialN = faktorialN * n
        n -= 1
    return faktorialN

def kombinasi (a, b) :
    c = a-b
    hasil = faktorial (a) / (faktorial (b) * faktorial (c))
    print (hasil)

def permutasi (a, b) :
    c = a-b
    hasil = faktorial (a) / faktorial (c)
    print (hasil)

#C = kombinasi
a = 5
b = 3
print(' Kombinasi dari (5,3) = ', end = ' ' ), kombinasi (5, 3)

#P = permutasi
o = 10
p = 7
print(' Permutasi dari (10,7) = ', end = ' ' ), permutasi (10, 7)
