#####################################################################################################
#-----------------------------------------  #
# Soru 1:
# Kullanıcı tarafından girilen bir saynının tek mi çift mi olduğunu bulun.
#-----------------------------------------
# 1.yol 
def tek_mi_cift_mi():
    n = int(input("Lütfen bir sayı giriniz : "))
    if n % 2 ==0 :
        print("Çift")
    else :
        print("Tek")    

# çağıralım 
tek_mi_cift_mi()

#-----------------------------------------  #
# 2.yol 
# kullanıcıdan değer al
sayi = int(input("Lütfen bir sayı giriniz: "))

# sonra if-else yapısı ile karar verelim
if sayi % 2 == 0:
    print(sayi, "çift.")
else:
    print(sayi, "tek.")

#-----------------------------------------  #
#####################################################################################################
#-----------------------------------------  #
# Soru 2:
# Kullanıcı tarafından girilen bir harfin sesli mi yoksa sessiz mi olduğunu bulalım.
#-----------------------------------------  #
# 1.yol 
def sesli_sessiz_mi():
    harf = input("Lütfen bir harf giriniz: ")
    if harf == "i":
        print("Sesli harf")
    elif harf == "ı":
        print("Sesli harf")
    elif harf == "ü":
        print("Sesli harf")
    elif harf == "o":
        print("Sesli harf")
    elif harf == "ö":
        print("Sesli harf")
    elif harf == "u":
        print("Sesli harf")
    elif harf == "e":
        print("Sesli harf")
    elif harf == "a":
        print("Sesli harf")   
    else :
         print("Sesiz harf")   

    
sesli_sessiz_mi()
#-----------------------------------------  #
# 2.yol 
# önce bir harf isteyelim
harf = input("Lütfen bir harf giriniz: ")
if harf == "a" or harf == "e" or harf == 'i' or harf == 'ı' or harf == 'o' or harf == 'ö' or harf == 'u' or harf == 'ü':
    print("SESLİ HARF", harf)
else:
    print("SESSİZ HARF", harf)

#-----------------------------------------  #
#####################################################################################################
#-----------------------------------------  #
# Soru 3:
# Kullanıcı tarafından girilen kenar sayısına göre hangi şekil olduğnu dönen bir fonksiyon yazın.
#-----------------------------------------  #
# 1.yol 
def hangi_sekil():
    """
    Kullanıcıdan bir sayı alır, ve o sayıya karşılık gelen şeklin adını döner.
    Parametre: yok
    Dönüş: str tipinde sekil_adi -> şeklin adı
    """
    
    # önce kullanıcıdan bir sayı al
    kenar_sayisi = int(input("Lütfen Kenar Sayısını girin: "))
    
    # şeklin adını tutan değişken tanımla
    sekil_adi = ""
    
    if kenar_sayisi == 3:
        sekil_adi = 'ÜÇGEN'
    elif kenar_sayisi == 4:
        sekil_adi = 'DÖRTGEN'
    elif kenar_sayisi == 5:
        sekil_adi = 'BEŞGEN'
    elif kenar_sayisi == 6:
        sekil_adi = 'ALTIGEN'
    else:
        sekil_adi = 'ÇOKGEN'
    
    return sekil_adi

# şimdi çağıralım 
sekil_adi = hangi_sekil()
print(sekil_adi)
#-----------------------------------------  #
#####################################################################################################
#-----------------------------------------  #
# Soru 4:
# Bir aydaki gün sayısını ekrana yazdırın. Ay'ın adını kullanıcı belirleyecek.
#-----------------------------------------  #
# Çözüm 4:

def ay_icindeki_gun_sayisi():
    
    # gün sayısını tutan değişken
    gun = 31
    
    # kullanıcıdan ay adını alalım
    ay = input("Lütfen ay adı giriniz: ")
    
    # Şimdi 28-29, 30 ve 31 gün olan aylar var
    if ay == 'Nisan' or ay == 'Temmuz' or \
       ay ==  'Eylül' or ay == 'Kasım':
        gun = 30
    elif ay == 'Şubat':
        gun = "28 ya da 29"
        
    return str(ay) + " ayı içinde " + str(gun) + " gün vardır."


# şimdi çağıralım 
ay_adi =ay_icindeki_gun_sayisi()
print(ay_adi)
#-----------------------------------------  #
#####################################################################################################
#----------------------------------------- #
# Soru 5:
# Kenar uzunlukları verilen bir üçgenin adını ekrana yazan bir fonksiyon oluşturalım.
#----------------------------------------- #
# Çözüm 5:

