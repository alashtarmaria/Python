## Döngüler
# Döngü: belirli bir kurala göre, belirlenmiş aralıklar içinde, belirli bir operasyonu 
# tekrar eden yapıdır.
# Python'da döngüler while ve for anahtar kelimeleri ile oluşturulur.

#-------------------------------------#
# While Döngüsü
#-------------------------------------#
# Örnek:
# Diyelim ki 10'dan 1'e kadar geri sayıp yazdırmak istiyoruz.
n = 10

print("------- Döngüden önce -------")
print("n:", n, "\n")

# while True:
#    .....

while n > 0:
    print(n)
    n = n - 1
    
print("------- Döngüden sonra -------")
print("n:", n, "\n")


#-------------------------------------#
# While Döngüsünün İşleyişi:

# While döngüsü, işlemeye başlamadan önce, kuralın doğruluğunu kontrol eder: Durma Kuralı
# Kural doğru (True) ise bir kere işleme yapar
# Kuralı tekrar kontrol eder, doğruysa tekrar işler
# Bu şekilde sonsuz bir döngü oluşmaması için, her seferinde kural kontrol edilir
# Durma koşulunun set edilmesi (tanımlanması) önemlidir
# Yukarıdaki örnekte, n = n - 1 yaparak bu ayarlamayı yaptık
# Böylece her adımda n değeri 1'er azaldığı için, en sonunda 0 oldu ve döngüye girmed

#-------------------------------------#
# Örnek:
# 1'den 20'ye kadar olan tek sayıların karelerini bulalım:

x = 1
while x <= 20:
    # tek sayı mı
    if x % 2 == 1:
        print("{0}'in karesi: {1}'".format(x, x**2))
    
    # durma koşulu
    x += 1
#-------------------------------------#
# Örnek:
# 1'den 10'a kadar olan çift sayıların toplamını bulalım:
k = 1
toplam = 0

while k < 11:
    
    # çift mi 
    if k % 2 == 0:
        toplam += k
        
    # durma koşulu
    k += 1
    
print(toplam)

#-------------------------------------#
# Örnek:
# Girilen bir sayının tüm çarpanlarını bulalım.
# kullanıcıdan sayı iste
sayi = int(input("Bir sayı giriniz: "))

i = 2

while i < sayi:
    
    # sayi, i'ye tam bölünüyor mu? -> %
    if sayi % i == 0:
        print(i)
        
    # durma koşulu
    i += 1

#-------------------------------------#   
# Örnek:
# Girilen bir sayının asal sayı olup olmadığını bulalım:
# kullanıcıdan sayı iste
sayi = int(input("Bir sayı giriniz: "))

# sayının asal olduğunu kabul edelim -> default
asal_mi = True

# döngü değişkeni
i = 2

while i < sayi:
    
    # sayi, i'ye tam bölünüyor mu? -> %
    if sayi % i == 0:
        asal_mi = False

    # durma koşulu
    i += 1

if asal_mi:
    print("{0} ASAL'dır".format(sayi))
else:
    print("{0} ASAL DEĞİL".format(sayi))
    
#-------------------------------------#
