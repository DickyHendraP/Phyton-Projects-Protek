#Program menentukan status kelulusan ujian mahasiswa
#Tidak ada nilai yang kurang dari 60 dan
#Nilai matematika nya harus di atas 70

#=======================================
#membuat input terlebih dahulu
#input an akan berjalan terus jika memenuhi syarat
bindo = int(input('masukkkan nilai Bahasa Indonesia : '))
if (bindo >=0 and bindo <=100):
    mtk = int(input('masukkan nilai Matematika : '))
if (mtk>=0 and mtk <=100):
    ipa=int(input('masukkan nilai Ipa : '))
if (ipa>=0 and ipa <=100):
    print('===================')
    print(' ')

#perhitungan nilai untuk menentukan lulus atau tidak
if (bindo >60 and mtk>70 and ipa>60):
    print ('Status Kelulusan : Lulus')
else:
    print ('Status Kelulusan : Tidak Lulus')
