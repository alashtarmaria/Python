# Soru 8:

# Verilen bir dictionary içindeki tek index'li elemanları silip geriye sadece çift index'li elemanların olduğu yeni bir dictionary dönen bir fonksiyon yazın.

# Fonksiyonun adı tekleri_sil olsun.

# İpuçları:

# Parametre olarak gelen orijinal dictionary'ye dokunmayın.
# döngü için items()
# index için enumerate()
# Parametre sözlük:
# sozluk = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F'}

# Sonuç:
# {'a': 'A', 'c': 'C', 'e': 'E'}

# Çözüm 8:
# 1. Yol
def tekleri_sil(sozluk):
    
    d = {}
    
    for index, item in enumerate(sozluk.items()):
        
        key = item[0]
        value = item[1]
        
        if index % 2 == 0:
            d[key] = value
            
    return d

sozluk = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F'}
ciftler = tekleri_sil(sozluk)
print(ciftler)



# 2. Yol
def tekleri_sil(sozluk):
    
    d = {}
    
    for index, item in enumerate(sozluk.items()):        
        if index % 2 == 0:
            d.update({item})
            # print(item)
            
    return d


sozluk = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F'}
ciftler = tekleri_sil(sozluk)
print(ciftler)
