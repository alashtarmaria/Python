# Soru 7:

# Parametre olarak bir liste alan bir fonksiyon yazın. Fonksiyonun adı, tuple_karesi_ile_degistir olsun.
# Bu listenin elemanları birer Tuple olsun.
# Her bir tuple farklı uzunlukta olabilir. Dolayısı ile Listenin elemanlarının uzunlukları sabit değil.
# Yazacağınız fonksiyon, Liste içindeki her bir Tuple elamanının tüm elemanlarının yerine karelerini yazsın.

# Ve yeni kareli listeyi geri dönsün.

# İpuçları:

# Parametre olarak gelen orjinal liste değişmesin
# Listenin içinde for ile dönerken, döngüdeki elemanı değiştirseniz de liste değişmez.
# Parametre:
# tuple_listesi = [(2,5,8), (4,3), (1,7,9,6), (5,)]

# Sonuc:
# yeni_tuple_listesi = [(4,25,64), (16,9), (1,49,81,36), (25,)]

# Çözüm 7:

def tuple_karesi_ile_degistir(liste):
    
    # orjinal listeyi değiştirme -> kopyala
    yeni_liste = liste.copy()
    
    for index, tup in enumerate(yeni_liste):
        
        yeni_tup = tuple()
        
        # tup'un elemanları üzerinde gez
        for t in tup:
            yeni_tup += (t**2,)
            
        # şimdi yeniden atanmış yeni_tup -> listeye geri ekle

        yeni_liste[index] = yeni_tup
        
    return yeni_liste        
        

tuple_listesi = [(2,5,8), (4,3), (1,7,9,6), (5,)]

yeni_tuple_listesi = tuple_karesi_ile_degistir(tuple_listesi)

print('tuple_listesi:', tuple_listesi)
print('yeni_tuple_listesi:', yeni_tuple_listesi)        

# tuple_listesi: [(2, 5, 8), (4, 3), (1, 7, 9, 6), (5,)]
# yeni_tuple_listesi: [(4, 25, 64), (16, 9), (1, 49, 81, 36), (25,)]