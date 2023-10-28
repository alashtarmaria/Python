#--------------------------------------------------------------------------------------#
# ########################### hata ayıklama(debug) #####################################
#--------------------------------------------------------------------------------------#
# Adım Adım Geliştirme 
# Kodlama yaparken, her şeyi tek seferde düşünemeyiz ve yapamayız.
# Bu yüzden adım adım geliştirme üzerine yoğunlaşmamız lazım.
# Adım adım geliştirme,  hata ayıklama(debug) için olmaz olmaz bir kavramdır.
# Eğer programın her adımında neyi yaptığını debug edemezseniz, o zaman her şeyi doğru yaptığından emin olamazsınız.


#-------------------------------------------------------------------#

# Örnek : 
# Diyelim ki iki nokta arasındaki mesafeyi hesaplamak istiyoruz.
       # Noktalar -> (x1, y1) ve (x2, y2)   
       # Matematikten bu iki nokta arasındaki uzaklık, Pisagor Teoreminden şöyle hesaplanır:
       # uzaklık = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}
# Fakat, bu tek satırlık formül, Python'da bu kadar basit değil.
# Be hesaplamadaki her bir adımı, tek tek planlamamız lazım.

# Şimdi bu fonksiyonu yazalım:
def uzaklik(x1, y1, x2, y2):
    
    # önce x'ler arasındaki farkı hesapla
    dx = x2 - x1
    
    # sonra y'ler arasındaki farkı hesapla
    dy = y2 - y1
    
    # <----- DEBUG ----->
    # daha fazla devam etmeden bunları doğru hesapladığımızı kontrol edelim
    
    print("dx:", dx)
    print("dy:", dy)

uzaklik(1, 6, 4, 10)    

#-----------------------------------------------------------------------------#
# Geliştirmeye devam:
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
    print("kareler toplamı: :", kareler_toplami)
    

uzaklik(2, 6, 10, 21)    
uzaklik(1, 6, 4, 10)

#-----------------------------------------------------------------------------#
# Geliştirmeye devam:
# **TDD (Test Driven Development)**: Her adımı test ederek ilerleme.

import math

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
    

uzaklik(2, 6, 10, 21)
uzaklik(1, 6, 4, 10)


#-----------------------------------------------------------------------------#