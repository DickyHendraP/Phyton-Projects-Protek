def kuadrat (bil) :
    bilSquare = []

    for d in range(len(bil)) :
        kali = bil[d] * bil[d]
        bilSquare.append(kali)
    return bilSquare

databil = [2, 4, 5, 6, 12]
hasil = kuadrat(databil)
print (hasil)
