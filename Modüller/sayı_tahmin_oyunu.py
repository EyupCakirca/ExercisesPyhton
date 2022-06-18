import random
import time
print("""
**********************************************
1 ile 100 arasındaki sayıyı tahmin ediniz.
Tahmin hakkınız 7'dir.
**********************************************""")

rastgele_sayı = random.randint(1,100)
tahmin_hakkı = 7
while True:
    tahmin = int(input("Tahmininiz?: "))
    if tahmin > rastgele_sayı:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Daha düşük bir sayı giriniz!")
        print("Kalan tahmin hakkınız:",tahmin_hakkı)
    elif tahmin < rastgele_sayı:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Daha yüksek bir sayı giriniz.")
        print("Kalan tahmin hakkınız:", tahmin_hakkı)
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler. Doğru tahmin ettiniz. Sayımız: ",rastgele_sayı)
        break
    if  tahmin_hakkı == 0:
        time.sleep(1)
        print("Malesef tahmin hakkınızı doldurdunuz.")
        print("Sayımız:",rastgele_sayı)
        break