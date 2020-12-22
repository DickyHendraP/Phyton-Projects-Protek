#Mengubah ('MATEMATIKA', 'T', 'S')

#Menggunakan cara sederhana yaitu : replace()
def HurufBaru(teks, a,b) :
    TeksNew = teks.replace(a, b)
    print(TeksNew)

#menggunakan cara lain dengan di ubah ke list > loppoing > baru di join
def BergantiHuruf(teks, a, b) :
    listTeks = list(teks)
    for i in range(len(listTeks)) :
        if(listTeks[i] == a) :
            listTeks[i] = b
        else :
            continue
    x = "".join(listTeks)
    print (x)
teks = "MATEMATIKA"
a = "T"
b = "S"

#mencetak hasil output nya
HurufBaru(teks,a,b)
BergantiHuruf(teks,a,b)
