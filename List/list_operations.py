# Liste Operasyonları (List Operations)
# List'lerde +, * (artı ve çarpma) gibi işlemler yapabiliriz.
# Ama kendi mantığı içerisinde.

# + Operatörü
# Listeleri uç uca ekler.
a = [10, 20, 30]
b = [4, 8, 12]

c = a + b
print(c)


hafta_ici = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma']
hafta_sonu = ['Cumartesi', 'Pazar']
hafta = hafta_ici + hafta_sonu
print(hafta)


# * Operatörü
# Çarpma (*) Operatörü bir listeyi verilen miktarda tekrarlar.
# (Tüm listeyi bir bütün olarak tekrarlar.)
# Stringler'de çarpma
metin = 'Araba'
print(metin * 5)

print([5] * 3)
print([11, 22] * 4)
print(4 * hafta)
