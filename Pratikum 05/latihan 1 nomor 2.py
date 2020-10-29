#Modifikasi program menentukan status kelulusan ujian mahasiswa agar nilai tidak sembarangan
#Program menentukan status kelulusan ujian mahasiswa
#Tidak ada nilai yang kurang dari 60 dan
#Nilai matematika nya harus di atas 70

#membuat input terlebih dahulu
bindo = int(input('masukkkan nilai Bahasa Indonesia : '))
mtk = int(input('masukkan nilai Matematika : ' ))
ipa = int(input('masukkan nilai ipa : '))

print('===============================')
print (' ')

#membuat  statement  nilai  jika di masukkan tidak sesuai maka akan tidak valid
if  (bindo<0 or bindo>100):
    print ("Maaf input ada yang tidak valid")
elif (mtk<0 or mtk>100):
    print ("Maaf input ada yang tidak valid")
elif (ipa<0 or ipa>100):
    print ("Maaf input ada yang tidak valid")

#perhitungan nilai untuk menentukan lulus atau tidak
elif (bindo>60 and mtk>70 and ipa>60):
    print ("Status kelulusan : Lulus")    
else :
    print ("Status kelulusan : Tidak Lulus")



