print("""
**********************************
Şifreniz en az 1 büyük harf, 1 küçük harf, 1 özel karakter ve 1 sayı içermelidir.
Şifreniz 8-12 karakter aralığında olmalıdır.
**********************************""")
büyük_harf = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZQWX"
küçük_harf = "abcçdefgğhıijklmnoöprsştuüvyzqwx"
özel_karakter = ".,!*?+-*/-_=)(&%@"
sayılar = "0123456789"

def şifre_kontrolü(şifre):
    sayaç_büyük_harf = 0
    sayaç_küçük_harf = 0
    sayaç_özel_harf = 0
    sayaç_sayı = 0
    uzunluk = len(şifre)

    for harf in şifre:
        if harf in büyük_harf:
            sayaç_büyük_harf += 1
        if harf in küçük_harf:
            sayaç_küçük_harf += 1
        if harf in özel_karakter:
            sayaç_özel_harf += 1
        if harf in sayılar:
            sayaç_sayı += 1
    if sayaç_büyük_harf >= 1 and sayaç_küçük_harf >= 1 and sayaç_özel_harf >= 1 and sayaç_sayı >= 1 and 8 <= uzunluk <= 12 :
        return True

while True:
    şifre = input("Şifrenizi giriniz: ")
    if şifre_kontrolü(şifre):
        print("Bararıyla kaydedildi.")
        break
    else:
        print("Hatalı şifre belirlediniz. Tekrar deneyiniz.")


