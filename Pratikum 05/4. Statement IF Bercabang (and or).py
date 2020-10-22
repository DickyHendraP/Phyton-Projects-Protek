#Statement IF Bercabang (and or)

a=-2
b=-7
if (a>0)and(b>0):
    print('Keduanya Positif')
elif (a>0)or(b>0):
    print('Salah Satu Positif')
elif (a<0)or(b<0):
    print('Salah Satu Negatif')
elif (a<0)and(b<0):
    print('Keduanya Negatif')
