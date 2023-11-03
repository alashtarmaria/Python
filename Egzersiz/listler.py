# Soru 1:
# Parametre olarak bir liste alan bir fonksiyon yazın. Adı toplam_fark olsun.
# Bu fonksiyon kendisine verilen listenin tüm elemanlarını toplasın ve geriye genel toplam dönsün.
# Örnek:
    # liste = [1, 2, 3, 4, 5] 
    # toplam(liste) -> 15

# Çözüm 1:
def toplam_fark(liste):
    
    # toplam değişkeni
    toplam = 0
    
    for i in liste:
        toplam += i
        
    return toplam
    

liste = [1, 2, 3, 4, 5] 
genel_toplam = toplam_fark(liste)
print(genel_toplam)    
# 15

liste = [10, 20, 30, 40, 500] 
genel_toplam = toplam_fark(liste)
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

# 2.yol 
# Çözüm 2:

def iki_seviye_toplam(liste):
    toplam = 0
    
    for eleman in liste :
        if type(eleman) == str:
            continue
        elif type(eleman) == list:
            for ic_eleman in eleman :
                toplam += ic_eleman 
        
        elif str(eleman).isdigit() :
            toplam += eleman
            
    return toplam   
 

liste = [[5, 8], [1, 4, 7], [10], 3, 10,'a']
toplam = iki_seviye_toplam(liste)
print(toplam)  
# 48


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


# Soru 5:
# Parametre olarak bir liste alan bir fonksiyon yazınız. Adı kareler_toplami olsun.
# Fonksiyonumuz listenin başından başlarak elemanların karelerini alacak. Bu kareleri toplayarak yeni bir liste oluşturacak. Oluşan yeni listenin her bir elemanı, parametre olan gelen listedeki o index'e kadar olan kareler toplamı olacak.
# Yani, yeni listedeki 4. eleman, gelen listedeki 1-2-3-4. elemanların kareleri toplamı olacak.
# Böylece sona kadar gidecek. Ve bu şekilde oluşan yeni listeyi dönecek.
# Örnek:
# dizi = [1,2,3,4,5] 
# kareler_toplami(dizi) -> [1, 5, 15, 37, 83]
# İpucu:

# Soru 1'de yazdığınız toplam fonksiyonunu kullanabilirsiniz
# Çözüm 5:
def kareler_toplami(liste):
    
    yeni_liste = []
    
    for eleman in liste:
        
        # yeni_listedeki elemanların toplamını 
        yeni_liste_toplami = toplam_fark(yeni_liste)
        
        # şimdi mevcut eleman'ın karesini de ekleyelim
        yeni_toplam = yeni_liste_toplami + eleman**2
        
        # şimdi bu yeni_toplami yeni_liste'ye ekle
        yeni_liste.append(yeni_toplam)
        
    return yeni_liste

liste = [1,2,3]
sonuc = kareler_toplami(liste)
print(sonuc)
# [1 ,5 , 15]


# Soru 6:
# Listenin tek index'leri (1,3,5...) toplamı ile çift index'leri (0,2,4...) toplamı arasındaki farkı veren bir fonksiyon yazınız.
# Adı tek_cift_index_farki olsun.
     # liste = [1,2,3,4,5,6]
     # Tekler index'ler toplamı = 2 + 4 + 6 = 12
     # Çift index'ler toplamı = 1 + 3 + 5 = 9
     # tek_cift_index_farki(liste) -> 12 - 9 = 3
# İpucu:
     # index sıfırdan başlar
     # sadece listeler ve index'leri kullanınız.
     # Bu fonksiyon içinde döngü kullanmayınız.
     # Soru 1'deki toplam() fonksiyonunu kullanınız.

# Çözüm 6:
def tek_cift_index_farki(dizi):
    
    # tekler listesi
    tekler = dizi[1::2]
    
    # tekler toplamı
    tekler_toplami = toplam_fark(tekler)
    
    # çiftler listesi
    ciftler = dizi[::2]
    
    # çiftler toplamı
    ciftler_toplami = toplam_fark(ciftler)
    
    # farkı bul
    fark = tekler_toplami - ciftler_toplami
    
    return fark

liste = [1,2,3,4,5,6]
fark = tek_cift_index_farki(liste)
print(fark)
# 3

# Soru 7:
# Parametre olarak kendisine verilen listeyi kırpan bir fonksiyon yazın. Kırpma işlemi dizinin ilk ve son elemanını silmek demektir.
# Fonksiyonumuzun adı kirpan olsun ve kendisine verilen parametreyi yerinde değiştirsin. Yani dışarıdaki orijinal listeyi modifiye etsin. Geriye hiçbir değer dönmesin. (None)        
# Fonksiyonu şu şekilde test ediniz ve dizinin yerinde değiştiğini ispatlayınız:
        # dizi = [1,2,3,4,5,6,7]
        # print('kirpan fonksiyon öncesi dizi:', dizi)
        # kirpan(dizi)

# Çözüm 7:
def kirpan(liste):
    
    # ilk elemanı sil
    liste.pop(0)
    
    # son elemanı sil -> pop() direk son elemanı siler
    liste.pop()

