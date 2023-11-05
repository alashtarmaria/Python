# Soru 3:
# Parametre olarak iki Set alan bir fonksiyon yazın. Adı ayni_elemenlar olsun.
# Fonksiyon bu iki küme içindeki ortak elemanları (kesişim kümesini) bir liste olarak dönsün.
# Bu listenin elemanları küçükten büyüğe sıralı dönsün.

# İpuçları:
# döngü kullanmayın
# intersection()
# sorted()
# Parametre:
# set_1 = {10, 20, 30, 40, 50, 60}
# set_2 = {20, 40, 60, 80, 90, 100}

# Sonuç:
# [20, 40, 60]


# Çözüm 3:
# Çözüm 3:
# Çözüm 3:

def ayni_elemanlar(kume_1, kume_2):
    
    # iki kümenin kesişim kümesi -> intersection
    kesisim = kume_1.intersection(kume_2)
    
    # şimdi kesişim'i sırala -> sorted()
    # sorted() parametre olarak set alır ama geriye liste döner
    kesisim = sorted(kesisim)
    
    return kesisim
    
    
set_1 = {10, 20, 30, 40, 50, 60}
set_2 = {20, 40, 60, 80, 90, 100}
kesisim = ayni_elemanlar(set_1, set_2)
print(kesisim)   


