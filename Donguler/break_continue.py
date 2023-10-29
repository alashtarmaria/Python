# Döngüden Çıkış: break
# Bazen, bir döngü tamamlanmadan çıkmamız gerekebilir.

# Bunun için break keyword'u kullanılır.


# Örnek:
# Verilen bir metnin harflerini yazalım.
# Harfleri yazarken, eğer boşluk (space) karakteri görürsek, döngüden çıkalım.

metin = input("Lütfen bir metin giriniz: ")

for harf in metin:
    
    # boşluk mu diye bak
    if harf == " ":
        break
    
    # boşluk değilse devam edecek
    print(harf)


# Örnek:
# 30'dan 100'e kadar olan sayıları yazalım.
# Eğer yazdığımız sayı 11'in katı ise yazıp sonra döngüden çıkalım:
# 11'in katını ilk bulduğumuz anda döngüden çıkacağız

print("------- Döngüden Önce -------")

for i in range(30, 101):
    
    # 11'in katı mı kontrol et
    if i % 11 == 0:
        print(i)
        break
    else:
        # 11'in katı değil -> sayıyı yaz
        print(i)

print("------- Döngüden Sonra -------")



# Döngününün Bir Sonraki Adımına Atla: continue
# Bazen, döngü içinde dönerken, bir koşula göre, o andaki adımı (iteration) atlayıp,
# bir sonraki adıma geçmeniz gerekebilir.
# Bunun için continue anahtar kelimesi kullanılır.

# Örnek:
# 1'den 10'a kadar çift sayıları continue kullanarak yazalım:

for i in range(1, 11):
    
    # sayı tek ise işleme devam etme -> bir sonraki adıma geç
    if i % 2 == 1:
        continue
    
    # eğer buraya geldiyse 
    print(i)


# Örnek:
# Verilen metnin harflerini yazacağız.
# Harfleri yazarken, eğer boşluk karakteri (space) görürsek bunu yazmayalım.
# Sadece boşluk dışındakileri yazıcaz.

metin = input("Lütfen bir metin giriniz: ")

for harf in metin:
    
    # boşluk mu -> continue
    if harf == ' ':
        continue
        
    # bolşuk değil -> print
    print(harf)
    