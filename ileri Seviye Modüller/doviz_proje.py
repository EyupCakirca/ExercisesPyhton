import requests
from bs4 import BeautifulSoup
import time

url = "https://www.doviz.com/"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

name = soup.find_all("span", {"class": "name"})
value = soup.find_all("span", {"class": "value"})

sözlük = {}
for i, j in zip(name, value):
    i = i.text
    j = j.text
    j = j.replace(".", "")
    j = j.replace(",", ".")
    sözlük[i] = j
    print(i, j)
print("""
********************************
Döviz Çevirme Programı
********************************
1. TL den Yabancı Para Birimine Çevir
2. Yabancı Para Biriminden TL ye Çevir.
Çıkış içi 'q' basınız.
********************************""")
while True:
    işlem = input("Hangi işlemi yapmak istiyorsunuz?:")
    if işlem == "q":
        print("Programdan çıkış yapılıyor...")
        time.sleep(2)
        print("Çıkış yapıldı.")
        break

    elif işlem == "1":
        try:
            para_birimi = input("Para birimini giriniz:")
            değer = float(input("Miktarı giriniz:"))
            print("{} TL ==> {} {}".format(değer, değer / float(sözlük[para_birimi]), para_birimi))
        except KeyError:
            print("Hatalı para birimi seçtiniz. Tekrar deneyiniz")
        except ValueError:
            print("Sadece sayı giriniz. Tekrar deneyiniz")

    elif işlem == "2":
        try:
            para_birimi = input("Para birimini giriniz:")
            değer = float(input("Miktarı giriniz:"))
            print("{} {} ==> {} TL".format(değer, para_birimi, float(sözlük[para_birimi]) * değer))
        except KeyError:
            print("Hatalı para birimi seçtiniz. Tekrar deneyiniz")
        except ValueError:
            print("Sadece sayı giriniz. Tekrar deneyiniz.")

    else:
        print("Geçersiz bir seçim yaptınız. Tekrar deneyiniz.")
