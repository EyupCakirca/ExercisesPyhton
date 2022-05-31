import time
import random

class Menü():
    def __init__(self,parlaklık = 50,kontrast = 50,güncel_yuva = ["HDMI-1"]):
        self.parlaklık = parlaklık
        self.kontrast = kontrast
        self.güncel_yuva = güncel_yuva
    def parlaklık_ayarı(self):
        print("Parlaklığı arttırmak için :'+'\nParlaklığı azaltmak için :'-'\nÇıkış için :'ç' tuşlarına basınız.")
        while True:
            seçim = input("Bir tuşa basınız : ")
            if seçim == "+":
                if self.parlaklık > 0 and self.parlaklık < 100:
                    print("Parlaklık attırılıyor...")
                    self.parlaklık += 1
                    print("Parlaklık seviyesi :", self.parlaklık)
            elif seçim == "-":
                if self.parlaklık > 0 and self.parlaklık < 100:
                    print("Parlaklık azaltılıyor...")
                    self.parlaklık -= 1
                    print("Parlaklık seviyesi :", self.parlaklık)
            elif seçim == "ç":
                print("Çıkış yapıldı. Parlaklık seviyesi :", self.parlaklık)
                break
            else:
                print("Yanlış tuşa bastınız.")
    def kontrast_ayarı(self):
        print("Kontrastı arttırmak için :'+'\nKontrastı azaltmak için :'-'\nÇıkış için :'ç' tuşlarına basınız.")
        while True:
            seçim = input("Bir tuşa basınız : ")
            if seçim == "+":
                if self.kontrast > 0 and self.kontrast < 100:
                    print("Kontrast attırılıyor...")
                    self.kontrast += 1
                    print("Kontrast seviyesi :", self.kontrast)
            elif seçim == "-":
                if self.kontrast > 0 and self.kontrast < 100:
                    print("Kontrast azaltılıyor...")
                    self.kontrast -= 1
                    print("Kontrast seviyesi :", self.kontrast)
            elif seçim == "ç":
                print("Çıkış yapıldı. Kontrast seviyesi :", self.kontrast)
                break
            else:
                print("Yanlış tuşa bastınız.")
    def yuva_ekle(self):
        print("Mevcut yuva Listesi :",self.güncel_yuva)
        yuva = input("Eklemek istediğiniz yuva ismini büyük harflerle giriniz : ")
        self.güncel_yuva.append(yuva)
        print("Güncel yuva listesi :",self.güncel_yuva)
    def yuva_sil(self):
        print("Mevcut yuva Listesi :", self.güncel_yuva)
        yuva = input("Silmek istediğiniz yuva ismini büyük harflerle giriniz : ")
        self.güncel_yuva.remove(yuva)
        print("Güncel yuva listesi :",self.güncel_yuva)
    def yuva_listesi(self):
        return "Bağlı yuva isimleri : {}".format(self.güncel_yuva)