def ucgenin_adi():
    
    # üçgenin adını tutan değişken
    ad = ""
    
    # önce 3 kenarı da kullanıcıdan istiyelim
    kenar_1 = float(input("Birinci kenar uzunluğunu giriniz:"))
    kenar_2 = float(input("İkinci kenar uzunluğunu giriniz:"))
    kenar_3 = float(input("Üçüncü kenar uzunluğunu giriniz:"))
    
    # şimdi olasılıklara göre karar verelim
    if kenar_1 == kenar_2 and kenar_2 == kenar_3:
        ad = 'Eşkenar Üçgen'
    elif kenar_1 == kenar_2 or kenar_1 == kenar_3 or kenar_2 == kenar_3:
        ad = 'İkizkenar Üçgen'
    else:
        ad = 'Çeşitkenar Üçgen'
        
    return ad

# şimdi çağıralım 
print(ucgenin_adi())

#----------------------------------------- #
#####################################################################################################
#----------------------------------------- #
# Soru 6:        
# Ay ve Güne göre hangi meyvenin yeneceğini bilen bir fonksiyon yazalım.
        # İlkbahar: Erik
        # Yaz: Karpuz
        # Sonbahar: Ayva
        # Kış: Portakal
#----------------------------------------- #
# Çözüm 6:

def hangi_meyve_yenir():
    
    # önce ay ve günü alalım
    ay = input("Ay adını giriniz: ")
    gun = int(input("Gün numarasını giriniz: "))
    
    # meyveye karar verelim
    if ay == 'Ocak' or ay =='Şubat':
        meyve = 'Portakal'
    elif ay == 'Mart':
        if gun < 20: # 21 Mart
            meyve = 'Portakal'
        else:
            meyve = 'Erik'
    elif ay == 'Nisan' or ay == 'Mayıs':
        meyve = 'Erik'
    elif ay == 'Haziran':
        if gun < 20: # 21 Haziran
            meyve = 'Erik'
        else:
            meyve = 'Karpuz'
    elif ay == 'Temmuz' or ay == 'Ağustos':
        meyve = 'Karpuz'
    elif ay == 'Eylül':
        if gun < 22: # 23 Eylül
            meyve = 'Karpuz'
        else:
            meyve = 'Ayva'
    elif ay == 'Ekim' or ay == 'Kasım':
        meyve = 'Ayva'
    elif ay == 'Aralık':
        if gun < 21: # 21 Aralık
            meye = 'Ayva'
        else:
            meyve = 'Portakal'
        
    print(ay, "ayının", gun, ". günü", meyve, "meyvesi yenir.")


# şimdi çağıralım 
hangi_meyve_yenir()

#----------------------------------------- #
#####################################################################################################
#-----------------------------------------  #
# Soru 7:
# Kullanıcıdan C, Ç, P, S harflerinden birini isteyen bir fonksiyon yazalım.

# Bu harfler haftanın günlerinin başlangıcı olsun. Gelen harfe göre hangi gün olduğunu tahmin etmeye çalışalım.

# Harflere göre ek sorular:

# C: "hafta içi mi" yoksa "hafta sonu mu"
# P: "hafta içi mi" yoksa "hafta sonu mu"
# hafta içi: "hafta başı mı" yoksa "hafta ortası mı"
#-----------------------------------------  #
# Çözüm 7:

def hangi_gun():
    
    # önce harfi alalım
    harf = input("Lütfen C, Ç, P, S harflerinden birini giriniz: ")
    
    # Eğer girilin harf bunlardan biri değilse, hata dönelim
    if not (harf == 'C' or harf == 'Ç' or harf == 'P' or harf == 'S'):
        print("Yanlış harf girdiniz.", harf, "harfi: C, Ç, P, S içinde değil.")
        
    # eğer bu harflerden biri ise
    else:
        
        # Gün bazlı kontroller
        # S
        if harf == 'S':
            gun = 'SALI'
            
        # Ç
        elif harf == 'Ç':
            gun = 'ÇARŞAMBA'
            
        # C
        elif harf == 'C':
            # C harfinden iki gün olduğu için hafta içi mi haft dışı mı sormamız lazım
            hafta_ici = input("Seçtiğiniz gün hafta içi mi? Evet - Hayır?")
            
            if hafta_ici == 'Evet':
                gun = 'CUMA'
            else:
                gun = 'CUMARTESİ'
                
        # P
        elif harf == 'P':
            # P harfi ile başlayan 3 gün var -> hafta içi/sonu -> hafta başı/ortası
            hafta_sonu = input("Seçtiğiniz gün hafta sonu mu? Evet - Hayır?")
            
            if hafta_sonu == 'Evet':
                gun = 'PAZAR'
                
            else:
                hafta_basi = input("Seçtiğiniz gün hafta başı mı? Evet - Hayır?")
    
                if hafta_basi == 'Evet':
                    gun = 'PAZARTESİ'
                else:
                    gun = 'PERŞEMBE'
        
        print("Seçtiğiniz gün:", gun)
    
