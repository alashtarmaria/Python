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
#Soru :
#-----------------------------------------------------------------------------------------------------#
#Soru :
#-----------------------------------------------------------------------------------------------------#
#Soru :
#-----------------------------------------------------------------------------------------------------#
#Soru :
#-----------------------------------------------------------------------------------------------------#
#Soru :
#-----------------------------------------------------------------------------------------------------#
#Soru :
#-----------------------------------------------------------------------------------------------------#
#Soru :
#-----------------------------------------------------------------------------------------------------#
#Soru :
#-----------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------#


#-----------------------------------------------------------------------------------------------------#