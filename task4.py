#: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]
def ayristirici(liste1):
    print(liste1)
    a = []
    b = []
    for index, liste in enumerate(liste1):
        if index % 2 == 0:
            a.append(liste)
        else:
            b.append(liste)
    return a, b

print(ayristirici(l))






