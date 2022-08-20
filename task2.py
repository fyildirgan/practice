#Verilen listeye aşağıdaki adımları uygulayınız.
#Adım 1: Verilen listenin eleman sayısına bakınız.
#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
#Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
#Adım 4: Sekizinci indeksteki elemanı siliniz.
#Adım 5: Yeni bir eleman ekleyiniz.
#Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
print(len(lst))
print(lst[0], lst[10])
print(lst[0:4])
lst.pop(8)
print(lst)
lst.append(100)
print(lst)
lst.insert(8, "N")
print(lst)

