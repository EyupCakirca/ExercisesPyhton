class Dosya():

    def __init__(self):

        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_içeriği = file.read()
            kelimeler = dosya_içeriği.split()
            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(",")
                i = i.strip(".")

                self.sade_kelimeler.append(i)

            self.kelimeler_kümesi = set()

            for i in self.sade_kelimeler:
                self.kelimeler_kümesi.add(i)

    def tüm_kelimeler(self):

        print("Tüm kelimeler............")

        for i in self.kelimeler_kümesi:
            print(i)
            print("***************************")

    def kelime_frekansı(self):

        kelime_sözlük = dict()

        for i in self.sade_kelimeler:
            if (i in kelime_sözlük):
                kelime_sözlük[i] += 1
            else:
                kelime_sözlük[i] = 1
        for kelime,sayı in kelime_sözlük.items():
            print("{} kelimesi {} defa geçiyor.".format(kelime,sayı))
            print("----------------------------")

    def arama_işlemi(self,kelime):

        sayı = 0
        for i in self.sade_kelimeler:
            if i == kelime:
                sayı += 1
        if sayı != 0:
            print("{} kelimesi {} adet metinde geçmektedir.".format(kelime,sayı))
        else:
            print("Aradığınız kelime metinde bulunmamaktadır.")

    def toplam_kelime(self):
        sayı = len(self.kelimeler_kümesi)

        print("Metinde toplam {} farklı kelime bulunmaktadır.".format(sayı))

    def alfabetik_sıra(self):
        büyük_harf = list()
        liste = list(self.kelimeler_kümesi)
        for i in liste:
            i = i.upper()
            büyük_harf.append(i)
        sıralama = sorted(büyük_harf)
        for i in sıralama:
            print(i)


dosya = Dosya()
print("""
***************************
METİN İŞLEMLERİ
1. Metinde hangi kelimeler geçiyor?
2. Metinde hangi kelimeden kaç adet geçiyor?
3. Metin içerisinde arama yapma işlemi.
4. Metinde toplam kaç farklı kelime vardır?
5. Metindeki kelimeleri alfabetik olarak sırala.

Çıkamk için 'q' ye basınız...
***************************
""")
while True:
    işlem = input("Yapmak istediğiniz işlemi seçiniz: ")
    if işlem == "q":
        print("Programdan çıkış yapıldı...")
        break
    elif işlem == "1":
        dosya.tüm_kelimeler()
    elif işlem == "2":
        dosya.kelime_frekansı()
    elif işlem == "3":
        anahtar = input("Aramak istediğiniz kelimeyi giriniz: ")
        dosya.arama_işlemi(anahtar)
    elif işlem == "4":
        dosya.toplam_kelime()
    elif işlem == "5":
        dosya.alfabetik_sıra()
    else:
        print("Hatalı seçim yaptınız. Tekrar deneyiniz.")
