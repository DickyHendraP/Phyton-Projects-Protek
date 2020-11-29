try :
    file = input('Masukkan Nama File : ' )
    print('Isi file', file, 'adalah : ')
    print(open (file, 'r').read())
except FileNotFoundError:
    print('###File tidak ditemukan###')
except UnicodeDecodeError:
    print('***Maaf, File tidak bisa dibuka, Karena tidak berformat ".txt"***')

