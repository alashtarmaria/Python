#Liste Dilimleme (Slicing)

#  2. eleman ile 5. eleman arasını alalım
# index = 1 den -> index = 4'e demek
liste = ['a', 'b', 'c', 'd', 'e', 'f']
print(liste[1:4])


# ilk 4 elemanı alalım
# 0, 1, 2, 3
liste[0:4]
print(liste[:4])


# listenin tüm elemanlarını yaz
# başlanguç -> 0 (default)
# bitiş -> sona kadar (default)
# liste[<bas> : <biti>]
print(liste[:])


# Liste Kopyalama:
# Kopayalamak -> Yeni bir liste almak demektir.

yeni_liste = liste[:]
print(yeni_liste)


baska_liste = liste[:]
print(baska_liste)

# Şimdi gerçekten 3 ayrı listemiz var mı, görelim:
# liste'nin 1. ve 2. elemanlarını değiştir
# index = 1 ve 2

print("liste:", liste)
print("yeni_liste:", yeni_liste)
print("baska_liste:", baska_liste)


# index = 1 ve 2
liste[1:3] = [10, 20]
print(liste)

print("liste:", liste)
print("yeni_liste:", yeni_liste)
print("baska_liste:", baska_liste)


yeni_liste[0] = 'AA'
print("liste:", liste)
print("yeni_liste:", yeni_liste)
print("baska_liste:", baska_liste)