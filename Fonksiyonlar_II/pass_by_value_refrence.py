#----------------------------------------------------------------------------#
#### Pass by Value, Pass by Reference

# Immutable ve Mutable yapılarını öğrendiğimize göre, 
# şimdi bu tiplerdeki nesnelerin bir fonksiyona parametre olarak geçtiğinde ne olacağını göreceğiz.,


# Ana Kural:
#################################
# **Immutable -> Pass by Value:**
# * Eğer Immutable bir nesne, bir fonksiyona parametre olarak geçerse,  **sadece kopyası** geçer.
# Kendisi olduğu yerde hiç değişmeden kalır.

   
#################################
# **Mutable -> Pass by Reference:**
# * Eğer Mutable bir nesne, bir fonksiyona parametre olarak geçerse, **referansı** geçer. 
# Yani bellekteki adresi geçer. Yani, eğer fonksiyon içinde bu değişken değişirse,  orjinal değişken değişmiş olur.


#--------------------------------------#
# Örnek:

# Immutable
# str
dil = "Python"

print("Fonksiyona Parametre olarak geçmeden önce:", dil)

def degistir(ad):
    ad = 'Java'
    
# fonksiyonu çağıralım ve dil parametremizi verelim
degistir(dil)

print("Fonksiyona Parametre olarak geçtikten sonra:", dil)

#--------------------------------------#
# Immutable olan `str` tipi, fonksiyona parametre olarak geçti ve değişmeden kaldı.
# Çünkü str'ler Immutable'dır. Imuutable olan tiplerin kendisi değil, kopyası fonksiyona geçer.
#--------------------------------------#

#--------------------------------------#
# Örnek:
# Immutable 
# int

sayi = 45

print("Fonksiyona Parametre olarak geçmeden önce:", sayi)

def degistir(sayi):
    sayi = 0
    
# fonksiyonu çağıralım ve dil parametremizi verelim
degistir(sayi)

print("Fonksiyona Parametre olarak geçtikten sonra:", sayi)

#--------------------------------------#
# `int` tipi de Immutable olduğu için, fonksiyona kopyası geçti -> **Pass by Value**

#-----------------------------------------#
#-----------------------------------------#
# Örnek:

# Mutable
# list

sayilar = [1, 2, 3, 4, 5]

print("Fonksiyona Parametre olarak geçmeden önce:", sayilar)

def degistir(dizi):
    dizi[0] = 'a'
    dizi[1] = 'b'
    
# fonksiyonu çağıralım ve dil parametremizi verelim
degistir(sayilar)

print("Fonksiyona Parametre olarak geçtikten sonra:", sayilar)

# Bakın, sayilar listesi `list` tipinde olduğu için ve List'ler **Mutable** oldukları için:
# fonksiyon içindeki değişiklik, orjinal listeyi de değiştirdi: -> **Pass by Reference**
