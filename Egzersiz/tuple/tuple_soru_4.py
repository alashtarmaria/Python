# Soru 4:

# Parametre olarak bir Tuple ve bir index alan bir fonksiyon yazın.
# Fonksiyon, verilen index'te yer alan elemanın tüm Tuple içinde kaç sefer yer aldığını bize dönsün. Adı kac_kere_geciyor olsun.

# İpuçları:
    # count()

# Parametreler:
    # t = (5, 2, 3, 3, 4, 2, 1, 3, 4, 5, 2, 1, 2)
    # i = 1
    # kac_kere_geciyor(t, i)

# Sonuc: 4
# Çözüm 4:

def kac_kere_geciyor(tup, index):
    
    # bu index'teki elemanı bul
    eleman = tup[index]
    
    # Tuple'in count() fonksiyonu var
    # verilen eleman Tuple içinde kaç kere geçtiğini verir
    return tup.count(eleman)

t = (5, 2, 3, 3, 4, 2, 1, 3, 4, 5, 2, 1, 2)
i = 1
adet = kac_kere_geciyor(t, i)
print(adet)
# 4


metin = ('G', 'u', 'i', 'd', 'o', ' ', 'v', 'a', 'n', ' ', 'R', 'o', 's', 's', 'u', 'm')
ind = 4
adet = kac_kere_geciyor(metin, ind)
print(adet)
# 2