class Kumanda(Menü):
    def __init__(self,durum = "kapalı",ses = 10,kanal_listesi = ["TRT","KANAL D","ATV","FOX","STAR"],kanal = "TRT"):
        super().__init__(parlaklık = 50,kontrast = 50,güncel_yuva = ["HDMI-1"])
        self.durum = durum
        self.ses = ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def __str__(self):
        return "Televizyon Bilgileri\nTv Durumu : {}\nSes Seviyesi : {}\nKanal Listesi : {}\nSon İzlenen Kanal : {}\nParlaklık Seviyesi : {}\nKontrast Seviyesi : {}\nYuva Listesi : {}".format(self.durum,self.ses,self.kanal_listesi,self.kanal,self.parlaklık,self.kontrast,self.güncel_yuva)
    def __len__(self):
        return len(self.kanal_listesi)

    def aç(self):
        if self.durum == "kapalı":
            print("Tv açılıyor...")
            self.durum = "açık"
    def kapat(self):
        if self.durum == "açık":
            print("Tv kapanıyor...")
            self.durum = "kapalı"
    def ses_ayar(self):
        print("Sesi arttırmak için :'+'\nSesi azaltmak için :'-'\nÇıkış için :'ç' tuşlarına basınız.")
        while True:
            seçim = input("Bir tuşa basınız : ")
            if seçim == "+":
                if self.ses > 0 and self.ses < 30:
                    print("Ses attırılıyor...")
                    self.ses += 1
                    print("Ses seviyesi :",self.ses)
            elif seçim == "-":
                if self.ses > 0 and self.ses < 30:
                    print("Ses azaltılıyor...")
                    self.ses -= 1
                    print("Ses seviyesi :",self.ses)
            elif seçim == "ç":
                print("Çıkış yapıldı. Ses seviyesi :",self.ses)
                break
            else:
                print("Yanlış tuşa bastınız.")
    def kanal_ekle(self):
        print("Eklemek istediğiniz kanal/kanalları büyük harfle ve aralarında ',' işareti olacak şekilde giriniz.\nMevcut kanal listesi :",self.kanal_listesi)
        kanal_giriş = input("Kanal/kanallar : ")
        liste = kanal_giriş.split(",")
        print("Kanal/kanallar ekleniyor...")
        time.sleep(1)
        for eklenecekler in liste:
            self.kanal_listesi.append(eklenecekler)
        print("Ekleme işlemi tamamlandı. Kanal listesi :",self.kanal_listesi)
    def kanal_sil(self):
        print("Silmek istediğiniz kanal/kanalları büyük harfle ve aralarında ',' işareti olacak şekilde giriniz.\nMevcut kanal listesi :",
            self.kanal_listesi)
        kanal_giriş = input("Kanal/kanallar : ")
        liste = kanal_giriş.split(",")
        print("Kanal/kanallar siliniyor...")
        time.sleep(1)
        for silinecekler in liste:
            self.kanal_listesi.remove(silinecekler)
        print("Silme işlemi tamamlandı. Kanal listesi :",self.kanal_listesi)

    def rastgele_kanal_geçme(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("İzlediğiniz kanal :",self.kanal)

def menü():
    print("""
    **************************************
    Televizyon Ayar Menüsü
    1. Parlaklık Ayarı
    2. Kontrast Ayarı
    3. Yuva Ekleme
    4. Yuva Silme
    5. Yuva Listesi
    Çıkmak için 'q' ye basınız.
    **************************************""")
    while True:
        seçim = input("Yapmak istediğiniz işlemş seçiniz : ")
        if seçim == "q":
            print("Menüden Çıkıldı...")
            break
        elif seçim == "1":
            kumanda.parlaklık_ayarı()
        elif seçim == "2":
            kumanda.kontrast_ayarı()
        elif seçim == "3":
            kumanda.yuva_ekle()
        elif seçim == "4":
            kumanda.yuva_sil()
        elif seçim == "5":
            print(kumanda.yuva_listesi())
        else:
            print("Hatalı seçim yaptınız!")

kumanda = Kumanda()
print("""
******************************************
Televizyon Uygulaması
1. Tv Aç
2. Tv Kapat
3. Ses Ayarla
4. Kanal Ekle
5. Kanal Sil
6. Kanal Sayısını Öğrenme
7. Rastgele Kanala Geçme
8. Televizyon Bilgileri
9. Ayar Menüsü
Çıkmak için 'q' ye nasınız...""")

while True:
    işlem = input("Yapmak istediğiniz işllemi saçiniz: ")
    if işlem == "q":
        print("Programdan Çıkıldı...")
        break
    elif işlem == "1":
        kumanda.aç()
    elif işlem == "2":
        kumanda.kapat()
    elif işlem == "3":
        kumanda.ses_ayar()
    elif işlem == "4":
        kumanda.kanal_ekle()
    elif işlem == "5":
        kumanda.kanal_sil()
    elif işlem == "6":
        print("Kanal Sayısı :",len(kumanda))
    elif işlem == "7":
        kumanda.rastgele_kanal_geçme()
    elif işlem == "8":
        print(kumanda)
    elif işlem == "9":
        menü()
    else:
        print("Hatalı işlem!")
