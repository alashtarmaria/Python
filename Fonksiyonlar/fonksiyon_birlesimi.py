# kullandığımız math.sin() fonksiyonunu tek adımda kullanmak istersek :
import math
derece = 30
sinus = math.sin(math.radians(derece))   # Chain: Fonksiyonları zincirlemek
print("Sinüs = ",sinus)


# tanımlamak: definition


# Parametresiz fonksiyon tanımalamak
def fonksiyon_adi():
    print("İlk fonksiyon")


# fonksiyonu çağırmak
fonksiyon_adi()  # ==> İlk fonksiyon





# indent: Python'da indent yapısı ile kod bölümlendirilir.
# indent: tab
# indent: 4 space

# Öğrenci Bilgileri

print("Adı: John Doe")
print("Yaşı: 24")
print("Dili: Python")
# ==>  Adı: John Doe
# ==>  Yaşı: 24
# ==>  Dili: Python

# Öğrenci bilgileri tekrar lazım olsa

print("Adı: John Doe")
print("Yaşı: 24")
print("Dili: Python")
# ==>  Adı: John Doe
# ==>  Yaşı: 24
# ==>  Dili: Python



# Parametresiz fonksiyon tanımla :
# 1
# öğrenci adını print eden fonksiyon
def ogrenci_adi():
    print("Adı: John Doe")

ogrenci_adi()  


# 2
# öğrenci yaşını print eden fonksiyon

def ogrenci_yasi():
    print("Yaşı: 24")

ogrenci_yasi()


# 3
# öğrencinin kullandığı dili print eden fonksiyon
def ogrenci_dili():
    print("Dili: Python")

ogrenci_dili()    


# Öğrenci bilgilerini tekrar yaz
ogrenci_adi()
ogrenci_yasi()
ogrenci_dili()


# tekrar öğrenci bilgileri
ogrenci_adi()
ogrenci_yasi()
ogrenci_dili()


# bütün öğrenci bilgilerini yazan tek fonksiyon yazalım
def ogrenci_bilgileri():
    ogrenci_adi()
    ogrenci_yasi()
    ogrenci_dili()
    

# tekrar öğrenci bilgileri
ogrenci_bilgileri()    
print("type :" ,type(ogrenci_bilgileri))
print(ogrenci_bilgileri)


# Peki, öğrencinin adını ve soyadını ayrı ayrı yazmak istesek , O zaman ogrenci_adi() fonksiyonunu iki alt fonksiyona bölmemiz lazım.:
# "Adı": "Peter"
# "Soyadı": "Parker"

# öğrencinin ilk adını ve soyadını veren iki ayrı fonksiyon yazalım

def ogrenci_ilk_adi():
    print("Adı: Peter")
    
    
def ogrenci_soyadi():
    print("Soyadı: Parker") 
    


# Şimdi öğrenci adı fonksiyonunu iki alt fonksiyonun birleşimi olarak yazalım
def ogrenci_adi():
    
    ogrenci_ilk_adi()
    
    ogrenci_soyadi()

#Çağıralım :
ogrenci_adi()
ogrenci_bilgileri()



# İşleme Sırası (Execution Flow):

# Python kodu, ilk satırdan itibaren çalıştırmaya başlar. 
# Ve aşağı doğru iner.
# Eğer bir fonksiyon çağrılmasına denk gelirse,
# Önce gider, o fonksiyonu çalıştırır, bitmesini bekler, geri döner.
# Kaldığı yerden aşağı doğru çalışmaya devam eder.



