
# Soru 10:

# Parametre olarak içinde listeler olan, iki seviyeli bir liste alan fonksiyon yazın. Adı listeyi_duzlestir olsun.

# Fonksiyon listenin altındaki tüm listleri düzleştirip, geriye tek seviyeli bir liste dönsün.

# İpuçları:

# döngü kullanmayın
# comprehension ile yapın
# Parametre:
# listeler_listesi = [[8,6], [3,1,4], [2,0,9], [5]]
          
# Sonuc:
# [8, 6, 3, 1, 4, 2, 0, 9, 5]

# Çözüm 10:

def listeyi_duzlestir(liste):
    
    return [j
            for i in liste
            for j in i]

listeler = [[8,6], [3,1,4], [2,0,9], [5]]

duz_liste = listeyi_duzlestir(listeler)
print(duz_liste)