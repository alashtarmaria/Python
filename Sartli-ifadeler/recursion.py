#### Recursion - Kendi Kendini Çağırmak

# Bir fonksiyon başka fonksiyonları çağırabildiği gibi, kendisini de çağırabilir.

# Buna Recursion adı verilir.

# Ör: Verilen bir sayıdan geriye doğru, 0'a kadar sayan bir fonksiyon.

# Önemli Not: Recursion'larda durma koşulu çok önemlidir. Eğer fonksiyon nerede duracağını bilemezse, sonsuz döngüye girer.



#---------------------------------------------------#
# Örnek : 
def geri_say(n):
    
    # ilk önce durma koşulunu yazmamız lazım
    if n <= 0:
        print("------ Program Sonu ------")
    else:
        print(n)
        geri_say(n-1)

geri_say(5)
#---------------------------------------------------#
# Örnek : 
#Şimdi kendisine verilen bir metni, geriye doğru sayarak yazan bir fonksiyon tanımlayalım.def metni_yaz(metin, n):
    
def metni_yaz(metin, n):
    
    # önce durma koşulu
    if n <= 0:
        return
    else:
        print(metin)
        metni_yaz(metin, n-1)



metni_yaz("Machine Learning", 5)        

#---------------------------------------------------#
# Örnek : 
# Şimdi gelen sayıyı da yazdıralım

def metni_yaz(metin, n):
    
    # önce durma koşulu
    if n <= 0:
        return
    else:
        print("{0} : {1}".format(n, metin))
        metni_yaz(metin, n-1)

metni_yaz("Machine Learning", 5)    

#---------------------------------------------------#
# Şimdi diyelim ki, durma koşulu koymadınız veya koşulunuz yanlış. -> Hiç durmaz (sonsuz döngü)

# RecursionError

#---------------------------------------------------#

#---------------------------------------------------#
# Örnek : 
# girilen sayıdan 100'e kadar olan sayıları yazalım

def yuze_kadar_say(n):
    
    # durma koşulu yok
    
    print(n)
    yuze_kadar_say(n + 1)


#yuze_kadar_say(80)

#---------------------------------------------------#

# Örnek : 
# recursion'ı düzgün yazsaydık

def yuze_kadar_say(n):
    
    # durma koşulu yok
    if n > 100:
        return
    else:
        print(n)
        yuze_kadar_say(n + 1)

yuze_kadar_say(80)

#---------------------------------------------------#
