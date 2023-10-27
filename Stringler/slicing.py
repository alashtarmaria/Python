# Slicing (Dilimleme)

# Indexing ile sonuç olarak sadece bir eleman elde ettik. Ama birkaç tanesini arka arkaya, bir öbek olarak istiyorsam ne yapardım?
# Diyelim ki ilk elemandan başlayarak 3. elemana kadar olan karakterleri elde etmek istiyorum (0. indexten 3. indexe kadar olanları)

isim = "Deniz"
# Burada önemli olan nokta ilk belirtilen indexing dahil edilip son olarak yazılanın dahil edilmemesi
# 0,1,2 indexlerindekileri döndürdü sonuç olarak

delimlenmis_isim = isim[0:3]
print(delimlenmis_isim)       # ---> Den


# ÖNEMLİ
# başlangıç:bitiş olarak veriyoruz ve bitiş olarak verdiğimiz index dahil olmuyor. 
# Başlangıcı belirtmezsek Python default olarak başlangıç değerini 0 alıyor.
# örnek :
delimlenmis_isim = isim[:3]
print(delimlenmis_isim)       # ---> Den

# ÖNEMLİ
# Bitişi belirtmezseniz Python String'in sonuna kadar alıyor, bu sefer son elemanını 
# da dahil ediyor.
# örnek :
delimlenmis_isim = isim[1:]
print(delimlenmis_isim)        # ---> eniz

# örnek :
delimlenmis_isim = isim[0:]
print(delimlenmis_isim)        # ---> Deniz

# örnek :
delimlenmis_isim = isim[:]
print(delimlenmis_isim)        # ---> Deniz


# Slicing yaparken bitiş olarak verdiğimiz değer en büyük indeximizden büyükse
# hata almayız, sadece sonuna kadar almış olur (sadece indexing yaparken en
# büyük indexten büyük değer verince hata alıyorduk.)
# örnek :
delimlenmis_isim = isim[1:20]
print(delimlenmis_isim)        # ---> eniz

# örnek :
delimlenmis_isim = isim[1:200]
print(delimlenmis_isim)        # ---> eniz

# örnek :
delimlenmis_isim = isim[1:]
print(delimlenmis_isim)        # ---> eniz


# başlangıç:bitiş olarak slicing yapabileceğimiz 
# gibi, başlangıç:bitiş:adım formunda da slicing yapabiliriz. 
# Burada adım parametresi kaçar kaçar gideceğimizi belirle
# örnek :
delimlenmis_isim = isim[0:10:2]
print(delimlenmis_isim)        # ---> Dnz

# örnek :
delimlenmis_isim = isim[0:10:3]
print(delimlenmis_isim)        # ---> Di


# Adım eksi bir değer de olabilir. Böylece ters yönce gitmiş oluruz. Ama başlangıç
# değerinin bitiş değerinden büyük olması lazım bunu yapabilmem için.
# örnek :
# 0. indexten 10. indexe 2 azalarak gidemez, o yüzden boş string döndürür
delimlenmis_isim = isim[10:0:-1]
print(delimlenmis_isim)        # ---> Boş string döndürür ""

# örnek :
delimlenmis_isim = isim[10:0:-1]
print(delimlenmis_isim)        # ---> zine

# örnek :
delimlenmis_isim = isim[::-1]
print(delimlenmis_isim)        # ---> zineD

# örnek :
delimlenmis_isim = isim[::-2]
print(delimlenmis_isim)        # ---> znD



#########
# örnek
m = "merhaba"
print("Cevap" ,"merhaba"[10])  # --> IndexError: string index out of range
                               # 10 diye bir indexi olmadığı, en son indexi 6 olduğu için hata alırım


# örnek
m = "merhaba"
print("Cevap" ,"merhaba"[1:10])  # --> erhaba
                                 # Slicing mantığında son olarak belirttiğim değer index sınırlarının dışında olsa da son elemana kadar alır, o yüzden bana "erhaba" stringini döndürür


####  Stringlerde Casting
# örnek 
a = "5"
b = "5.3"
print("a = ",int(a))              # --> 5
print("b = ",float(b))            # --> 5.3

