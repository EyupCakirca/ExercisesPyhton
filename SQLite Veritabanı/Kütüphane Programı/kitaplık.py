import sqlite3
import time

class Kitap():
    def __init__(self,kitap_adı,yazar,yayınevi,tür,dil,sayfa_sayısı,baskı):
        self.kitap_adı = kitap_adı
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.dil = dil
        self.sayfa_sayısı = sayfa_sayısı
        self.baskı = baskı

    def __str__(self):
        return "Kitap Adı: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nDil: {}\nSayfa Sayısı: {}\nBaskı: {}\n".format(self.kitap_adı,self.yazar,self.yayınevi,self.tür,self.dil,self.sayfa_sayısı,self.baskı)

class Kütüphane():
    def __init__(self):
        self.bağlantı_oluştur()

    def bağlantı_oluştur(self):
        self.bağlantı = sqlite3.connect("kütüphane.db")
        self.cursor = self.bağlantı.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS kitaplık (KitapAdı TEXT,Yazar TEXT,Yayınevi TEXT,Tür TEXT,Dil TEXT,SayfaSayısı INT,Baskı INT)"
        self.cursor.execute(sorgu)
        self.bağlantı.commit()

    def bağlantı_kes(self):
        self.bağlantı.close()

    def kitapları_göster(self):
        sorgu = "SELECT * FROM kitaplık"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Kitaplıkta kitap bulunmamaktadır.")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                print(kitap)

    def kitap_sorgula(self,kitap_adı):
        sorgu = "SELECT * FROM kitaplık WHERE KitapAdı = ?"
        self.cursor.execute(sorgu,(kitap_adı,))
        aranan_kitap = self.cursor.fetchall()
        if len(aranan_kitap) == 0:
            print("Aradığınız kitap kitaplıkta bulunmamaktadır.")
        else:
            kitap = Kitap(aranan_kitap[0][0],aranan_kitap[0][1],aranan_kitap[0][2],aranan_kitap[0][3],aranan_kitap[0][4],aranan_kitap[0][5],aranan_kitap[0][6])
            print(kitap)

    def kitap_ekle(self,kitap):
        sorgu = "INSERT INTO kitaplık VALUES (?,?,?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.kitap_adı,kitap.yazar,kitap.yayınevi,kitap.tür,kitap.dil,kitap.sayfa_sayısı,kitap.baskı))
        self.bağlantı.commit()

    def kitap_sil(self,kitap_adı):
        sorgu = "DELETE FROM kitaplık WHERE KitapAdı = ?"
        self.cursor.execute(sorgu,(kitap_adı,))
        self.bağlantı.commit()

    def baskı_yükselt(self,kitap_adı):
        sorgu = "SELECT * FROM kitaplık WHERE KitapAdı = ?"
        self.cursor.execute(sorgu,(kitap_adı,))
        kitap = self.cursor.fetchall()
        if len(kitap) == 0:
            print("Böyle bir kitap bulunamadı.")
        else:
            print("Baskı numarası değiştiriliyor...")
            time.sleep(1)
            baskı = kitap[0][6]
            baskı += 1
            sorgu2 = "UPDATE kitaplık SET Baskı = ? WHERE KitapAdı = ?"
            self.cursor.execute(sorgu2,(baskı,kitap_adı))
            self.bağlantı.commit()
            print("Baskı numarası arttırıldı.")

    def alfabetik_sırala_kitap_adı(self):
        sorgu = "SELECT * FROM kitaplık ORDER BY KitapAdı"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()

        for i in kitaplar:
            kitap = Kitap(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            print(kitap)

    def alfabetik_sırala_yazar(self):
        sorgu = "SELECT * FROM kitaplık ORDER BY Yazar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()

        for i in kitaplar:
            kitap = Kitap(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            print(kitap)

    def kitap_miktarı(self):
        sorgu = "SELECT COUNT(KitapAdı) FROM kitaplık"
        self.cursor.execute(sorgu)
        sayı = self.cursor.fetchall()
        print(sayı[0][0])

