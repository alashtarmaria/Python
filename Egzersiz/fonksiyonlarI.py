#Soru 1:
# Ekrana "Selam Dünya!" yazan bir fonksiyon yazın.
def selamlama():
    print("Selam Dünya!")
    
selamlama()                                # --> Selam Dünya



#Soru 2:
# String şeklinde iki parametre alan bir fonksiyon yazın. Bu parametreleri kişi ismi kabul edelim.
# Fonksiyon bu iki ismi "ve" ile bağlayarak selamlasın.
# Ör: Selam Clark Kent ve Superman.
# (String'in format fonksiyonu kullanın.)
# 1.yol
def isimleri_selamla(isim1,isim2):
    birlesmis_adi = "Selam " + isim1 + " ve " + isim2
    print(birlesmis_adi)
          
        
isimleri_selamla("Clark Kent","Superman")     # --> Selam Clark Kent ve Superman
isimleri_selamla("Bruce Wayne", "Batman")     # --> Selam Bruce Wayne ve Batman
isimleri_selamla("Peter Parker","Spiderman")  # --> Selam Peter Parker ve Spiderman

# 2.yol
def isimleri_selamla2(isim1,isim2):
    print("Selam {0} ve {1}".format(isim1,isim2))

isimleri_selamla2("Clark Kent","Superman") 



#Soru 3:
# Kullanıcıdan girdi olarak ismini isteyen bir fonksiyon yazın.
# Bu fonksiyon aldığı ismi "Selam sana ...." şeklinde selamlasın.
# (Girdi almak için input() fonksiyonunu kullanın.)
def ismini_soyle():
    # input() -> enter tuşunu bekler
    adi = input("Lütfen ismini söyler misin ? ")
    # enter sonrasında kod devam eder
    # 1.yol 
    # print("Selam sana",adi)
    # 2.yol 
    print("Selam sana {0}".format(adi))

ismini_soyle()                     # --> Selam sana Python 




#Soru 4:
# Parametre olarak 3 sayı alan bir fonksiyon yazın.
# Fonksiyon bu sayılardan en büyüğünü size geri dönsün.
# Bu fonksiyonun docstring'ini de yazın.
# Çözüm 4:
# 1.yol
def maksimum_getir(sayi_1, sayi_2, sayi_3):
    """
    Bu fonksiyon 3 sayı alır ve en büyüğünü (max) döner.
    Parametreler: int sayi1, sayi2, sayi3
    Sonuc: Python'un max fonksiyonun verdiği değeri döner.
    """
    return max(sayi_1, sayi_2, sayi_3)

print(maksimum_getir(10,82,5))
help(maksimum_getir)

# 2.yol
def maksimum_getir_2(sayi_1, sayi_2, sayi_3):
    """
    Bu fonksiyon 3 sayı alır ve en büyüğünü (max) döner.
    Parametreler: int sayi1, sayi2, sayi3
    Sonuc: Python'un max fonksiyonun verdiği değeri döner.
    """
    # max sayısyı al = > max()
    maksimum = max(sayi_1, sayi_2, sayi_3)
    return maksimum

# fonksiyonu çağır --> dönen değeri al be yazdır
maksimum_sayi = maksimum_getir_2(10,82,5)
print(maksimum_sayi)
help(maksimum_sayi)




#Soru 5:
# Parametre olarak gelen metni parçalayan küçük harfe çeviren bir fonksiyon yazın.
     #  parçalamak için: strip()
     #  küçük harf yapmak için: lower()

def parcala_ve_kucuk_yap(orjinal_metin):
    # strip() => boşluk karakterlerinden parçalar 
    parcalanmis_metin = orjinal_metin.strip()
    print("Çirkin metin :",parcalanmis_metin)

    # lower() = > küçük harf yapar
    kucultmus_metin = parcalanmis_metin.lower()
    print("Düzgün metin :",kucultmus_metin)


metin = "PyThon MaCHine LEARning"    
parcala_ve_kucuk_yap(metin)



#Soru 6:
# Parametre olarak gelen iki sayının toplamını dönen bir fonksiyon yazın.
# 1. yol
def topla(sayi_1 ,sayi_2):
    return sayi_1 + sayi_2

topla(10 , 8)



#Soru 7:
# Parametre olarak gelen 3 sayı alan bir fonksiyon yazın.
# Fonksiyon bu sayıların ikili farklarını alsın ve bu farklardan en küçüğünü dönsün.
         # Fark için mutlak değeri kullanın -> abs (absolute value)
         # Minimum için -> min
def en_kucuk_fark(sayi_1 ,sayi_2 , sayi_3):
    fark_1 = abs(sayi_1 - sayi_2)
    fark_2 = abs(sayi_2 - sayi_3)
    fark_3 = abs(sayi_1 - sayi_3)
    return min(fark_1,fark_2,fark_3)

print(en_kucuk_fark(8,5,10))

# daha uzun çağırma yöntemi 
# a = 5
# b = 8
# c = 10
# min_fark = en_kucuk_fark(a,b,c)
# print(min_fark)



#Soru 8:
# Parametre olarak bir sayı alan bir fonksiyon yazın.
# Fonksiyon bu sayının karekökünü dönsün.
# Karekök için -> math.sqrt()
# Çözüm 8:
import math
def kare_kok_al(sayi):
    kare_kok = math.sqrt(sayi)
    return kare_kok

print(kare_kok_al(81))



#Soru 9:
# Parametre olarak bir sayı alan bir fonksiyon yazın.
# Fonksiyon bu sayının logaritmasını dönsün.
# Logaritma için -> math.log()
import math
def logaritmayi_al(sayi):
    logaritma = math.log(sayi)
    return logaritma

print(logaritmayi_al(12))



#Soru 10:
# 1.yol
import math
def hepotenus_hesapla(n1,n2):
    return math.sqrt(n1**2 + n2**2)

print(hepotenus_hesapla(4,3))

# 2.yol
import math
def hepotenus_hesapla_2(n1,n2):
    hip = n1**2 + n2**2
    return math.sqrt(hip)

print(hepotenus_hesapla_2(3,4))       # --> 5.0
print(hepotenus_hesapla_2(7,24))      # --> 25.0
print(hepotenus_hesapla_2(8,15))      # --> 17.0

