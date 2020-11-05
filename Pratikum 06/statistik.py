#latihan soal 4 materi function
#stastik

#sum
def sum(*n) :
    i = 0
    for x in n :
        i = i + x
    print (i)

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
    max = n[0]
    for i in (n) :
        if (i>max):
            max = i
    print (max)

#min
def min(*n):
    min = n[0]
    for i in (n) :
        if (i < min):
            min = i
    print (min)
