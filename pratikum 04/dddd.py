import time
import datetime

nama =input("hallo...nama saya Mr. dicky, nama kamu siapa? ")
print("oh..nama anda", nama, ", nama yang bagus sekali")

time.sleep(1)

thnLahir =int(input("BTW..." + nama + " kamu lahir tahun berapa? "))

skrg=datetime.datetime.now()
usia=skrg.year-thnLahir

print("hmmm...", nama,"kamu sudah", usia,"tahun ya..")

if (usia > 50):
    print("Anda sudah cukup tua ya?")
    print("Jaga kesehatan ya!!")
elif (usia > 20):
    print("Ternyata Anda masih cukup muda belia")
    print("Jangan sia-siakan masa mudamu ya!!")
elif (usia > 17):
    print("Hihihi... Anda ternyata masih ABG")
    print("Mulai berpikirlah secara dewasa ya!!")
else:
    print("Oalah.. Anda masih anak-anak toh?")
    print("Jangan suka merengek-rengek minta jajan ya!!")

