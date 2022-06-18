import math
import time
print("""
*********************************
Hesap Makinesi
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
5. Cos
6. Sin
7. Tan
8. Faktoriyel
9. x üzeri y
10. x in karekökü
11. Mutlak değer
12. EBOB
13. Log10
14. x in y ninci karekökü
Çıkmak için 'q' ye basınız.
*********************************""")

while True:
    işlem = input("Yapmak istediğiniz işlemi seçiniz: ")
    if işlem == "q":
        print("Başarıyla çıkış yaptınız.")
        break
    elif işlem == "1":
        sayı1 = int(input("Birinci sayıyı giriniz: "))
        sayı2 = int(input("İkinci sayıyı giriniz: "))
        print("İşleminiz yapılıyor...")
        toplam = sayı1 + sayı2
        time.sleep(1)
        print("Sonuç:",toplam)
    elif işlem == "2":
        sayı1 = int(input("Birinci sayıyı giriniz: "))
        sayı2 = int(input("İkinci sayıyı giriniz: "))
        print("İşleminiz yapılıyor...")
        sonuç = sayı1 - sayı2
        time.sleep(1)
        print("Sonuç:",sonuç)
    elif işlem == "3":
        sayı1 = int(input("Birinci sayıyı giriniz: "))
        sayı2 = int(input("İkinci sayıyı giriniz: "))
        print("İşleminiz yapılıyor...")
        sonuç = sayı1 * sayı2
        time.sleep(1)
        print("Sonuç:",sonuç)
    elif işlem == "4":
        sayı1 = int(input("Birinci sayıyı giriniz: "))
        sayı2 = int(input("İkinci sayıyı giriniz: "))
        print("İşleminiz yapılıyor...")
        sonuç = sayı1 / sayı2
        time.sleep(1)
        print("Sonuç:",sonuç)
    elif işlem == "5":
        sayı1 = int(input("sayıyı giriniz: "))
        sayı1 = math.radians(sayı1)
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        sonuç = math.cos(sayı1)
        print("Sonuç:",sonuç)
    elif işlem == "6":
        sayı1 = int(input("sayıyı giriniz: "))
        sayı1 = math.radians(sayı1)
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        sonuç = math.sin(sayı1)
        print("Sonuç:", sonuç)
    elif işlem == "7":
        sayı1 = int(input("sayıyı giriniz: "))
        sayı1 = math.radians(sayı1)
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        sonuç = math.tan(sayı1)
        print("Sonuç:",sonuç)
    elif işlem == "8":
        sayı1 = int(input("sayıyı giriniz: "))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        sonuç = math.factorial(sayı1)
        print("Sonuç:",sonuç)
    elif işlem == "9":
        sayı1 = int(input("Birinci sayıyı giriniz: "))
        sayı2 = int(input("İkinci sayıyı giriniz: "))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        sonuç = math.pow(sayı1,sayı2)
        print("Sonuç:",sonuç)
    elif işlem == "10":
        sayı1 = int(input("sayıyı giriniz: "))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        sonuç = math.sqrt(sayı1)
        print("Sonuç:",sonuç)
    elif işlem == "11":
        sayı1 = int(input("sayıyı giriniz: "))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        sonuç = math.fabs(sayı1)
        print("Sonuç:",sonuç)
    elif işlem == "12":
        sayı1 = int(input("Birinci sayıyı giriniz: "))
        sayı2 = int(input("İkinci sayıyı giriniz: "))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        sonuç = math.gcd(sayı1, sayı2)
        print("Sonuç:", sonuç)
    elif işlem == "13":
        sayı1 = int(input("Birinci sayıyı giriniz: "))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        sonuç = math.log10(sayı1)
        print("Sonuç:", sonuç)
    elif işlem == "14":
        sayı1 = int(input("Birinci sayıyı giriniz: "))
        sayı2 = 1 / (int(input("İkinci sayıyı giriniz: ")))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        sonuç = math.pow(sayı1, sayı2)
        print("Sonuç:", sonuç)
    else:
        print("Hatalı bir seçim yaptınız.")
        continue
