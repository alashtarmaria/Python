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
# Soru 4:
"""
İsmi Rectangle olan bir class tanımlayın. 
X-Y koordinat düzleminde bir dikdörtgeni temsil etsin.
Docstring'i şu olsun: "(x,y) koordinat düzlemindeki bir dikdörtgeni gösterir."

Rectangle'in 4 attribute'u vardır: 
    * kose_1 (Point)
    * kose_2 (Point)
    * kose_3 (Point)
    * kose_4 (Point)
Bu dört köşenin tipi Soru 3'de tanımladığınız Point class'ıdır.

Köşelerden 1 ve 2 aynı doğru üzerinde, 3 ve 4 aynı doğru üzerindedir.

1..............2
.              .
.              .
.              .
3..............4

Rectangle'in __init__() metodunu tanımlayın.
Ek olarak enini ve boyunu hesaplayan metodları vardır:
    * en = 1 - 2 arası mesafe  -> en_hesapla()
    * boy = 1 - 3 arası mesafe -> boy_hesapla()
Rectangle bu mesafeleri hesaplamak için Point class'ını kullanır.

Son olarak alan hesaplayan bir metodu vardır. Adı 'alan'.
'alan' metodu dikdörtgenin alanını hesaplayarak döner.

Örnek çağırma:
p_1 = Point(5, 8)
p_2 = Point(9, 8)
p_3 = Point(5, 2)
p_4 = Point(9, 2)

en = rect.en
boy = rect.boy
alan = rect.alan()

Beklenen Sonuç:
en: 4.0
boy: 6.0
alan: 24.0
"""

# Çözüm 4:
class Rectangle:
    """(x,y) koordinat düzlemindeki bir dikdörtgeni gösterir."""

    def __init__(self, p_1, p_2, p_3, p_4):
        self.kose_1 = p_1
        self.kose_2 = p_2
        self.kose_3 = p_3
        self.kose_4 = p_4
        self.en_hesapla()
        self.boy_hesapla()

    def en_hesapla(self):
        self.en = self.kose_1.uzaklik(self.kose_2)

    def boy_hesapla(self):
        self.boy = self.kose_1.uzaklik(self.kose_3)

    def alan(self):
        return self.en * self.boy


p_1 = Point(5, 8)
p_2 = Point(9, 8)
p_3 = Point(5, 2)
p_4 = Point(9, 2)

rect = Rectangle(p_1, p_2, p_3, p_4)

en = rect.en
boy = rect.boy
alan = rect.alan()

# print('en:', en)
# print('boy:', boy)
# print('alan:', alan)

# --------------------------------------------------------------------------------------#
