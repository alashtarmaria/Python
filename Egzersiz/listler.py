# Soru 1:
# Parametre olarak bir liste alan bir fonksiyon yazın. Adı toplam olsun.
# Bu fonksiyon kendisine verilen listenin tüm elemanlarını toplasın ve geriye genel toplam dönsün.
# Örnek:
    # liste = [1, 2, 3, 4, 5] 
    # toplam(liste) -> 15

# Çözüm 1:
def toplam(liste):
    
    # toplam değişkeni
    toplam = 0
    
    for i in liste:
        toplam += i
        
    return toplam
    

liste = [1, 2, 3, 4, 5] 
genel_toplam = toplam(liste)
print(genel_toplam)    
# 15

liste = [10, 20, 30, 40, 500] 
genel_toplam = toplam(liste)
print(genel_toplam)
# 600
