import sqlite3
import time

class Şarkı():
    def __init__(self,şarkı_ismi,sanatçı,albüm,prodüksiyon_şirketi,şarkı_süresi):
        self.şarkı_ismi = şarkı_ismi
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.prodüksiyon_şirketi = prodüksiyon_şirketi
        self.şarkı_süresi = şarkı_süresi

    def __str__(self):
        return "Şarkı İsmi : {}\nSanatçı : {}\nAlbüm : {}\nProdüksiyon Şirketi : {}\nŞarkı Süresi : {}".format(self.şarkı_ismi,self.sanatçı,self.albüm,self.prodüksiyon_şirketi,self.şarkı_süresi)

class Kütüphane():
    def __init__(self):
        self.bağlantı_oluştur()

    def bağlantı_oluştur(self):
        self.bağlantı = sqlite3.connect("kütüphane.db")
        self.cursor = self.bağlantı.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS Müzik(Şarkıİsmi TEXT,Sanatçı TEXT,Albüm TEXT,ProdüksiyonŞirketi TEXT,ŞarkıSüresi FLOAT)"
        self.cursor.execute(sorgu)
        self.bağlantı.commit()


    def müzik_listesi(self):
        sorgu = "SELECT * FROM Müzik"
        self.cursor.execute(sorgu)
        müzik_listesi = self.cursor.fetchall()

        if len(müzik_listesi) == 0:
            print("Müzik listesinizde kayıtlı şarkı bulunmamaktadır.")
        else:
            for i in müzik_listesi:
                şarkı = Şarkı(i[0],i[1],i[2],i[3],i[4])
                print(şarkı)
                print("**************************")

    def şarkı_ekle(self,şarkı):
        sorgu = "INSERT INTO Müzik VALUES(?,?,?,?,?)"
        self.cursor.execute(sorgu,(şarkı.şarkı_ismi,şarkı.sanatçı,şarkı.albüm,şarkı.prodüksiyon_şirketi,şarkı.şarkı_süresi))
        self.bağlantı.commit()

    def şarkı_sil(self,şarkı_ismi):
        sorgu_şarkı = "SELECT * FROM Müzik WHERE Şarkıİsmi = ?"
        self.cursor.execute(sorgu_şarkı,(şarkı_ismi,))
        şarkı = self.cursor.fetchall()
        if len(şarkı) == 0:
            print("Listenizde böyle bir şarkı bulunmamaktadr.")
        else:
            sorgu_sil = "DELETE FROM Müzik WHERE Şarkıİsmi = ?"
            self.cursor.execute(sorgu_sil,(şarkı_ismi,))
            self.bağlantı.commit()
            print("Şarkı müzik listenizden siliniyor...")
            time.sleep(1)
            print("Şarkı silindi.")

    def toplam_şarkı_süresi(self):
        sorgu = "SELECT SUM(ŞarkıSüresi) FROM Müzik"
        self.cursor.execute(sorgu)
        toplam_şarkı_süresi = self.cursor.fetchall()
        print(toplam_şarkı_süresi[0][0])

    def toplam_şarkı_sayısı(self):
        sorgu = "SELECT COUNT(Şarkıİsmi) FROM Müzik"
        self.cursor.execute(sorgu)
        şarkı_sayısı = self.cursor.fetchall()
        print(şarkı_sayısı[0][0])

    def tümünü_sil(self):
        sorgu = "DELETE FROM Müzik"
        self.cursor.execute(sorgu)
        self.bağlantı.commit()

    def alfabetik_sırala(self):
        sorgu = "SELECT * FROM Müzik ORDER BY Şarkıİsmi"
        self.cursor.execute(sorgu)
        müzik_listesi = self.cursor.fetchall()
        if len(müzik_listesi) == 0:
            print("Müzik listesinizde kayıtlı şarkı bulunmamaktadır.")
        else:
            for i in müzik_listesi:
                şarkı = Şarkı(i[0],i[1],i[2],i[3],i[4])
                print(şarkı)
                print("******************************")