#2.yol 
# Çözüm 7:
# def kirpan(liste):
#     del liste[0]
#     del liste[-1]

dizi = [1,2,3,4,5,6,7]
print('kirpan fonksiyon öncesi dizi:', dizi)
kirpan(dizi)
print('kirpan fonksiyon sonrası dizi:', dizi)
# kirpan fonksiyon öncesi dizi: [1, 2, 3, 4, 5, 6, 7]
# kirpan fonksiyon sonrası dizi: [2, 3, 4, 5, 6]



# Soru 8:
# Parametre olarak bir liste bir de sıralama tipi isteyen bir fonksiyon yazın. Adı sirala olsun.
# Sırala Fonksiyonu, liste ile beraber tipi boolean olan azalan_mi adında bir parametre alacak. Bu parametresnin default değeri False olacak.
# Eğer azalan_mi parametresi True ise, fonksiyon listeyi büyükten küçüğe sıralayacak,
# Eğer azalan_mi parametresi False ise, fonksiyon listeyi küçükten büyüğe sıralayacak
# Sonunda sıralanmış listeyi geri dönecek.
# Notlar:
#      Sıralama işlemi için Python List yapısının standart fonksiyonlarını kullanın
#      Döngü kullanmayın
#      Fonksiyon orijinal listeyi değiştirmesin

# Çözüm 8:

# Birinci yol
def sirala(liste, azalan_mi = False):
    
    sirali_liste = []
    
    # azalan_mi değerine bal
    if azalan_mi:
        sirali_liste = sorted(liste, reverse=True)
    else:
        sirali_liste = sorted(liste)
        
    return sirali_liste

# İkinci yol

def sirala(liste, azalan_mi=False):
    
    return sorted(liste, reverse=azalan_mi)
    

a = [12, 4, 2, 1, 6, 3, 45]
print('a:', a)

sirali = sirala(a, False)
print('sirali - artan', sirali)

sirali = sirala(a, True)
print('sirali - azalan', sirali)

print('sirala sonrası a:', a)
# a: [12, 4, 2, 1, 6, 3, 45]
# sirali - artan [1, 2, 3, 4, 6, 12, 45]
# sirali - azalan [45, 12, 6, 4, 3, 2, 1]
# sirala sonrası a: [12, 4, 2, 1, 6, 3, 45]


# Soru 10:
# Verilen bir listenin büyükten küçüğe sıralı olup olmadığını kontrol eden bir fonksiyon yazın.
# Adı azalan_sirali_mi olsun, ve eğer liste büyükten küçüğe sıralı ise True, değilse False dönsün.
# Yapılacaklar:
# 4 farklı yolla çözünüz bu soruyu


# Çözüm 10:

# Yol 1:
# İç İçe Döngüler
# En az Pythonic

def azalan_sirali_mi(liste):
    
    # döngü 1
    for i, eleman_1 in enumerate(liste):
        
        # döngü 2
        for j, eleman_2 in enumerate(liste):
            if j > i:
                if eleman_2 > eleman_1:
                    return False
                
    return True

dizi = [2, 7, 3, 4]
print(azalan_sirali_mi(dizi))
# False

dizi = [2, 3, 4, 7]
print(azalan_sirali_mi(dizi))
# False

dizi = [7, 4, 3, 2]
print(azalan_sirali_mi(dizi))
# True

dizi = [7, 7, 4, 3, 2, 1, 1]
print(azalan_sirali_mi(dizi))
# True

dizi = ['a', 'd', 'b', 'c']
print(azalan_sirali_mi(dizi))
# False

dizi = ['a', 'b', 'c', 'd']
print(azalan_sirali_mi(dizi))
# False

dizi = ['d', 'c', 'b', 'a']
print(azalan_sirali_mi(dizi))
# True


# Çözüm 10:
# Yol 2:
# İkili Fark kontrolü
# Biraz daha Pythonic

def azalan_sirali_mi_2(liste):
    
    # baştan sona kadar git
    # her elemanı kendisinden sonraki ile karşılaştır
    # eğer fark negatif ise, o zaman azalmıyordur
    for i in range(len(liste) - 1):
        
        if liste[i] - liste[i+1] < 0:
            return False
    
    return True

dizi = [7, 4, 3, 2]
print(azalan_sirali_mi_2(dizi))
# Çözüm 10:

# Yol 3:
# Sıralı liste ile kontrol
# Pythonic

def azalan_sirali_mi_3(liste):
    
    # yeni bir liste yarat
    sirali_liste = liste[::]
    
    # sirali listeyi büyükten küçüğe sırala
    sirali_liste.sort(reverse=True)
    
    # şimdi sırali_liste ile liste eşit mi
    if liste == sirali_liste:
        return True
    else:
        return False

dizi = [2, 7, 3, 4]
print(azalan_sirali_mi_3(dizi))


# Çözüm 10:
# Yol 4:
# direk kontrol
# Pythonic ve Functional

def azalan_sirali_mi_4(liste):
    
    # direk yeni liste ile liste aynı mı ?
    return sorted(liste, reverse=True) == liste

dizi = [2, 7, 3, 4]
print(azalan_sirali_mi_4(dizi))