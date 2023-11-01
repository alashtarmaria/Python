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


# Soru 2:
# Parametre olarak, iç içe bir liste (nested list) alan bir fonksiyon yazın. İsmi iki_seviye_toplam olsun. Bu iç içe liste parametresi 2 seviyeli olsun.
# Fonksiyon bu iç içe listenin tüm iç elemanları da dahil olmak üzere, genel toplam hesaplasın ve dönsün.

# Örnek:
# liste = [[5, 8], [1, 4, 7], [10], 3]
# iki_seviye_toplam(liste) -> 38
# Çözüm 2:

def iki_seviye_toplam(dizi):
    
    toplam = 0
    
    for eleman in dizi:
        
        # tip kontrolü -> list ise 
        if type(eleman) == list:
            for ic_eleman in eleman:            
                toplam += ic_eleman
        elif str(eleman).isdigit():
            toplam += eleman
            
    return toplam
liste = [[5, 8], [1, 4, 7], [10], 3]

toplam = iki_seviye_toplam(liste)

print(toplam)    
# 38


# Soru 3:
# Soru 2'de yazdığımız fonksiyon sadece 2 seviyeli iç içe liste alabiliyordu. Şimdi bunu jenerik bir hale getirelim ve her seviye iç içe listeyi toplayabilsin. İsmi ic_ice_toplam olsun.
# Fonksiyon bu iç içe listenin tüm iç elemanları da dahil olmak üzere, genel toplam hesaplasın ve dönsün.
# Örnek:
# liste = [[5, 8], [1, 4, 7, [8, 2]], [10, [-1, 2]], 3]
# ic_ice_toplam(liste) -> 49
# İpucu: Recursive
# Çözüm 3:

def ic_ice_toplam(dizi):
    
    toplam = 0
    
    for eleman in dizi:
        
        if type(eleman) == int:
            toplam += eleman
            
        elif type(eleman) == list:
            
            # eğer eleman list ise, onun elemanları içinde döneceğiz
            # recursion
            
            toplam += ic_ice_toplam(eleman)
            
    return toplam

liste = [[5, 8], [1, 4, 7, [8, 2]], [10, [-1, 2]], 3]

toplam = ic_ice_toplam(liste)

print(toplam)
# 49


# Soru 4:
# Parametre olarak bir liste alan bir fonksiyon yazınız. Adı kareler olsun.
# Fonksiyonumuz listedeki her bir elemanın karesini hesaplayacak ve yeni bir listeye ekleyecek. Sonuçta bu yeni listeyi dönecek. Yani parametre olarak gelen listedeki, elemanların karesini tutan yeni bir liste verecek.
# Örnek:
# dizi = [1,2,3,4,5]
# kareler(dizi) -> [1, 4, 9, 16, 25]
# Çözüm 4:

def kareler(liste):
    
    # yeni listeyi tutan bir değişken
    #yeni_liste = []
    yeni_liste = list()
    
    for i, eleman in enumerate(liste):
        yeni_liste.append(eleman**2)
        
    return yeni_liste


dizi = [1,2,3,4,5]

sonuc = kareler(dizi)

print(sonuc)
# [1, 4, 9, 16, 25]