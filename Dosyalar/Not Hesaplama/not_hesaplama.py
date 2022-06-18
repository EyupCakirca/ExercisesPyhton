def not_hesaplama(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if son_not >=90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"

    return  isim + "-------->" + harf + "\n"


def geçtiKaldı(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)

    if son_not >= 55:
        return "geçti"
    else:
        return "kaldı"


with open("dosya.txt", "r", encoding ="utf-8") as file:
    eklencekler_listesi = []

    for i in file:
        eklencekler_listesi.append(not_hesaplama(i))

    with open("notlar.txt", "w", encoding ="utf-8") as file2:
        for i in eklencekler_listesi:
            file2.write(i)

with open("dosya.txt", "r", encoding="utf-8") as file:

    geçti = []
    kaldı = []

    for i in file:
        if geçtiKaldı(i) == "geçti":
            geçti.append(i)
        elif geçtiKaldı(i) == "kaldı":
            kaldı.append(i)
        else:
            print("hata")

    with open("geçenler.txt", "w", encoding="utf-8") as file2:
        for i in geçti:
            liste = i.split(",")
            isim = liste[0]
            file2.write(isim + "\n")
    with open("kalanlar.txt", "w", encoding="utf-8") as file3:
        for i in kaldı:
            liste = i.split(",")
            isim = liste[0]
            file3.write(isim + "\n")