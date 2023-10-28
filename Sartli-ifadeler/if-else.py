#----------------------------------------------------------------------------------------------------------------------------#

# **Alternatif İşleme:**
# **else**
# Çoğu zaman bir koşul yerine geldiği ya da gelmediği zaman bunun alternatifleri lazım olur.
# Bu durumlar için **if** bloğundan sonra **else** bloğu çalışıtırılır

#--------------------------------------------------------------------#
# Örnek :
# Eğer x sayısı çift sayı ise, ekrana 'ÇİFT' yazsın
# Değilse, ekrana 'TEK' yazsın
# Çift olma koşulu: 2'ye tam bölünüyorsa (% mod operatörü)
x = 14

print("---- if bloğu öncesi ----")

if x % 2 == 0:
    print("ÇİFT")
else:
    print("TEK")
    
print("---- if bloğu sonrası ----")


#--------------------------------------------#
# elif
# Yukarıda sadece 2 durum kontrol ettik:
# if
# else
# Ama çoğu zaman ikiden fazla durum lazım olur.
# Bunun için if-elif-...-else bloğu kullanılır.
# elif: elseif

#--------------------------------------------#

#--------------------------------------------------------------------#

# Örnek :
# kullanıcıdan bir sayı isteyelim
# bu sayının, POZİTİF, NÖTR ya da NEGATİF olma durumunu kontrol edelim

def pozitif_mi():
    
    # input() fonksiyonun str döner. 
    girdi = input("Lütfen bir sayı giriniz: ")
    
    # girdiyi -> integer (int) yapalım
    n = int(girdi)
    
    # koşulları kontrol et
    if n > 0:
        print("POZİTİF")
    elif n == 0:
        print("NÖTR")
    else:
        print("NEGATİF")

pozitif_mi()

#--------------------------------------------------------------------#

# Örnek :
# Şimdi kullanıcıdan 1-7 arasında bir sayı isteyen bir fonksiyon yazalım.
# Fonksiyonumuz, bu sayıya göre haftanın hangi günü olduğuna karar verip, kullanıcıya dönsün. (return)

def haftanin_gunleri():
    
    # kullanıcıdan bir gün numarası isteyelim
    gun_numarasi = int(input("Lütfen bir gün numarası giriniz. (1-7 arasında): "))
    
    # fonksiyonun sonunda geri döneceğimiz gün adını tutan bir değişken tanımlayalım
    gun_adi = ""
    
    # kontrol et
    if gun_numarasi == 1:
        gun_adi = "PAZARTESİ"
    elif gun_numarasi == 2:
        gun_adi = 'SALI'
    elif gun_numarasi == 3:
        gun_adi = 'ÇARŞAMBA'
    elif gun_numarasi == 4:
        gun_adi = 'PERŞEMBE'
    elif gun_numarasi == 5:
        gun_adi = 'CUMA'
    elif gun_numarasi == 6:
        gun_adi = 'CUMARTESİ'
    else:
        gun_adi = 'PAZAR'
        
    # gun_adi'ni geri dön -> return
    return gun_adi
    
# şimdi çağıralım
print(haftanin_gunleri())   


#--------------------------------------------------------------------#

# Haftanın günleri fonksiyonumuz güzel çalışıyor ama sorunları var:
# 1- Ya kullanıcı sayı yerine bir harf girse?
# 2- Ya kullanıcı haftanın gün sayısı olan 7'den büyük bir sayı girerse ne olur?
# 3- Ya kullanıcı 1'den küçük bir sayı girerse ne olur?

#--------------------------------------------------------------------#

def haftanin_gunleri():
    
    # kullanıcıdan bir gün numarası isteyelim
    # direk aldığımız değeri int olarak çeviremeyiz (cast edemeyiz)
    # önce kontrol etmemiz lazım
    girdi = input("Lütfen bir gün numarası giriniz. (1-7 arasında): ")
    
    # KONTROL 1: TAM SAYI KONTROLÜ
    # girdi'nin tam sayı (int) olmasını istiyoruz
    # o zaman int kontrolü yapmamız lazım -> isdigit()
    if girdi.isdigit():
        gun_numarasi = int(girdi)
    else:
        print("Lütfen tam sayı giriniz.")
        # girdi hatalı olduğuna göre programı sonlandırmamız lazım -> return
        return
    
    print("------ 1. KONTROL BAŞARILI ------")
    
    # KONTROL 2: SAYININ 1-7 ARASINDA OLMA KONTROLÜ
    # Bu noktaya gelmişsek -> 1. Kontrol başarılıdır. Ve gün numarası gelmiştir
    
    if gun_numarasi < 1 or gun_numarasi > 7:
        print("Lütfen 1 ile 7 arasında bir sayı giriniz.") 
        return
    
    print("------ 2. KONTROL BAŞARILI ------")
    
    # sonunda ekrana yazacağımız gun adını tutacak değişkeni tanımalayabilirim
    gun_adi = ""
    
    # kontrol et
    if gun_numarasi == 1:
        gun_adi = "PAZARTESİ"
    elif gun_numarasi == 2:
        gun_adi = 'SALI'
    elif gun_numarasi == 3:
        gun_adi = 'ÇARŞAMBA'
    elif gun_numarasi == 4:
        gun_adi = 'PERŞEMBE'
    elif gun_numarasi == 5:
        gun_adi = 'CUMA'
    elif gun_numarasi == 6:
        gun_adi = 'CUMARTESİ'
    else:
        gun_adi = 'PAZAR'
        
    # gun_adi'ni geri dön -> return
    return gun_adi


# şimdi çağıralım
haftanin_gunleri()
