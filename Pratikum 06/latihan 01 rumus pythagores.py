#latihan soal 1 materi function
#isPytagores
def isPythagores (a, b, c):
    if(a*a) == (c*c) - (b*b) or (b*b) == (c*c) - (a*a) or (c*c) == (a*a) + (b*b):
        print (True)
    else:
        print (False)

print(' ****mentukan benar tidak nya pyhtagoras****')         
#a=3, b=4, c=5        
print (' a=3, b=4, c=5  --> ', end = ' '), isPythagores(3, 4, 5)
#a=5, b=9, c=12
print (' a=5 b=9, c=12  --> ', end = ' '), isPythagores(5, 9, 12)
#a=8, b=6, c=10
print (' a=8, b=6, c=10  --> ', end = ' '), isPythagores(8, 6, 10)
#a=7, b=8, c=11
print (' a=7, b=8, c=11  --> ', end = ' '), isPythagores(7, 8, 11)

