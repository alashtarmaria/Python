# Soru 9:

# Matematik'teki ardışık sayılar aslında bir listedir.

# Gauss Yöntemi ardışık sayıların toplamını veren bir yöntemdir. Ve şu şekilde çalışır:

# Önce listeyi küçükten büyüğe yazar
# Sonra büyükten küçüğe yazar
# Bu iki listeyi index bazlı alt alta toplar
# Bulduğu değeri 2'ye böler (çünkü listeyi 2 kere yazmıştır)
# Gauss Yöntemi böylece ardışık sayılar toplamını bulmuş olur
# Örnek: 1'den 10'a kadar sayıların toplamı:

# 1   2   3   4   5   6   7   8   9   10
# 10  9   8   7   6   5   4   3   2   1
# +   +   +   +   +   +   +   +   +   +
# 11  11  11  11  11  11  11  11  11  11    (ikili toplamlar)

# Toplam = 11 * 10
# Sonuç = Toplam / 2
# Bu soruda, 20'den başlayıp 300'e kadar 5'er 5'er artarak giden sayıların toplamını Gauss Yöntemi ile bulan bir fonksiyon yazın. Fonksiyonun adı gauss olsun.

# Fonksiyon parametre olarak, başlangıç değeri, bitiş değeri ve artış miktarını alsın.

# Parametrelerin adlari ve default değerleri şu şekilde olsun:

# baslangic -> 1
# bitis -> 100
# artis -> 2
# Yapılacaklar:

# Listeyi range() fonksiyonu ile üretiniz

# Çözüm 9:

# Birinci yol
# Uzun yol

def gauss(baslangic=1, bitis=100, artis=2):
    
    # önce list oluştur
    liste = list(range(baslangic, bitis, artis))
    
    # listenin tersi
    ters_liste = liste[::-1]
    
    # toplam
    toplam = 0
    
    for i in range(len(liste)):
        
        ikili_toplam = liste[i] + ters_liste[i]
        
        toplam += ikili_toplam
        
    sonuc = toplam / 2
    
    return sonuc        

ardisik_toplam = gauss(1, 10, 1)
print(ardisik_toplam)    
# 45 . 0




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

ardisik_toplam = gauss_2(2, 100, 3)
print(ardisik_toplam)    
# 1650.0