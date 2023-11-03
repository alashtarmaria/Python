# İkinci yol
# True Gaussian Yol

def gauss_2(baslangic=1, bitis=100, artis=2):
    
    # önce list oluştur
    liste = list(range(baslangic, bitis, artis))
    
    toplam = 0
    
    for i in range(len(liste)):
        
        ikili_toplam = liste[i] + liste[-i-1]
        
        toplam += ikili_toplam
        
    return toplam / 2

# index mabtığını hatırlayalım 
liste = list(range(1, 10, 1))
print(liste[0] + liste[-1])
# 10 
print(liste[1] + liste[-2])
# 10 
print(liste[2] + liste[-3])
# 10 


ardisik_toplam = gauss_2(2, 100, 3)
print(ardisik_toplam)    
# 1650.0