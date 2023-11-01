# id yöntemi

# Python'da tüm nesneler bir id ile tutulur.
# Nesnenin bellekteki adresi.
# Id değeri -> id() fonksiyonu ile bulunur.
 #   id(x) == id(y) kontrolü -> aynılık (identical) -> nesneler

liste = ['a', 'b', 'c', 'd', 'e', 'f']
yeni_liste = liste[:]
baska_liste = liste[:]
print("liste:", liste)
print("yeni_liste:", yeni_liste)
print("baska_liste:", baska_liste)
# liste değişkeninin id'sini alalım
print(id(liste))


# yeni_liste'nin id'si
print(id(yeni_liste))


# baska_liste'nin id'si
print(id(baska_liste))

