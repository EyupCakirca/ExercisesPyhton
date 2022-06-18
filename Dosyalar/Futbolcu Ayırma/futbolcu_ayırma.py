
with open("futbolcular.txt","r",encoding="utf-8") as file:
    galatasaray = []
    beşiktaş = []
    fenerbahçe = []

    for i in file:
        i = i[:-1]
        liste = i.split(",")
        isim = liste[0]
        takım = liste[1]
        if takım == "Galatasaray":
            galatasaray.append(isim + "\n")
        elif takım == "Fenerbahçe":
            fenerbahçe.append(isim + "\n")
        else:
            beşiktaş.append(isim + "\n")

    with open("gs.txt","w",encoding="utf-8") as file2:
        for i in galatasaray:
            file2.write(i)
    with open("fb.txt","w",encoding="utf-8") as file3:
        for i in fenerbahçe:
            file3.write(i)
    with open("bjk.txt","w",encoding="utf-8") as file4:
        for i in beşiktaş:
            file4.write(i)
