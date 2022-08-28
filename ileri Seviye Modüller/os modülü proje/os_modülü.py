import os

dosyalar = os.walk("C:\ZZ DEPO")
resimler = list()
müzikler = list()
vidyolar = list()
pdfler = list()
for klasör_yolu,klasör_isimleri,dosya_isimleri in dosyalar:
    for dosya in dosya_isimleri:
        if dosya.endswith(".jpeg"):
            resimler.append(os.sep.join([klasör_yolu,dosya]))
        elif dosya.endswith(".mp4"):
            vidyolar.append(os.sep.join([klasör_yolu,dosya]))
        elif dosya.endswith(".pdf"):
            pdfler.append(os.sep.join([klasör_yolu,dosya]))
        elif dosya.endswith(".mp3"):
            müzikler.append(os.sep.join([klasör_yolu,dosya]))

with open("pdf_dosyaları.txt","w",encoding = "utf-8") as file:
    for i in pdfler:
        file.write(i + "\n")
with open("jpeg_dosyaları.txt","w",encoding="utf-8") as file1:
    for i in resimler:
        file1.write(i + "\n")
with open("mp3_dosyaları.txt","w",encoding="utf-8") as file2:
    for i in müzikler:
        file2.write(i + "\n")
with open("mp4_dosyaları.txt","w",encoding="utf-8") as file3:
    for i in vidyolar:
        file3.write(i + "\n")