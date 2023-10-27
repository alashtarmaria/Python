#----------------------------------------------------------------------------------------------------------------------------#

# Alıştırma 1:
# İsmi kare olan bir fonksiyon yazın.
# Bu fonksiyon Kaplumbağa tipinde t adında bir parametre alsın.
# Ek olarak, kaç adım yürüyeceğini de parametre olarak alsın.
# Bu kaplumbağayı kullanarak bir kare çizsin fonksiyonumuz.
import turtle
# Çözüm 1:

# fonksiyonumuzu tanımlayalım

def kare(t, uzunluk):
    """
    Kaplumbağa ile kare çizen fonksiyon.
    Parametreler:
        * t: turtle tipinde nesne
        * uzunluk: int tipinde yürüme miktarı (pixe)
    """
    
    # döngü ile kare çizdir
    for i in range(4):
        t.fd(uzunluk)
        t.lt(90)


# önce tospik'imizi yaratalım
tospik = turtle.Turtle()



# şimdi kare fonksiyonunu çağıralım
# önce 100 pixel ile çağıralım
kare(tospik, 100)

# sonra 200 pixel ile çağıralım
kare(tospik, 200)

# son olarak 300 pixe ile çağıralım
kare(tospik, 300)



# şimdi araları dolduralım:
# 300 - 100 = 200
# 10 seferde doldurmak için 200 / 10 = 20 pixel
for i in range(10):
    kare(tospik, 100 + i * 20)


# Tospik'i temizlemek için
tospik.clear()

turtle.mainloop()