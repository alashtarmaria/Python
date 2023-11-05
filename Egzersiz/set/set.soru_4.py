# Soru 4:

# Parametre olarak iki Set alan bir fonksiyon yazın. Adı tum_elemanlar olsun.

# Fonksiyon bu iki küme içindeki tüm elemanları (birleşim kümesi) bir liste olarak versin.

# Bu listede aynı olan elemanlar sadece bir kere geçmek zorunda.

# Bu liste büyükten küçüğe sıralı olmak zorunda.

# İpuçları:

# döngü kullanmayın
# unioun()
# sort()
# Parametre:
# set_1 = {10, 20, 30, 40, 50, 60}
# set_2 = {20, 40, 60, 80, 90, 100}

# Sonuç:
# [100, 90, 80, 60, 50, 40, 30, 20, 10]

# Çözüm 4:

def tum_elemanlar(s1, s2):
    
    birlesim = s1.union(s2)
    
    # sort() -> için liste olmak zorunda
    birlesim = list(birlesim)
    
    # sort yap -> tersten sırala
    birlesim.sort(reverse=True)
    
    return birlesim
    

set_1 = {10, 20, 30, 40, 50, 60}
set_2 = {20, 40, 60, 80, 90, 100}
birlesim = tum_elemanlar(set_1, set_2)
print(birlesim)    