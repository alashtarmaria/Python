# ------------------------------ TEMEL KAVRAMLAR ---------------------------#

"""
Object Oriented Programming (OOP)
Nesne Tabanlı Programlama

Nesne -> etrafımızdaki herşey

Python'da nesnelerin özellikleri:
* öznitelikler (attribute)
* davranışları (behavior)

Örnek:
Penguen
* öznitelikleri: adi, yaşı, boyu, kilosu, rengi, turu...
* davranışları: yüzme, yürüme, şarkı söyleme, dans etme...

OOP: Kod tekrarını önlemek için var.
DRY: Do not repeat yourself
"""

"""
Class (Sınıf):
Class bir nesnenin eskiz çizimidir.
Mimari çizimidir.
Nesnenin neye benzeyeceğini anlatır.
Ör: Bina bir nesnedir. O binanın kağıt üstündeki çizimi (mimari çizim) Class'dır.

Penguen:
Kağıda çizilmiş bir penguen, çizim olan, Sınıfıdır.
O çizimden yapılmış gerçek Penguen'de Nesnedir.
"""


class Penguen:
    pass


"""
Class yaratmak için 'class' anahtar kelimesi kullanılır.
TANIMLADIĞIMIZ Class'ımızın adı Penguen.
"""

"""
Object (Nesne):
Nesne, Class'ın hayat bulmuş şeklidir. (instance)
Class'ın ete kemiğe bürünmüş halidir.
Instance: Tekil olarak YARATILMIŞ bir nesnedir.
"""

nesne = Penguen()

"""
Nesneler class'ların çağrılması ile oluşturulur.
"""

"""
Class Attribute:
Bütün Penguen'lerin ortak özellikleri vardır.
Bilimsel olarak türü (species) -> kuş
İşte sınıftan (class) üretilmiş bütün varlıklarda (nesne) ortak olan özelliklere;
Class Attribute

Instance Attribute:
Tekil bir nesneye özel nitelikler; 
Instance Attribute
Penguen, yaşı, rengi, kilosu, boyu
"""

"""
Metod = Fonksiyon 
Metod'lar Class içinde tanımlanan fonksiyonlardır.
"""


class Penguen:

    # class attribute'ları (sınıf öznitelikleri)
    tur = 'Kuş'

    # instance attribute'ları (varlığın öznitelikleri)
    def __init__(self, ad, yas, renk):
        self.ad = ad
        self.yas = yas
        self.renk = renk

"""
self: o anda yaratılan nesneyi anlatır
"""

# İki adet Penguen Nesnesi yaratalım
kral = Penguen('Kral Penguen', 4, 'Turuncu')
sari_goz = Penguen('Sarı Gözlü Penguen', 1, 'Kahverengi')

# önce class attribute'larını print edelim
# print("{0}'ın bilimsel türü: {1}".format(kral.ad, kral.__class__.tur))
# print("{0}'ın bilimsel türü: {1}".format(sari_goz.ad, sari_goz.__class__.tur))

# instance attribute'larını print edelim
# print("{0}'in yaşı {1} ve rengi {2}".format(kral.ad, kral.yas, kral.renk))
# print("{0}'in yaşı {1} ve rengi {2}".format(sari_goz.ad, sari_goz.yas, sari_goz.renk))

"""
Attribute'lara -> '.' ile erişilir.
* Class Attribute ise -> .__class__.
* Instance Attribute -> .
"""

"""
__init__(self, ....):
Bir class'tan, nesne yaratılırken ilk çağrılan yaratıcı (yapıcı, contructor) metoddur.
__init__() instance oluşturur.

* self: O anda yaratılmakta olan nesneyi anlatır.
Nesnenin özellikleri:
self.ad = ...
self.renk = ...
self.yas = ...
"""

"""
Metodlar (Davranışlar):
Method bir class içinde tanımlanmış fonksiyondur.
Nesnelerin davranışlarını anlatır.
"""


# Penguen Class'ımıza metod ekleyelim
class Penguen:

    # class attribute
    tur = 'Kuş'

    # instance attribute'lar
    def __init__(self, ad, yas, renk):
        self.ad = ad
        self.yas = yas
        self.renk = renk

    # instance method (varlığın metodu)
    def yuzme(self):
        return f"{self.ad} yüzebilir."

    def sarki_soyle(self, soyleyebilir_mi=False):
        if soyleyebilir_mi:
            return f"{self.ad} şarkı söylebilir."
        else:
            return f"{self.ad} şarkı söylemeyez."

    def dans_et(self, dans_edebilir_mi=False):
        if dans_edebilir_mi:
            return f"{self.ad} dans edebilir."
        else:
            return f"{self.ad} dans edemez."


# yeni Penguen nesneleri oluştur
makaroni = Penguen('Makaroni Pengueni', 8, 'Sarı-Siyah')

# print(makaroni.yuzme())
#
# # Makaroni Pengueni şarkı söyleyebilir
# print(makaroni.sarki_soyle(soyleyebilir_mi=True))
#
# # Makaroni dans edemez
# print(makaroni.dans_et(False))
#
# # Neşeli Ayaklar Penguenini yarat
neseli_ayaklar = Penguen('Neşeli Ayaklar', 1, 'Gri-Papyon')

# # Neşeli Ayaklar yüzebilir
# print(neseli_ayaklar.yuzme())
#
# # Neşeli Ayaklar Penguen'i şarkı söyleyemez
# print(neseli_ayaklar.sarki_soyle(False))
#
# # Neşeli Ayaklar dans edebilir
# print(neseli_ayaklar.dans_et(True))



# ------------------------------ KALITIM ---------------------------#

"""
Kalıtım (Inheritance):
Aynen gerçek hayattaki gibi, OOP'de Class'lar birbirinden Kalıtım alabilirler.
Kalıtım Alan Class -> Child Class, Derived Class (Çocuk Classı)
Kalıtım Veren Class -> Parent Class, Base Class (Ana Class) - Super
"""


# Kuş Sınıfını yaratalım
class Kus:
    def __init__(self):
        print('Kuş yaratıldı.')

    def kimimBen(self):
        print('Ben bir Kuşum.')

    def ucma(self):
        print('Kuşlar uçabilir.')

    def yuzme(self):
        print('Kuşlar yüzebilir.')


# bir Kuş nenesi yarat
# minik_kus = Kus()
# minik_kus.kimimBen()
# minik_kus.ucma()
# minik_kus.yuzme()


# Kuş türleri için bir ana class'ımız var.
# Baykuş da bir kuş -> child class


# child class - derived class
class Baykus(Kus):
    # Bir sınıf hangi sınıftan kalıtım alıyorsa, parantez içinde ana sınıf yazılır.

    def __init__(self):
        # önce ana sınıfının, super(), __init__() metodunu çağır
        super().__init__()
        print('Baykuş yaratıldı.')

    def kimimBen(self):
        print('Ben bir Baykuşum.')

    # Baykuş da tüm kuşlar gibi uçtuğu için ucma() metodunu overrirde (ezmek) etmeye gerek yok
    # aynen kullanacağız

    def yuzme(self):
        print('Baykuşlar yüzemez.')

    # Baykuşların gece görüşü vardır.
    def gece_gorusu(self):
        print("Baykuşun gece görüşü vardır.")


# kucuk_baykus = Baykus()
# kucuk_baykus.kimimBen()
# kucuk_baykus.ucma()
# kucuk_baykus.yuzme()
# kucuk_baykus.gece_gorusu()

# minik_kus -> Kus türünde idi
# minik_kus.gece_gorusu()


















