#---------------------------------------------------------------------------------------#
# Fonksiyonlar II
# Fonksiyonlar çoğu zaman, işlemlerini bitirdikten sonra geriye değer dönerler.

# Fonksiyonu çağran yer de o değeri alır ve buna göre işlemlerini yapar.
# Geriye değer dönmeyen fonksiyonlara **void** fonksiyonlar denir.
# Geriye değer dönme -> **return**

#----------------------------------------------------------#

# **Önemli Not:** Fonksiyon içinde, return ifadesinden sonra gelen kodlar çalıştırılmaz. 
# Çünkü return fonksiyondan çıkış demektir.

#----------------------------------------------------------#
###########################################################################################

### Dönüş Değeri
#----------------------------------------------------------#
# Örnek :
import math
e = math.exp(1.0)

print(e)

#----------------------------------------------------------#
# Örnek :
# dairenin alanını hesaplayan bir fonksiyon yazalım ve değerini alıp ekrana basalım.
def alan(yaricap):
    
    a = math.pi * yaricap**2
    
    return a
    
daire_alani = alan(4)
print(daire_alani)    

#----------------------------------------------------------#

# Yukarıdaki alan fonksiyonunun içindeki `a` değişkenine **geçici değişken** denir.
# Tek amacı hesaplanan alan değeri tutup bunu return'e vermek.
# Bu geçici değişkenleri kullanmayabiliriz. (Genelde debug işlemleri için önerilir.)
#----------------------------------------------------------#

# Geçici değişken olmadan alan fonksiyonu

#----------------------------------------------------------#
# Örnek :
def alan(yaricap):
    return math.pi * yaricap**2


daire_alani = alan(4)
print(daire_alani)

# Yukarıda print(daire_alani) yazdık -> geçici değişken verdik

#----------------------------------------------------------#
# daire_alani
print(alan(4))
#----------------------------------------------------------#

