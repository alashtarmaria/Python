#-------------------------------------------------------------------------------#
## İç-İçe (Nested) Şartlı İfadeler

# not Operatörü
# Bir yargıyı, (True veya False) tersine çevirmek için kullanılır.
# değilse gibi okunabil

#---------------------------------------------------#
# Örnek : 
# normal if kullanımı
x = 5
if x == 5:
    print("x 5'e eşittir.")
else:
    print("x 5'e eşit değildir.")


#---------------------------------------------------#
# Örnek : 
# not ile if kullanımı
x = 5
if not x == 5:
    print("x 5'e eşit değildir.")
else:
    print("x 5'e eşittir.")   

#---------------------------------------------------#

# Önemli Not: if'ler içeri girmek için True'ya ihtiyaç duyar.
# if True:
#     ......
#     ......

#---------------------------------------------------#

# Diyelim ki, bir koşul sağlandıktan sonra, o koşul içinde başka bir koşula bakmamız lazım.
# Bunun için içeride, tekrar bir koşul yapısı kurmanız lazım
# İç-İçe Koşul Yapısıdır (Nested)
# #---------------------------------------------------#

#---------------------------------------------------#
# Örnek : 
x = 300
y = 30

if x == y:
    print("x ile y aynı.")
else:
    
    if x > y:
        print("x y'den büyüktür.")
    elif x == y:
        print("x ile y aynı.")
    else:
        print("x y'den küçüktür.")
    


#---------------------------------------------------#
# Örnek : 
x = 10
y = 30

if x == y:
    print("x ile y aynı.")
else:
    
    if x > y:
        print("x y'den büyüktür.")
        
    # gereksiz kod -> redundant
    # elif x == y:
        # print("x ile y aynı.")
        
    else:
        print("x y'den küçüktür.")

#---------------------------------------------------#
# Örnek : 
# kullanıcıdan bir sayı isteyelim
# bu sayı 10'dan küçükse:
    # tek ise -> 10'dan KÜÇÜK - TEK
    # çift ise -> 10'dan KÜÇÜK - ÇİFT
    
# sayı 10'dan büyükse
    # tek -> TEK
    # çift -> ÇİFT
    
def sayi_tek_mi():
    
    # kullanıcıdan bir sayı iste
    girdi = input("Lütfen bir sayı giriniz: ")
    
    # input() -> str (metin) döner -> int'e cast etmeniz lazım
    sayi = int(girdi)
    
    # koşulları kontrol et
    if sayi < 10:
        
        # sayi tek mi çift mi?
        if sayi % 2 == 1:
            print("10'dan KÜÇÜK - TEK")
        else:
            print("10'dan KÜÇÜK - ÇİFT")
            
    else:
        # sayi tek mi çift mi?
        if sayi % 2 == 1:
            print("TEK")
        else:
            print("ÇİFT")

sayi_tek_mi()   

