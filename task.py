#Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
#kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."
text = text.upper()
text = text.replace(",", " ")
text = text.replace(".", " ")
print(text)




