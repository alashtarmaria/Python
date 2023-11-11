"""
 OOP ile ilgili QUIZ - 10 Soru
"""

# --------------------------------------------------------------------------------------#

# Soru 1:
"""
Adı Ogrenci olan bir class tanımlayın.
Ogrenci'nin 2 özelliği var:
* isim (str)
* numara (str)

Bu Ogrenci class'ından iki öğrenci yaratın.
Bilgileri şu şekilde olacak:
1- isim: James Bond, numara: 007
2- isim: Klark Kent, numara: 333

Sonra bu iki öğrencinin adlarını print edin.

İpuçları:
* __init__

Beklenen Sonuç:
James Bond
Klark Kent
"""

# Çözüm 1:
class Ogrenci:
    def __init__(self, isim, numara):
        self.isim = isim
        self.numara = numara


# Öğrenci nesneleri yarat
ogr_1 = Ogrenci('James Bond', '007')
ogr_2 = Ogrenci('Klark Kent', '333')

# print(ogr_1.isim)
# print(ogr_2.isim)

# --------------------------------------------------------------------------------------#

# Soru 2:
"""
Soru 1'deki Ogrenci class'ımızın şimdi de kayıt olduğu dersleri tutan,
bir attribute'u (özelliği) daha olsun. 
Bu özelliğin adı 'dersler' olsun ve list tipinde olsun.
Bu özellik, Ogrenci yaratılırken boş liste olarak initialize olacak.

Ogrenci derslere birer birer katılacak.
Dolayısı ile 'derse_katil()' adında bir metodu da olacak.
Be metod parametre olarak katılacak dersi alacak.
Eğer ders henüz listede yoksa, o zaman kayıt olacak.

Ek olarak 'get_dersler' adında bir metod daha olacak.
Bu metod bize öğrencinin kayıt olduğu ders listesini verecek.

Buna göre Ogrenci class'ını modifiye edin.

Öğrencinin bilgileri şu şekilde olacak:
isim: Cin Ali, numara: 1111
katılacağı dersler: Temel Python ve Yapay Zeka

Beklenen Sonuç:
ogrenci.get_dersler()  ->  ['Temel Python', 'Yapay Zeka']
"""

# Çözüm 2:
class Ogrenci:
    def __init__(self, isim, numara):
        self.isim = isim
        self.numara = numara
        # ders listesini -> []
        self.dersler = []

    def derse_katil(self, ders):
        # bu ders yoksa -> ekle
        if not ders in self.dersler:
            self.dersler.append(ders)

    def get_dersler(self):
        return self.dersler


ogrenci = Ogrenci('Cin Ali', '1111')

ogrenci.derse_katil('Temel Python')
ogrenci.derse_katil('Yapay Zeka')

# print(ogrenci.get_dersler())

# --------------------------------------------------------------------------------------#
# Çözüm 3:
import math

class Point:
    """(x,y) koordinat düzlemindeki bir noktayı gösterir."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def uzaklik(self, diger):
        x_ler_farki = self.x - diger.x
        y_ler_farki = self.y - diger.y
        d = math.sqrt(x_ler_farki**2 + y_ler_farki**2)
        return d


nokta_1 = Point(1, 7)
nokta_2 = Point(4, 3)

# docstring'i yazdır
# print(nokta_1.__doc__)

uzaklik = nokta_1.uzaklik(nokta_2)
print(uzaklik)

# --------------------------------------------------------------------------------------#

