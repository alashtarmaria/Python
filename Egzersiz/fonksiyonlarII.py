# Soru 1:
# Ekrandan girdi okuyan fonksiyonlar yazdık. Şimdi bu girdi okuma işini jenerik bir hale getirelim.
# Bu fonksiyon, parametre olarak, text türünde bir istek metni alsın ve bu metne göre kullanıcıdan girdi istesin.
# Sonra aldığı girdiyi bize geri göndersin (dönsün).
# Son olarak, bu fonksiyonun geriye hangi tipte (type) veri döndüğünü inceleyelim.

# Çözüm 1:
def girdi_al(metin):
    """
    Gelen metne göre, kullanıcıdan girdi isteyen jenerik fonksiyon.
    Parametre: str tipinde istek metni
    Dönüş: Kullanıcının girdiği metni (str)
    """
    
    # önce kullanıcıdan bir girdi isteyelim
    girdi = input(metin)
    
    # şimdi aldğımız bu girdiyi geri dönelim -> return
    return girdi


# Şimdi tam sayı isteyen bir girdi alalım
sayi = girdi_al("Lütfen bir tamsayı giriniz: ")
print(sayi)

# Şimdi ay adını isteyen bir girdi alalım
ay = girdi_al("Lütfen bir ay adı giriniz: ")
print(ay)

# Son olarak, girdi_al fonksiyonun bize net tipte veri döndüğünü görelim
print(type(ay))

#-----------------------------------------------------------------------------------------------------#

# Soru 2:
# Soru 1'de yazdığımız jenerik girdi fonksiyonun bize sürekli metin (str) döndüğünü biliyoruz.
# Ama tamsayı istediğimiz durumlar da oldu.
# Şimdi yeni bir fonksiyon yazalım.
# Bu yeni fonksiyon, girdi_al fonksiyonun bize döndüğü değer üzerinden tam sayı olup olmadığını kontrol etsin ve bize tamsayı ise True değilse False dönsün.

# Çözüm 2:

def tamsayi_mi(girdi):
    """
    Gelen girdinin tam sayı olup olmadığını kontrol eder.
    Parametre: str tipinde girdi
    Dönüş: Tam sayı ise, True; değilse False
    """
    
    # gelen girdiye göre olasılıklar
    
    # olasılık 1: Kullanıcı metnin başında veya sonunda boşluk (space) bırakmış olabilir. Kaldıralım. -> str.strip()
    girdi = girdi.strip()
    
    # olaslık 2: Kullanıcı sayının başına +, - işareti koymuş olabilir. Bunları da kaldıralım. -> str.strip(<kesilecek_karakterler>)
    girdi = girdi.strip('+-')
    
    # Artık geriye kalan metnin tam sayı olup olmadığını kontrol edebiliriz -> isdigit()
    if girdi.isdigit():
        return True
    else:
        return False
    

# Şimdi tamsayı mı fonksiyonu test edelim
# önce bir girdi alalım
istek_metni = "Lütfen bir tamsayı giriniz : "
girdi = girdi_al(istek_metni)

# girdi tamsayı olup olmadığı karanını alalım
girdi_tam_sayi_mi = tamsayi_mi(girdi)   

# Bakalım girdi tam sayı mıymış?
print(girdi_tam_sayi_mi)

# tek seferde sayı alıp ekrana yazalım
print(tamsayi_mi(girdi_al("lütfen tam sayı giriniz : ")))


#-----------------------------------------------------------------------------------------------------#
#Soru 3:
# Soru 1 ve Soru 2'deki fonksiyonları kullanarak kullanıcıdan tamsayı alalım. Ve bu sayıyı dönelim.
# Soru 2 bize tamsayı almayı garantiler.
# Kullanıcı tamsayı girmemişse tekrar tekrar (recursive) soralım.

# Çözüm 3:

def tamsayi_al(metin):
    """
    Kullanıcıdan tamsayı alır. (inatçı)
    Parametre: str tipinde istek metni
    Dönüş: int tipinde girilen tipi
    """
    
    # kullanıcıdan girdi isteyelim
    girdi = girdi_al(metin)
    
    # girdi tam sayı mı kontrol et
    if tamsayi_mi(girdi):
        return int(girdi)
    else:
        # kullanıcıdan tam sayı gelmediğine göre tekrar sor.
        return tamsayi_al(metin)
    

sayi = tamsayi_al("tam sayı giriniz : ")
print(sayi)
#-----------------------------------------------------------------------------------------------------#
#Soru 4 :
# 1.yol
# Çözüm 4:

def haftanin_gunu():
    
    # kullanıcıdan gün numarası al
    gun_numarasi = tamsayi_al("Lütfen gün numarası giriniz (1-7 arasında): ")
    
    # Burada yapmamız gereken kontrol gelen sayının 1-7 arasında olmasıdır.
    if not 1 <= gun_numarasi <= 7:
        return "Geçersiz gün numarası. 1-7 arasında olmalı!"
    
    # 1-7  kontrolünü geçtiysek
    if gun_numarasi == 1:
        return "Pazartesi"
    elif gun_numarasi == 2:
        return 'Salı'
    elif gun_numarasi == 3:
        return 'Çarşmaba'
    elif gun_numarasi == 4:
        return 'Perşembe'
    elif gun_numarasi == 5:
        return 'Cuma'
    elif gun_numarasi == 6:
        return 'Cumartesi'
    else:
        return 'Pazar'
    
print(haftanin_gunu())  



