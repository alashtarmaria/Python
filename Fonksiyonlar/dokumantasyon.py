### Docstring - Fonksiyonun Dokümantasyonu

# örnek :
def cube(n):
    n_kup = n**3
    return n_kup
 
print(cube(3))


# Fonksiyonun hakkında yardım alalım
help(cube)

# Help on function cube in module __main__:
# cube(n)


# Yardım görmek için -> biraz daha detaylı yardım
# cube?
# Signature: cube(n)
# Docstring: <no docstring>
# File:      c:\users\musaa\desktop\python\icerik\5_fonksiyonlar_i\<ipython-input-87-8ce6df08a509>
# Type:      function



# Yardım 3 -> en detaylısı
# Source kodu da gösterir
# cube??
# Signature: cube(n)
# Docstring: <no docstring>
# Source:   
# def cube(n):
    
#     # sayının küpünü hesapla
#     n_kup = n**3
    
#     # bu küp değerini geri dön
#     return n_kup
# File:     
# Type:      function




# Docstring'i olan bir fonksiyon yazalım

import math

def ustel_hesapla(sayi, ust):
    """
        Bu fonksiyon üstel hesaplama yapar.
        Parametreler: int sayi, int ust
        Sonuc: verilen sayinin, verilen üstünü döner.
    """
    
    # sayının üstünü hesapla
    # ustel = sayi**ust
    ustel = math.pow(sayi, ust)
    
    # bulduğun üssü döne
    return ustel
    

# Şimdi bu fonksiyon için yardım çağıralım
# help()
help(ustel_hesapla)

# ? ile yardım
#ustel_hesapla?


# ?? ile yardım
#ustel_hesapla?

# import math
# print(dir(math))

# Docstring için -> __doc__
# 1
ustel_hesapla.__doc__

# 2
print(ustel_hesapla.__doc__)


# Yarattığımız ustel_hesapla fonksiyonu için hangi modülde olduğunu görmek için
print(ustel_hesapla.__module__)

# __main__
# main modülü, bizim şu anda içinde çalıştığımız modüldür.


print(ustel_hesapla.__name__)