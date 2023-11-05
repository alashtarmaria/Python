# Soru 8:

# Parametre olarak bir küme alan bir fonksiyon yazın. Adı kopyala_ve_temizle olsun.

# Fonksiyon parametre olarak gelen kümeyi boşaltsın ama değerlerini yeni bir küme olarak geri dönsün.

# Yani parametre yerinde değişip boş küme olacak ama değerleri ise başka bir küme olarak geri dönecek.

# İpuçları:

# döngü kullanmayın
# copy()
# clear()
# Parametre:
# set1 = {'A', 'B', 'C', 'D', 'E'}

# Sonuç:
# fonksiyon çağırmadan önce set1: {'E', 'C', 'D', 'B', 'A'}
# fonksiyon çağırdıktan sonra set1: set()
# set1_kopyasi: {'D', 'B', 'E', 'A', 'C'}


# Çözüm 8:
def kopyala_ve_temizle(kume):
    
    # orjinal kümeyi boşaltmadan önce -> kopyala
    kopya_kume = kume.copy()
    
    # orjinal küme'yi boşalt
    kume.clear()
    
    # kopyayı geri dön
    return kopya_kume


set1 = {'A', 'B', 'C', 'D', 'E'}
print('fonksiyon çağırmadan önce set1:', set1)

set1_kopyasi = kopyala_ve_temizle(set1)
print('fonksiyon çağırdıktan sonra set1:', set1)
print('set1_kopyasi:', set1_kopyasi)
    