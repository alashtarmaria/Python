# Matematiksel işlemleri yapmak için Python'da **math** modülü kullanılır.
# **Modül:** birbiriyle ilgili fonksiyonları ve dosyaları bir arada tutan dosya kümeleridir.
# Bir fonksiyon hakkında bilgi almak için help(<fonksiyon_adi>) şeklinde bir ifade kullanabiliriz.


# math modülü içeri nasıl alınır
import math


# math modülünü görelim
#print(math)


# Python'da help özelliği vardır
#help(math)


# math modülü içindeki bir fonksiyonu -> . ile çağırılır
#math.pi


# Örnek1 :
# Yarı çapı 10 cm olan bir çemberin çevresi ne kadardır?
# Çevre = 2 * pi * r
r = 10
cevre = 2 * math.pi * r
print("Çevre =" ,cevre) # ==> 62.83185307179586


# Örnek2:
# 30 derecenin sinüsünü hesaplayalım
derece = 30
# radyan hesapla
radyan = math.radians(derece)
print("Radyan = " ,radyan) # ==>  0.5235987755982988


# Örnek3:
# Yanlış kullanım 
sinus = math.sin(derece)
print("Sinüs = ",sinus) # ==>  -0.9880316240928618
 # help(math.sin) => burada radayan olarak vememiz lazım 


# Doğru kullanım
sinus = math.sin(radyan)
print("Sinüs = ",sinus) # ==>  0.49999999999999994


# Yukarıda kullandığımız math.sin() fonksiyonunu tek adımda kullanmak istersek :
import math
derece = 30
sinus = math.sin(math.radians(derece))
print("Sinüs = ",sinus)