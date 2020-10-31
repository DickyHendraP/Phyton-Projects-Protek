#menghitung perulangan sebarapa banyak
from random import randint
perulangan = 0 
while True :
    bill = randint(0, 10)
    print(bill)
    perulangan+= 1
    if bill==5:
        break
print('Jumlah perulangan : ' , str(perulangan))    
