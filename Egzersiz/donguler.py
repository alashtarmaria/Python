# Soru 1:
# Ekrana yıldızlardan oluşmuş bir kare çizen bir fonksiyon yazın.
# Fonksiyon parametre olarak karenin bir kenarında bulunan yıldız sayısını alsın.
# Diyelim ki kullanıcı 5 olarak girdi sayıyı, o zaman karenin 5 satırı ve her satırda 5 sütunu (yıldız) olur.
# Bunun için iç içe while döngüleri kullananın.

# Çözüm 1:
def kare_yildiz_while(n):
    i = 0

    yildiz = ""

    while i < n:
        yildiz = ""
        
        j = 0
        while j < n:
            yildiz +=" * "
            j+=1
            
        print(yildiz)
          
        i+=1

        
        
n = int(input("Yıldız sayısı giriniz:"))
kare_yildiz_while(n)
    
##########################################################
# Soru 2:
# Ekrana yıldızlardan oluşmuş bir kare çizen bir fonksiyon yazın.
# Fonksiyon parametre olarak karenin bir kenarında bulunan yıldız sayısını alsın.
# Diyelim ki kullanıcı 5 olarak girdi sayıyı, o zaman karenin 5 satırı ve her satırda 5 sütunu (yıldız) olur.
# Bunun için iç içe for döngüleri kullananın.
# Çözüm 2:
def kare_yildiz_for(n):
    for i in range(n):
        yildiz=""
        for j in range(n):
            yildiz+=" * "
        print(yildiz)    

n = int(input("Yıldız sayısı giriniz:"))
kare_yildiz_for(n)   
##########################################################

# Soru 3:
# Ekrana yıldızlardan oluşmuş bir ikizkenar dik üçgen çizen bir fonksiyon yazın.
# Fonksiyon parametre olarak üçgenin dik bir kenarında bulunan yıldız sayısını alsın.
# Diyelim ki kullanıcı 5 olarak girdi sayıyı, o zaman üçgen şu şekilde olur.
# Çözüm 3:

def ucgen_while(n):
    i = 0
    yildiz =""
    while i < n :
        yildiz =""
        j=0
        while j < n :
            yildiz+="* "
            j+=1
            
            print(yildiz)
            i+=1

            
ucgen_while(5)

##########################################################
# Soru 4:
# Ekrana yıldızlardan oluşmuş bir ikizkenar dik üçgen çizen bir fonksiyon yazın.
# Fonksiyon parametre olarak üçgenin dik bir kenarında bulunan yıldız sayısını alsın.
# Diyelim ki kullanıcı 5 olarak girdi sayıyı, o zaman üçgen şu şekilde olur.
# Çözüm 4:
def ucgen_for(n):
    for i in range(n):
        yildiz=""
        for j in range(i+1):
            yildiz += "* "
            
        print(yildiz)


            
ucgen_for(5)

##########################################################
# Soru 5:

# Ekrana yıldızlardan oluşmuş ters bir ikizkenar dik üçgen çizen bir fonksiyon yazın.
# Fonksiyon parametre olarak üçgenin dik bir kenarında bulunan yıldız sayısını alsın.
# Diyelim ki kullanıcı 5 olarak girdi sayıyı, o zaman üçgen şu şekilde olur.
          # * * * * *
          # * * * *
          # * * *
          # * * 
          # * 
# Bunun için iç içe for döngüleri kullananın.
# Çözüm 5:
def ters_ucgen_for(n):
    for i in range(n,0,-1):
        yildiz=""
        for j in range(i):
            yildiz += "* "
            
        print(yildiz)

            
ters_ucgen_for(5)

##########################################################
# Soru 6:

# Ekrana yıldızlardan oluşmuş bir ikizkenar üçgen çizen bir fonksiyon yazın.
# Fonksiyon parametre olarak bir sütundaki yıldız sayısını alsın.
# Diyelim ki kullanıcı 5 olarak girdi sayıyı, o zaman üçgen şu şekilde olur.          
           # *
           # * *
           # * * *
           # * * * * 
           # * * * * *
           # * * * *
           # * * *
           # * *
           # *
# Bunun için iç içe for döngüleri kullananın.

# Çözüm 6:

def ikizkenar_ucgen_for(n):
    for i in range(n):
        yildiz =""
        for j in range(i+1):
            yildiz+="* "
        print(yildiz)
    
    for i in range(n,0,-1):
        yildiz =""
        for j in range(i):
            yildiz+="* "
        print(yildiz)
            
            
ikizkenar_ucgen_for(5)   


