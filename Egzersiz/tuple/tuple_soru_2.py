# Soru 2:

# Parametre olarak verilen bir Tuple'ı String'e dönüştüren ve bu String'i geri dönen bir fonksiyon yazın.
# Adı tuple_to_string olsun.

# İpuçları:
    # join()
    # Parametre:
    # t = ('Y', 'a', 'p', 'a', 'y', ' ', 'Z', 'e', 'k', 'a')

# Sonuc: Yapay Zeka
# Çözüm 2:
def tuple_to_string(tup):
    return  "".join(tup)

t = ('Y', 'a', 'p', 'a', 'y', ' ', 'Z', 'e', 'k', 'a')

t = tuple_to_string(t)

print(t)