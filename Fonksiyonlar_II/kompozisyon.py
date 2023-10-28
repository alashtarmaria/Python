#----------------------------------------------------------#
### Kompozisyon - Fonksiyonların Beraber Kullanımı
# Fonksiyonel Programlama

# Yapılacak işleri küçük parçalara bölmek, ve onları kendi fonksiyonlarına vermek.

# Ör: Diyelim ki elimizde iki nokta var. 

# Bu iki noktayı birleştiren doğru parçasını yarıçap kabul edelim.

# Bu yarıçapa sahip dairenin alanını hesaplayalım.

# Bu işleri tek fonksiyon içinde yapmak yerine, zaten bu alt işlemler için uzmanlaşmış fonksiyonları çağırabiliriz.
#----------------------------------------------------------#
import math
#----------------------------------------------------------#

def uzaklik(x1, y1, x2, y2):
    
    # önce x'ler arasındaki farkı hesapla
    dx = x2 - x1
    
    # sonra y'ler arasındaki farkı hesapla
    dy = y2 - y1
    
    # <----- DEBUG ----->
    # daha fazla devam etmeden bunları doğru hesapladığımızı kontrol edelim
    
    # print("dx:", dx)
    # print("dy:", dy)
    
    # karelerin toplamını hesapla
    kareler_toplami = dx**2 + dy**2
    
    # <----- DEBUG ----->
    # print("kareler toplamı: :", kareler_toplami)
    
    return math.sqrt(kareler_toplami)
    


#----------------------------------------------------------#

def alan(yaricap):
    
    a = math.pi * yaricap**2
    
    return a
    
# daire_alani = alan(4)
# print(daire_alani)    

#----------------------------------------------------------#

def iki_noktadan_gecen_daire_alani(x1, y1, x2, y2):
    """
    Yarıçapı verilen iki nokta arası olan bir dairenin alanını hesaplar.
    Parametreler:
        * x1: int, birinci noktanın x koordinatı
        * y1: int, birinci noktanın y koordinatı
        * x2: int, ikinci noktanın x koordinatı
        * x2: int, ikinci noktanın y koordinatı
    Dönüş: dairenin alanı (int)
    """
    
    # yarıçapı hesaplayalım
    r = uzaklik(x1, y1, x2, y2)
    print("r:", r)
    
    # alanı hesapla
    a = alan(r)
    print("alan:", a)
    
    return a    


iki_noktadan_gecen_daire_alani(1, 6, 4, 10)    