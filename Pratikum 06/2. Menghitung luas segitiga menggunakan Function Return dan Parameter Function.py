#program menghitung luas segitiga menggunakan function
#Function dengan Return Value (Non-void Function)

def luasSegitiga(a, t):
    luas = a * t  / 2
    return luas
alas = 10
tinggi = 20
print ('Luas segitiga dgn alas ', alas, ' dan tinggi ', tinggi, ' adalah ',
       luasSegitiga (alas , tinggi))

#bedakan dengan program di bawah ini
#program menghitung luas segitiga menggunakan function
#Parameter Function dengan Nilai Default

def luasSegitiga2 (a, t):
    luas = a * t / 2
    print ('Luas segitiga dgn alas ', a, ' dan tinggi ', t, ' adalah ',
          luas)
alas = 10
tinggi = 20
luasSegitiga2(alas, tinggi)
