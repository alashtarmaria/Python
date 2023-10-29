# For Döngüsü
# range() -> artış : negatif değer geri gelir
# range(başlangıç, bitiş, -artış)


#-------------------------------------#
# Örnek:
# 0'dan 10'a kadar olan sayıları yazalım:

for i in range(10):

    print(i)

#-------------------------------------#

# For Döngüsü: bir aralıkta (range) ya da liste içinde kolayca döngü kurmamızı sağlar.
# For Döngüsü Özellileri:
  # belirli bir aralıkta -> range(başlangıç, bitiş, artış)
  # başlangıç -> dahil (default: 0)
  # bitiş -> hariç
  # artış -> default 1

#-------------------------------------#
# Örnek:
# 1'e 10'a kadar olan sayıları, 2'şer atlayarak ekrana yazacağız.

for i in range(1,10,2):

    print(i)


#-------------------------------------#
# Örnek:
# 5'ten 30'a (dahil) kadar olan sayıları 3'er atlayarak yazalım:
sayi= int(input("lütfen bir sayı giriniz : "))

for i in range(5, 31, 3):

    print(i)
#-------------------------------------#
# Örnek:
# Girilen bir sayının tüm çarpanlarını yazalım:
sayi = int(input("Lütfen bir sayı giriniz: "))

for i in range(2, sayi):
    
    # sayi, i'ye tam bölünüyor mu?
    if sayi % i == 0:
        print(i)

#-------------------------------------#
# Örnek:
# Girilen bir sayının asal olup olmadığını bulalım:
sayi = int(input("Bir sayı giriniz: "))

# asal olarak varsayalım
asal_mi = True

for i in range(2, sayi):
    # sayi, i'ye tam bölünüyor mu
    if sayi % i == 0:
        asal_mi = False

if asal_mi:
    print("{0} ASAL'dır".format(sayi))
else:
    print("{0} ASAL DEĞİL".format(sayi))
#-------------------------------------#
# Örnek:
# Tek for döngüsü içinde, 20'den 1'e kadar tek sayıları geriye doğru yazın.

for i in range(20, 1, -1):

    if i % 2 == 1:

        print(i)

#-------------------------------------#
# Örnek:
# 1 de dahil olsun
for i in range(20, 0, -1):

    if i % 2 == 1:
        
        print(i)

#------------------------------------------------------------------------------------#

# For Döngüsü ile Metinler (String'ler) Üzerinde Dönme

#-------------------------------------#
# Örnek:
metin = "Python"

for harf in metin:
    print(harf)
    

#-------------------------------------#
# Örnek:
# Girilen bir metnin harflerinden sonra "-" karakteri koyalım.
# kullanıcından metin iste
metin = input("Lütfen bir metin giriniz: ")

yeni_metin = ""

for harf in metin:
    # harfi ve "-" karakterlerini yeni metne ekle
    yeni_metin += harf + "-"
    
print(yeni_metin)


#-------------------------------------#
# Örnek:

#-------------------------------------#
# Örnek: