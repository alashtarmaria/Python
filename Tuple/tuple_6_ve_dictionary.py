# Dictionary'ler ve Tuple'lar

# Daha önce Dictionary bölümünde görmüştük; Dictionary'nin elemanlarını almak için items() fonksiyonu kullanılır.
# İşte bu items() fonksiyonu biz bir Tuple listesi döner.

# ilk 3 harfi ve onların ASCII kodlarını tutan bir sözlük
sozluk = {
    'A': ord('A'),
    'B': ord('B'),
    'C': ord('C'),
    'a': ord('a'),
    'b': ord('b'),
    'c': ord('c')
}

print(sozluk)
# {'A': 65, 'B': 66, 'C': 67, 'a': 97, 'b': 98, 'c': 99}


# items()
print(sozluk.items())
#  dict_items([('A', 65), ('B', 66), ('C', 67), ('a', 97), ('b', 98), ('c', 99)])


# Şimdi dict_items üzerine döngü kuralım
for key, value in sozluk.items():
    print(key, value)

# A 65
# B 66
# C 67
# a 97
# b 98
# c 99    
    


# Hatırlatma: Her ne kadar yukarıda elemanlar sıralı gelmiş ve sanki Dictionary'de sıralı duruyorlamış gibi gelse de, bu doğru değildir. 
# Dictionary içinde elemanların sıralı olmasını beklemeyin. Yapısı gereği, index tutmadığı için sıra beklemek yanlış olur.

# Bir Tuple Listesini Dictionary Yapmak:
# Az önce bir dictionary'nin elemanlarını items() ile alınca, bize içinde Tuple'lar olan bir List verdiğini gördük.
# Şimdi aynı işlemi tersten yapalım:
# İçinde Tuple'lar olan bir List'i, Dictionary'ye çevirelim:
aylar_gunler = [
    ('Ocak', 31),
    ('Şubat', 28),
    ('Mart', 31),
    ('Nisan', 30)
]

print(aylar_gunler)
#[('Ocak', 31), ('Şubat', 28), ('Mart', 31), ('Nisan', 30)]

aylar = dict(aylar_gunler)
print(aylar)
print(type(aylar))
# {'Ocak': 31, 'Şubat': 28, 'Mart': 31, 'Nisan': 30}
# <class 'dict'>



# Tuple'i Dictionary'ye Key Yapmak:

# Daha önce, Dictionary bölümünde şunu demiştik:

# Bir Dictionary'nin key'i Immutable olmak zorunda. Yani Immutable (Değiştirilemez) tipler sadece key olabilir.

# İşte Tuple'lar Immutable oldukları için, Dictionary'e key olmak için kullanılabilirler.

# Örnek:
# Diyelim ki bir sınıftaki öğrencilerin notlarını bir Dictionary içinde tutmak istiyorunuz.
# Öğrencilerin bilgileri Adlar, Soyadlar ve Dereceler ayrı listeler olarak tutuluyor olsun.
# Şu şekilde bir sözlük kuracağız:

# ogrenci_durumu = {
#     ('Musa', 'Arda'): 'AA', 
#     ('Bruce', 'Wayne'): 'DC', 
#     ('Klark', 'Kent'): 'FF', 
#     ('Peter', 'Parker'): 'FD'
# }


# Çözüm:

# sıralı listelerimiz
adlar = ['Musa', 'Bruce', 'Klark', 'Peter']
soyadlar = ['Arda', 'Wayne', 'Kent', 'Parker']
dereceler = ['AA', 'DC', 'FF', 'FD']

# boş dictionary
ogrenci_durumu = {}

# 3 listeyi de zip ile birleştirelim
for ad, soyad, derece in zip(adlar, soyadlar, dereceler):
    ogrenci_durumu[(ad, soyad)] = derece

print(ogrenci_durumu)
