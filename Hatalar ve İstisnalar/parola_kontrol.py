def parola_kontrol(parola):
    tr_karakter = "ığüİşöç"
    rakam = "1234567890"

    for i in parola:
        if i in tr_karakter:
            raise TypeError("Türkçe karakter kullanılamaz.")
        if i in rakam:
            raise TypeError("Rakam kullanılamaz.")
        else:
            pass
    if len(parola) == 0:
        raise AssertionError("parola bölümü boş bırakılamaz.")
    print("Parola kaydedildi.")

print("""
********************************************

Parola Kontrol Programı

********************************************""")

parola = input("Parola giriniz: ")
parola_kontrol(parola)

