# Parametreler (Argümanlar) :

# Çoğu zaman fonksiyonlar parametrelere ihtiyaç duyarlar.
# Parametre fonksiyonun çalışması için kendisine iletilen girdilerdir.
# Parametreler, fonksiyon çağrılırken iletilir.


# Diyelim ki kendisine iletilen sayının karesini alan bir fonksiyon yazmak istiyoruz
def karesini_yaz(sayi):
    
    # sayının karesini al
    karesi = sayi**2
    
    # sayının karesini yaz
    print(karesi)

# şimdi bu fonksiyonu parametre ile çağıralım:

karesini_yaz() 
# TypeError: karesini_yaz() missing 1 required positional argument: 'sayi'

karesini_yaz(5) 
# 25



# Örnek:
# İki parametre alan bir fonksiyon tanımlayalım
# İki parametre: kisa_kenar, uzun_kenar
# Fonksiyon dikdörtgenin alanını hesaplasın

def dikdortgen_alani_hesapla(kisa_kenar, uzun_kenar):
    
    # alan hesapla -> bunu bir değişkene ata
    dikdortgen_alani = kisa_kenar * uzun_kenar
    
    # bu alanı print et
    print("Alan = ",dikdortgen_alani)


# Şimdi fonksiyonu, iki parametre ile çağıralım
dikdortgen_alani_hesapla(4, 6)

# 2.yöntem 
kisa = 4
uzun = 6

dikdortgen_alani_hesapla(kisa, uzun)



# Örnek:
# Daha önce tanımladığımız ogrenci_bilgileri fonksiyonunu bu sefer parametrik yapalım

# öğrenci ilk adı
def ogrenci_ilk_adi(ilk_adi):
    print("Adı: " + ilk_adi)
    
# öğreci soyadı
def ogrenci_soyadi(soyadi):
    print("Soyadı: " + soyadi)
    
# öğrenci yaşı
def ogrenci_yasi(yas):
    print("Yaşı: " + str(yas))
    
# öğrenci dili
def ogrenci_dili(dil):
    print("Dili: " + dil)
    
    
def ogrenci_bilgileri(ilk_adi, soyadi, yas, dil):
    
    # öğrenci ilk adı
    ogrenci_ilk_adi(ilk_adi)
    
    # öğrenci soyadı
    ogrenci_soyadi(soyadi)
    
    # öğrenci yaşı
    ogrenci_yasi(yas)
    
    # öğrenci dili 
    ogrenci_dili(dil)

# fonksiyonu çağıralım :
ilk = 'Klark'
soy = "Kent"
yasi = 28
kullandigi_dil = 'Python'

ogrenci_bilgileri(ilk, soy, yasi, kullandigi_dil)