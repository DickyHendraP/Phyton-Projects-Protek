#latihan soal 5 materi function
#menghitung nilai rata-rata, maks, dan min

#avarage
def avarage(*n):
    i = 0
    j = 0
    for x in n :
        i = i + x
        j += 1
    avarage = i/j
    print (avarage)

#maks
def max (*n):
    max = n [0]
    for i in (n) :
        if (i > max):
            max = i
    print (max)

#min
def min(*n):
    min = n[0]
    for i in (n) :
        if (i < min):
            min = i
    print (min)

print (' Nilai Rata - rata (5,10,4,9,30,16,2,11) = ', end = ' '), avarage(5,10,4,9,30,16,2,11)
print (' Nilai Maks (5,10,4,9,30,16,2,11) = ', end = ' '), max(5,10,4,9,30,16,2,11)
print (' Nilai Min (5,10,4,9,30,16,2,11) = ', end = ' '), min(5,10,4,9,30,16,2,11)
print()
print (' Nilai Rata - rata (81,98,12,83,45,77,69,30,56) = ', end = ' '), avarage(81,98,12,83,45,77,69,30,56)
print (' Nilai Maks (81,98,12,83,45,77,69,30,56) = ', end = ' '), max(81,98,12,83,45,77,69,30,56)
print (' Nilai Min (81,98,12,83,45,77,69,30,56) = ', end = ' '), min(81,98,12,83,45,77,69,30,56)
