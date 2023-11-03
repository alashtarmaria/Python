#----------------------------------------------------------------------------------------------------------------------------#
# Alıştırma 3:
# Şimdi bir çember çizen bir fonksiyon yazalım.
# Bu fonksiyonun parametreleri: kaplumbağa (t), yarıçap (r).
# Bu fonksiyon, poligon fonksiyonunu çağıracak ve çizimi ona yaptıracak.
# Kendisi bir çizim yapmayacak.
# 50 kenarlı bir poligon çizelim.

import math
import turtle
t = turtle.Turtle()

def poligon(t, uzunluk, n):
    """
    Kaplumbağa ile poligon çizen fonksiyon.
    Parametreler:
        * t: turtle tipinde nesne
        * uzunluk: int tipinde yürüme miktarı, pixel
        * n: int tipinde kenar sayısı
    """
    
    # dönüş derecesini hesapla
    aci = 360 / n
    
    for i in range(n):
        t.fd(uzunluk)
        t.lt(aci)


def cember(t, r):
    """
    Cember çizen fonksiyon.
    Parametreler:
        * t: turtle tipinde kaplumbağa
        * r: int tipinde yarıçap
    Dönüş: poligon fonksiyonunu çağırıp, ekrana çember çizer
    """
    
    cevre = 2 * math.pi * r
    n = 50
    uzunluk = cevre / n
    poligon(t, n=n, uzunluk=uzunluk)


turtle.resetscreen() 


# cember'i çağır
cember(t, 100)   


# Bu çözümün sorunu n (kenar sayısının) sabit olması.
# Kenar sayısını (n) yarıçap'a göre hesaplayalım.


import math

def cember(t, r):
    """
    Cember çizen fonksiyon.
    Parametreler:
        * t: turtle tipinde kaplumbağa
        * r: int tipinde yarıçap
    Dönüş: poligon fonksiyonunu çağırıp, ekrana çember çizer
    """
    
    cevre = 2 * math.pi * r
    
    n = int(cevre / 3)
    
    uzunluk = cevre / n
    
    poligon(t, n=n, uzunluk=uzunluk)



# şimdi tospik'i tekrar çalıştır
t.clear()

cember(t, 100)