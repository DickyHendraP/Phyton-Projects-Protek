buah = {'Apel' : 5000,
        'Jeruk' : 8500,
        'Mangga' : 7800,
        'Duku' : 6500}
def singPalingMahal (dictionary) :
    key  = list (dictionary.keys())
    values = tuple (dictionary.values())

    HargaMahal = max (values)

    indexHargaMahal = values.index(HargaMahal)

    print (key[indexHargaMahal])

singPalingMahal (buah)
        