# şimdi çağıralım 
hangi_gun()

#-----------------------------------------  #
#####################################################################################################
#-----------------------------------------  #
# Soru 8:
# Kullanıcıdan pozitif bir sayı isteyelim. Girdinin gerçekten tamsayı olup olmadığını kontrol edelim. Ek olarak tam sayı ise bunun pozitif olup olmadığını da kontrol edelim.

# Bu sayının tek-çift olmasına göre TUHAF mı TUHAF DEĞİL mi, buna karar verelim.

# Eğer sayı tek sayı ise TUHAF
# Eğer sayı çift ama 1 - 10 (ikisi de dahil) arasında ise TUHAF DEĞİL
# Eğer sayı çift ama 11 - 20 (ikisi de dahil) arasında ise TUHAF
# Eğer sayı çift ama 20 den büyükse TUHAF DEĞİL
#-----------------------------------------  #
# Çözüm 8:
def tuhaf_mi():
    
    # sayi isteyelim -> str
    n = input("Bir sayı girin, size tuhaf mı değil mi, söyleyeyim: ")
    
    # girilen sayi tam sayı mı?
    if not n.isdigit():
        print("TUHAF! Çünkü sayı girmediniz.")
        return
    
    # sayı olduğuna göre -> int'e çevirebiliriz
    n = int(n)

    # Pozitif kontrolü
    if n <= 0:
        print("TUHAF! Çünkü sayı POZİTİF değil.")
        return
    
    # sayı pozitif
    else:
        
        # tek mi
        if n % 2 == 1:
            print("TUHAF - Tek")
            
        # çift
        else:
            # 1-10 arasında mı
            if 1 <= n <= 10:
                print("TUHAF DEĞİL - 1-10 Arasında")
            elif 11 <= n <= 20:
                print("TUHAF - 11-20 Arasında")
            elif n > 20:
                print("TUHAF DEĞİL - 20 den büyük")


# şimdi çağıralım 
tuhaf_mi()    
#-----------------------------------------  #
#####################################################################################################
#-----------------------------------------  #
# Soru 9:
# TEK-ÇİFT Toplamlar Kuralı:
# İki sayının toplamı Tek ise sayılardan sadece biri Tek'tir.
# İki sayının toplamı Çift ise sayıların ikisi Tek ya da ikisi Çift'tir.
# Kullanıcıdan iki sayı isteyip Tek-Çift Toplamlar Kuralına göre toplamın Tek mi yoksa Çift mi olduğunu bulan bir fonksiyon yazın.

# Önemli: Bu soruyu x + y diyerek, direk toplam değeri üzerinden yapmayınız.
#-----------------------------------------  #
# Çözüm 9:

def tek_cift_toplamlar_kurali():
    
    # sayıları alalım
    n1 = int(input("Birinci sayı: "))
    n2 = int(input("İkinci sayı: "))
    
    # sadece biri tek ise -> sonuç TEK
    # (n1 tek ve n2 çift) veya (n1 çift ve n2 tek)
    if (n1 % 2 == 1 and n2 % 2 == 0) or (n1 % 2 == 0 and n2 % 2 == 1):
        print("Toplam: TEK")
    # bunun dışındaki bütün durumlarda (case'lerde) -> sonuç ÇİFT
    else:
        print("Toplam: ÇİFT")
        
# şimdi çağıralım 
tek_cift_toplamlar_kurali()
#-----------------------------------------  #
#####################################################################################################
#-----------------------------------------  #
# Soru 10:
# Kullanıcıdan iki sayı alalım. Bu sayılardan hangisinin küçük, hangisinin büyük olduğunu bulalım.

# Sonra büyük sayıdan geriye gidip, küçük sayıya kadar olan sayıları ekrana yazalım.

# Önemli: Recursion ile yapınız.
#-----------------------------------------  #
# Çözüm 10:
   
def geri_cift_say():
    
    # önce iki sayı alsın
    sayi1 = int(input("Birinici Sayı: "))
    sayi2 = int(input("İkinci Sayı: "))
    
    # küçük ve büyük sayıyı tutan değişkenler
    kucuk = 0
    buyuk = 0
    
    if sayi1 <= sayi2:
        kucuk = sayi1
        buyuk = sayi2
    else:
        kucuk = sayi2
        buyuk = sayi1
        
    print("küçük:", kucuk)
    print("büyük:", buyuk)
    
    geri_yaz(kucuk, buyuk)
    

# recursion fonksiyonu tanımla

def geri_yaz(bitis, deger):
    
    # durma koşulu
    if deger == bitis:
        print(deger)
        return
    
    else:
        print(deger)
        geri_yaz(bitis, deger - 1)

# şimdi çağıralım 
geri_cift_say()
#-----------------------------------------  #
#####################################################################################################



