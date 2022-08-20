#Verilen sözlük yapısına aşağıdaki adımları uygulayınız
#Adım 1: Key değerlerine erişiniz.
#Adım 2: Value'lara erişiniz.
#Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
#Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
#Adım 5: Antonio'yu dictionary'den siliniz.
dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}
print(dict.keys())
print(dict.values())
dict['Daisy']= ["England", 13]
print(dict)
dict["Ahmet"] = "Turkey", 24
print(dict)
dict.pop("Antonio")
print(dict)


