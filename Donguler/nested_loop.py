# Döngü içinde Döngü (Nested Loops)
# Birçok zaman bir döngü içinde gezerken, döngünün o andaki elemanı (iteration) 
# için başka bir döngü çalıştırmamız gerekir.


# Örnek:
# Ekrana yıldızlardan oluşan bir kare çizelim:
# Bu karenin 3 satırı, 3 sütunu (yıldız) olsun.
# while kullanarak yapalım.

# Çözüm:

# satırlar için bir döngü
# sütunlar için, içeride ikinci bir döngü

# satır döngüsü
i = 0

while i < 3:
    
    yildizlar = ""
    
    # sütun döngüsü
    j = 0
    while j < 3:
        yildizlar += "* "
        j += 1
    
    # yıldızları yazdıralım (satır bazlı yazıyoruz)
    print(yildizlar)
    
    i += 1




# Örnek:
# Yukarıdaki örneği for döngüsü ile yapalım:    
# Çözüm

# satırlar için bir döngü
# sütunlar için, içeride bir döngü

# satır döngüsü
for i in range(10):
    yildizlar = ""
    
    # sütun döngüsü
    for j in range(5):
        yildizlar += "* "
        
    # yıldızları yazdıralım (satır bazlı yazıyoruz)
    print(yildizlar)
    