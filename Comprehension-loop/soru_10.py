
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

def listeyi_duzlestir_1(liste):
    
    return [ic_eleman
          for eleman in liste
          for ic_eleman in eleman]

listeler = [[8,6], [3,1,4], [2,0,9], [5]]

duz_liste = listeyi_duzlestir_1(listeler)
print(duz_liste)

# Çözüm 10 2.yol:
def listeyi_duzlestir_2(liste):
    
    yeni_liste = []
    
    for eleman in liste :
        for ic_eleman in eleman :
            yeni_liste.append(ic_eleman)
            
    return yeni_liste        
    
    
listeler = [[8,6], [3,1,4], [2,0,9], [5]]

duz_liste = listeyi_duzlestir_2(listeler)

print(duz_liste)
