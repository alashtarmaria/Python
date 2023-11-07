# Soru 1:

# Önce for dögüsü ile 1 den 10'a (hariç) kadar olan sayıların karelerini veren bir fonksiyon yazın. Adı kareleri_ver olsun.
# Ardından aynı fonksiyonu comprehension ile yazın. Adı kareleri_ver_comp olsun.
# [1, 4, 9, 16, 25, 36, 49, 64, 81]


# Çözüm 1:

# for döngüsü
def kareleri_ver():
    
    kareler = []
    
    for i in range(1, 10):
        kareler.append(i**2)

    return kareler

kareler = kareleri_ver()
print(kareler)


# comprehension

def kareleri_ver_comp():
    
    kareler = [x**2 for x in range(1, 10)]
    
    return kareler

kareler = kareleri_ver_comp()
print(kareler)