# Soru 5:

# Paramere olarak iki liste bir fonksiyon yazın. Fonksiyonun adı farki_ver olsun.

# Fonksiyon bu iki liste arasındaki farklı elemanları bir Set olarak dönsün.

# Yani birinci listede olup ikinci listede olmayan elemanları.

# İpuçları:

# döngü kullanmayın
# set()
# difference()
# Parametre:
# l_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l_2 = [2, 4, 6, 8]

# Sonuç:
# {1, 3, 5, 7, 9}

# Çözüm 5:
def farki_ver(liste_1, liste_2):
    
    # list'leri set'e çevir
    set_1 = set(liste_1)
    set_2 = set(liste_2)
    
    # fark -> difference (set'ler üzerinde çalışır)
    fark = set_1.difference(set_2)
    
    return fark


l_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l_2 = [2, 4, 6, 8]

farklar = farki_ver(l_1, l_2)
print(farklar)
    