# 2.yol 
def haftanin_gunu():
    sayi =  tamsayi_al("Lütfen gün numarası giriniz (1-7 arasında): ")
    gun = ""
    if sayi < 1 or sayi > 7:
        return haftanin_gunu()
    else :
        if sayi == 1:
            gun = "Pazartesi"
        elif sayi == 2 :
            gun = "Salı" 
        elif sayi == 3:
            gun = "Çaşamba"   
        elif sayi == 4 :
            gun = "Perşembe"   
        elif sayi == 5:
            gun = "Cuma"   
        elif sayi == 6:
            gun = "Cumartesi"   
        else:
            gun = "Pazar" 
    return gun     

print(haftanin_gunu())  

#-----------------------------------------------------------------------------------------------------#
#Soru 5:
# Çözüm 5:

def n(c):
    ustu = m(c, c)
    print(c, ustu)
    return ustu

def m(x, y):
    x = x + 2
    return x**y

def p(x, y, z):
    toplam = x + y + z
    kare = n(toplam)**2
    return kare

a = 1
b = a + 1
print(p(a, b+1, a+b)) 
# 7 4782969
# 22876792454961

# Stack Trace:
# Önce a değişkeni yaratılır ve değeri 1 olarak atanır, ardında b yaratılır ve değeri 2 olur.
                 # Print fonksiyonu p fonksiyonunu çağırır. -> p(1, 3, 3)
                 # p fonksiyonu parametrelerinin toplamı ile, n fonksiyonunu çağırır.
                 # m fonksiyonu aldığı x parametresine 2 ekler, ve x**y'yi geri döner
                 # n fonksiyonu, m'den dönen bu sonucu ustu değişkenine atar ve önce değişkenleri print eder -> print(c, ustu)
                 # n fonksiyonu, ardından ustu değişkenini p fonksiyonuna geri döner
                 # p fonksiyonu n'den aldığı değerin karesini alır ve bu kare değerini geri döner
                 # print fonksiyonu, p'den aldığı değeri ekrana yazar.


#-----------------------------------------------------------------------------------------------------#
#Soru 6:
# Adı aritmetik_ortalama olan bir fonksiyon tanımlayın.
# Bu fonksiyon değişken uzunlukta parametre alıyor alsın.
# Yani parametre sayısı önceden belli değil.
# Fonksiyonunuz aldığı bu parametrelerin aritmetik ortalamasını ekrana yazsın.

# Aritmetik Ortalama = Toplam / Eleman Sayısı

# Çözüm 6:
def aritmetik_ortalama(*args):
    
    # önce gelen parametrelerin toplamını alalım
    toplam = sum(args)
    eleman_sayisi = len(args)   # length -> len
    
    return toplam / eleman_sayisi

ortalama = aritmetik_ortalama(2, 5, 11)
print(ortalama)    

#-----------------------------------------------------------------------------------------------------#
#Soru 7:
# Dairenin alanını hesaplayan bir fonksiyon yazınız. Parametre olarak yarıçap alsın ve tüm fonksiyon tek satır olsun.
# 𝐷𝑎𝑖𝑟𝑒𝐴𝑙𝑎𝑛ı=𝜋∗𝑟**2

# Çözüm 7:
import math

def daire_alani(r):
    return math.pi * r**2

print(daire_alani(10))
#-----------------------------------------------------------------------------------------------------#
#Soru 8:
# Çemberin çevresini hesaplayan bir fonksiyon yazınız. Parametre olarak yarıçap 
# alsın ve tüm fonksiyon tek satır olsun.
# Ç𝑒𝑚𝑏𝑒𝑟Ç𝑒𝑣𝑟𝑒𝑠𝑖=2∗𝜋∗𝑟

# Çözüm 8:
import math
def cember_cevresi(r):
    """Çemberin cevresini döner."""
    return 2 * math.pi * r 

print(cember_cevresi(10))
#-----------------------------------------------------------------------------------------------------#
#Soru 9:
# Dikdörtgenin alanını hesaplayan bir fonksiyon yazınız. Parametre olarak kısa (a) ve
#  uzun kenarı (b) alsın ve tüm fonksiyon tek satır olsun.
# 𝐷𝑖𝑘𝑑ö𝑟𝑡𝑔𝑒𝑛𝐴𝑙𝑎𝑛ı=𝑎∗𝑏

# Çözüm 9:
def dikdortgen_alani(a, b):
    return a * b

print(dikdortgen_alani(5, 12))

#-----------------------------------------------------------------------------------------------------#
#Soru 10:
# Silindirin yüzey alanını hesaplayan bir fonksiyon yazın.
# Bu fonksiyon parametre olarak silindirin taban yarıçapını (r) ve yüksekliğini alsın.

# Silindir, üstünde ve altında daire olan, yan yüzeyi ise açılınca diktörtgen olan bir 
# şekildir.
# Alanları hesaplarken her işi yapan ayrı fonksiyonları kullanın

# Çözüm 10:

def silindir_alani(r, h):
    """
    Silindirin toplam yüzey alanını hesaplar.
    Parametreler:
        * r: int tipinde yarıçap
        * h: int tipinde yükseklik
    Dönüş: int tipinde silindirin alanı
    """
    
    # Önce dairelerin alanını hesaplayalım (2 adet var)
    daire = daire_alani(r)
    
    # Şimdi yan alanı hesaplayalım
    # yan alan, alt ve üst çemberler açılınca ortaya çıkan dikdörtgen
    # yan alan = cemberin cevresi * yukseklik
    
    cember = cember_cevresi(r)
    
    dikdortgen = dikdortgen_alani(cember, h)
    
    # toplam silindir alanını hesapla
    toplam_alan = 2 * daire + dikdortgen
    
    return toplam_alan

print(silindir_alani(10, 2))


#-----------------------------------------------------------------------------------------------------#






#-----------------------------------------------------------------------------------------------------#