# Soru 7:

# Parametre olarak iki küme alan bir fonksiyon yazın. Adı tamamen_farkli_mi_2 olsun.

# Fonksiyon bu iki küme arasında hiç ortak eleman olup olamadığını kontrol etsin:

# Eğer hiç ortak eleman yoksa, şöyle dönsün -> "Bu iki Küme tamamen farklı"
# Eğer en az bir elemanları ortaksa, şöyle dönsün -> "Bu iki Kümenin ortak elemanları var:"
# ve ortak eleman kümesini beraber dönsün
# Fonksiyon ayrıca parametre olarak gelen iki kümenin gerçekten Set tipinde olup olmadığını kontrol da etsin. Eğer herhangi biri Set tipinde değilse, "Parametreler Set tipinde değil" hatası fırlatsın.

# İpuçları:

# döngü kullanmayın
# tamamen farklı için: isdisjoint()
# isinstance()
# raise Exception()

# Parametre:
# set_1 = {20, 10, 40, 30, 50}
# set_2 = {60, 80, 70, 100, 90}
# Sonuç:
# 'Bu iki Küme tamamen farklı'

# ----------------------------------------
# Parametre:
# set_1 = {20, 10, 40, 30, 50, 60}
# set_2 = {60, 80, 70, 90, 40, 10}
# Sonuç:
# 'Bu iki Kümenin ortak elemanları var: {40, 10, 60}'


# Çözüm 7:

def tamamen_farkli_mi_2(set1, set2):
    
    # önce ikisinin de set olduğunu kontrol et
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise Exception('Parametreler Set tipinde değil.')
    else:
        
        # tamamen farklı mı?
        if set1.isdisjoint(set2):
            return 'Bu iki Küme tamamen farklı.'
        else:
            return 'Bu iki Kümenin ortak elemanları var:' + str(set1.intersection(set2))

set_1 = {20, 10, 40, 30, 50}
set_2 = {60, 80, 70, 100, 90}
print(tamamen_farkli_mi_2(set_1, set_2))

set_1 = {20, 10, 40, 30, 50, 60}
set_2 = {60, 80, 70, 90, 40, 10}
print(tamamen_farkli_mi_2(set_1, set_2))