from müzik import *

print("""
********************************************
Müzik Kütüphanesi
1. Müzik Listesi
2. Şarkı Ekle
3. Şarkı Sil
4. Toplam Şarkı Süresi
5. Toplam Şarkı Sayısı
6. Tüm Şarkıları Sil
7. Şarkı İsimlerini Alfabetik Olarak Sırala
Çıkmak için 'q' ye basınız.
********************************************""")

kütüphane = Kütüphane()
while True:
    seçim = input("Yapmak istediğiniz işlemi seçiniz: ")
    if seçim == "q":
        print("Programdan çıkılıyor...")
        time.sleep(1)
        print("Çıkış yapıldı!")
        break
    elif seçim == "1":
        kütüphane.müzik_listesi()
    elif seçim == "2":
        şarkı_ismi = input("Şarkı İsmi: ")
        sanatçı = input("Sanatçı: ")
        albüm = input("Albüm: ")
        prodüksiyon_şirketi = input("Prodüksiyon Şirketi: ")
        şarkı_süresi = float(input("Şarkı Süresi: "))

        şarkı = Şarkı(şarkı_ismi,sanatçı,albüm,prodüksiyon_şirketi,şarkı_süresi)
        print("Şarkı müzik listenize ekleniyor...")
        time.sleep(1)
        kütüphane.şarkı_ekle(şarkı)
        print("Şarkı eklendi.")
    elif seçim == "3":
        şarkı_ismi = input("Silmek istediğiniz şarkının ismini giriniz: ")
        kütüphane.şarkı_sil(şarkı_ismi)
    elif seçim == "4":
        kütüphane.toplam_şarkı_süresi()
    elif seçim == "5":
        kütüphane.toplam_şarkı_sayısı()
    elif seçim == "6":
        cevap = input("Tüm şarkıları silmek istediğinizden emin misiniz? E/H: ")
        if cevap == "E":
            print("Tüm şarkılar siliniyor...")
            time.sleep(2)
            kütüphane.tümünü_sil()
            print("Şarkılar silindi.")
        else:
            print("Silme işlemi iptal edildi.")
    elif seçim == "7":
        kütüphane.alfabetik_sırala()
    else:
        print("Hatalı seçim yaptınız.")


