boy = int(input("Boyunuzu Giriniz(cm.): "))
kilo = int(input("Kilonuzu Giriniz(kg.): "))

y = (boy/100) ** 2
vki = (kilo / y)


print("Vücut Kitle Endeksiniz: {}".format(round(vki,2)))

