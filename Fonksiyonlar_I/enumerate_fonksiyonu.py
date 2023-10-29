# Bazen, for döngüsü ile gezerken, döngünün o andaki indeksine ihtiyaç duyarız.
# Bunun için hazır bulunan enumerate() fonksiyonu kullanılır.


# örnek : 
# kullanıcından metin iste
metin = input("Lütfen bir metin giriniz: ")

yeni_metin = ""

for harf in metin:
    # harfi ve "-" karakterlerini yeni metne ekle
    yeni_metin += harf + "-"
    
print(yeni_metin)


# Örnek:
# Yukarıdaki örnekte, sonda gereksiz bulunan "-" karakterini kaldıralım

# kullanıcından metin iste
metin = input("Lütfen bir metin giriniz: ")

yeni_metin = ""

for index, harf in enumerate(metin):
    
    # harfi yeni metne ekle
    yeni_metin += harf
    
    # son index'e geldiğimizde "-" karakterini istemiyoruz
    if index < len(metin) - 1:
        yeni_metin += "-"
    
print(yeni_metin)


# Örnek:
print(len("pandas"))
# 0, 1, 2, 3, 4, 5

for index, harf in enumerate("pandas"):
    print(index)


# Örnek:
# 10'dan başlayıp 100'e (dahil) kadar 5'er saydığımızı farzedelim.
# Acaba 6. sırada saydığımız sayı kaçtır?

# Önce sayılarımızı görelim

for sayi in range(10, 101, 5):
    print(sayi)

# Altıncı (6.) sıradaki sayı aslında index'i = 5 olan demektir.
# Çünkü index'ler 0'dan başlar.


# kod daha okunur olsun
aralik = range(10, 101, 5)

for index, sayi in enumerate(aralik):
    if index == 5:
        print(sayi)


# tek seferde yazalım
for i, sayi in enumerate(range(10, 101, 5)):
    if i == 5:
        print(sayi)
            

