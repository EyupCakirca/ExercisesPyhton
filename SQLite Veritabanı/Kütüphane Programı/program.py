from kitaplık import *

print("""
*******************************************************
Kütüphane Programı
1. Kitapları Göster
2. Kitap Sorgula
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt
6. Alfabetik Olarak Sırala Kitap Adı
7. Alfabetik Olarak Sırala Yazar
8. Kitaplıktaki Kitap Miktarı

Çıkış için 'q' ye basınız.
*******************************************************""")

kütüphane = Kütüphane()
while True:
    işlem = input("Yapmak istediğiniz işlemi seçiniz: ")
    if işlem == "q":
        print("Programdan çıkış yapılıyor...")
        time.sleep(1)
        print("Çıkış yapıldı.")
        break
    elif işlem == "1":
        kütüphane.kitapları_göster()
    elif işlem == "2":
        kitap_adı = input("Sorgulamak istediğiniz kitabın adını yazınız: ")
        print("Kitap aranıyor...")
        time.sleep(2)
        kütüphane.kitap_sorgula(kitap_adı)
    elif işlem == "3":
        kitap_adı = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        dil = input("Dil: ")
        sayfa_sayısı = int(input("Sayfa Sayısı: "))
        baskı = int(input("Baskı: "))

        yeni_kitap = Kitap(kitap_adı,yazar,yayınevi,tür,dil,sayfa_sayısı,baskı)
        print("Kitap ekleniyor...")
        time.sleep(1)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")
    elif işlem == "4":
        isim = input("Silmek istediğiniz kitabın adını yazınız: ")
        print("{} adlı kitabı silmek istediğinizden emin misiniz?(E/H)".format(isim))
        seçim = input("Cevap: ")
        if seçim == "E":
            print("Kitap siliniyor...")
            time.sleep(1)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi.")
        else:
            print("Silme işlemi iptal edildi.")
    elif işlem == "5":
        kitap_adı = input("Baskısını arttırmak istediğiniz kitabın adını yazınız: ")
        kütüphane.baskı_yükselt(kitap_adı)
    elif işlem == "6":
        kütüphane.alfabetik_sırala_kitap_adı()
    elif işlem == "7":
        kütüphane.alfabetik_sırala_yazar()
    elif işlem == "8":
        kütüphane.kitap_miktarı()
    else:
        print("Yanlış seçim yaptınız.")

