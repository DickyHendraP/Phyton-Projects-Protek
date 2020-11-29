#membuka dan mau membaca file c:/data1.txt
file = open('c:/Users/dickyhe/Documents/GitHub/Phyton Projects/Phyton-Projects-Protek/Pratikum 07/data1.txt', 'r')

#rumus untuk menjumlahkan semua bilangan yang ada di dalam file data1.txt
#dan terjadi eror karena file tidak valid, bisa di atasi dengan blok try-except ValueError
sum = 0
for data in file:
    try :
        sum = sum + int(data)
    except ValueError:
        continue
print (sum)