# Ama yukarıdaki fonksiyonun sonucunda bir sorun var. Ortadaki satır iki kere yazılmış yani kendini tekrar etmiş.
# Bunun sebebi hem ucgen_for() hem de ters_ucgen_for() fonksiyonlarının ikisinde de aynı sayırın olması. 
# Birinden kaldırırsak sorun çözülür.
def ikizkenar_ucgen_for(n):
    for i in range(n):
        yildiz =""
        for j in range(i+1):
            yildiz+="* "
        print(yildiz)
    
    for i in range(n,0,-1):
        yildiz =""
        for j in range(i-1):
            yildiz+="* "
        print(yildiz)
            
            
ikizkenar_ucgen_for(5)



def ikizkenar_ucgen_for(n):
    
    # üstteki üçgen
    ucgen_for(n-1)
    
    # alltaki üçgen
    ters_ucgen_for(n)

##########################################################
# Soru 7:
# Parametre olarak kendisine verilen bir sayının asal sayı olup olmadığını dönen bool bir fonksiyon yazın.
# Sayı asal ise True, asal değilse False dönecek
# Çözüm 7:

# Çözüm 7:

def asal_mi(n):
    asal =True
    
    for i in range(2 ,n ):
        if n % i ==0:
            asal= False
        
    return asal
        

asal_mi(40)     
##########################################################
# Soru 8:
# Parametre olarak kendisine verilen bir sayının bütün asal çarpanlarını bulan bir fonksiyon yazın.
# Çözüm 8:

def asal_carpanlar(n):
    for i in range(2,n):
        if n % i == 0:
            if asal_mi(i) :
                print(i)


        
        
asal_carpanlar(24)


##########################################################
# Soru 9:
# 1'den 50'ye (ikisi de dahil) kadar olan sayılar üzerinde dönen bir fonksiyon yazın.
# 3'ün katları için sayının kendisi yerine "Üj"
# 5'in katları için sayının kendisi yerine "Bej"
# 3 ve 5'in ortak katları için ise sayının kendisi yerine "ÜjBej" yazsın.

# Çözüm 9:

# bu fonksiyonda büyükten küçüğe gideceğiz
# önce hem 3 hem de 5'e bölünürse
# ardından ayrı ayrı 3 ve 5'e bölünürmü diye bakıcaz

def ujbej():
    
    uj = "Üj"
    bej = "Bej"
    
    for i in range(1, 51):
        
        # hem 3 hem de 5
        if i % 3 == 0 and i % 5 == 0:
            print(uj+bej)
        elif i % 3 == 0:
            print(uj)
        elif i % 5 == 0:
            print(bej)
        else:
            print(i)


##########################################################            
# Soru 10:
# Girilen bir cümleyi önce kelimelerine ayıran, sonra da bu kelimelerdeki harflerin arasına '-' (tire) karakteri koyan bir fonksiyon yazın.
# Daha sonra kelimeleri de '__' (iki alt tire) karakteri ile birleştirsin.
# Ve birleşmiş yeni cümleyi kullanıcıya dönsün.
# Cümleyi kelimelere parçalamak için split() fonksiyonunu kullanınız

# Çözüm 10:

def cumle_birlestir(cumle):
    
    kelimeler = cumle.split()  # split() -> boşluk karakterinden keser
    
    # birleşmiş cümleyi tutan değişken
    birlesmis_cumle = ""
    
    # döngü 1 -> kelimeler üzerinde dön
    for kelime_index, kelime in enumerate(kelimeler):
        
        # print(kelime)
        
        # birleşmiş kelimeyi tuttuğumuz değişken tanımla
        birlesmis_kelime = ""
        
        # döngü 2: kelime içindeki harflerde döner
        for harf_index, harf in enumerate(kelime):
            # print(harf)
            
            # harf'i ekle
            birlesmis_kelime += harf
            
            # tire '-' ekle -> sonuncusuna ekleme
            if harf_index < len(kelime) - 1:
                birlesmis_kelime += "-"
    
        # print(birlesmis_kelime)
        
        # birleşmiş kelimeyi -> birleşmiş cümleye ekle
        birlesmis_cumle += birlesmis_kelime
        
        # son kelime değilse -> __ ekle
        if kelime_index < len(kelimeler) - 1:
            birlesmis_cumle += "__"
        
    return birlesmis_cumle


cumle = "Bu oldukça kısa bir cümledir."
birlesmis_cumle = cumle_birlestir(cumle)
print(birlesmis_cumle)






























































# # Örnek :
# # koduyla ilgili aşağıdakilerden hangisi doğrudur?
# sonuc=1

# for i in range(4):

#     sonuc*=3

# print(sonuc)
# # for döngüsünde yer alan i, her iterasyonda 3 ile çarpılır.
# # i döngü içerisinde hesaba katılmaz. --> doğru cevap



# i=0
# while(i<10):
#     if(i==3 or i==5):
#         continue
#     print("i: ",i)
#     i=i+1


