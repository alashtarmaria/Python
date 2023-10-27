#----------------------------------------------------------------------------------------------------------------------------#

# Alıştırma 2:
# Şimdi poligon çizen bir fonksiyon yaratalım.
# Fonksiyonun parametreleri, kaplumbağa, mesafe ve kenar sayısı olacak.
# Çözüm 2:
# poligon fonksiyonumuzu tanımlayalım

def poligon(t, uzunluk, n):
    """
    Kaplumbağa ile poligon çizen fonksiyon.
    Parametreler:
        * t: turtle tipinde nesne
        * uzunluk: int tipinde yürüme miktarı, pixel
        * n: int tipinde kenar sayısı
    """
    
    for i in range(n):
        t.fd(uzunluk)
        t.lt(90)


# turtle modülünü import et
import turtle

# bir kaplumbağa yarat
t = turtle.Turtle()

# poligon'u çağır
poligon(t, 100, 6)
poligon(t, 100, 10)

t.clear()
turtle.mainloop()

#----------------------------------------------------------------------------------------------------------------------------#

# **Dönüş Derecesi = 360 / kenar sayısı**
# tekrardan çözelim :
# Çözüm :

# poligon fonksiyonumuzu tanımlayalım
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


# poligon'u çağır
poligon(t, 100, 6)
poligon(t, 100, 10)


# ekranı boşalt
t.clear()


# 100 pixel ile 10 kenarlı poligon
poligon(t, 100, 10)

# ekranı boşalt
turtle.resetscreen()


# poligon'u çağır
poligon(t, uzunluk=200, n=12)

turtle.resetscreen()
poligon(t=t ,n=12, uzunluk=100)
#--------  İsimlendirilmiş Parametreler** -> `keyword arguments`  -----------

turtle.mainloop()