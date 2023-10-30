
# For-Else Yapısı
# Bazen, bir for döngüsünün düzgün tamamlanıp tamamlanmadığını kontrol etmemiz gerekebilir.
# Örneğin: Eğer for döngüsü bir elemanı için çalışmamışsa, break ifade çağrılmışsa, o zaman düzgün çalışmamış demektir.
# Bunun için for-else yapısı kullanılır.


# Örnek:
# 2 ile 10 arasındaki sayıları yazdırdığımızı varsayalım.
# Eğer sayı 7'nin katı ise, döngüden çıkalım.
# Eğer düzgün çalışırsa "Döngü Düzgün Çalıştı" diye yazalım

print("-------- For Döngüsünden Önce -----------")

for i in range(2, 10):
    print(i)
    if i % 7 == 0:
        break
else:
    print("Döngü Düzgün Çalıştı")

print("-------- For Döngüsünden Sonra -----------")



# Şimdi yukarıdaki örneği 7'ye değil 17'ye tam bölünme diye bakalım:
print("-------- For Döngüsünden Önce -----------")

for i in range(2, 10):
    print(i)
    if i % 17 == 0:
        break
else:
    print("Döngü Düzgün Çalıştı")

print("-------- For Döngüsünden Sonra -----------")

# burada, döngü hiç if'in içine girmedi, break olmadı.
# Yani düzgün çalıştı -> else yapısına gelir.