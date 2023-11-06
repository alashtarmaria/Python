# Fonksiyonların Dönüş Değeri Olarak Tuple'lar

# Fonksiyonları işlerken fark etmiş olabilirsiniz, Fonksiyon geriye sadece bir değer döner.

# Peki birden fazla değer dönmesi gerekse ne yapacağız.

# Cevap Tuple. Dönecek değerleri bir Tuple içine alırsak o zaman geriye 
# sadece Tuple'i dönmemiz yeterli.


# Örneğin Python'un standart divmod() fonksiyonu iki parametre alır.
# Bölünen ve bölen.
# Bölme işlemini yaptıktan sonra geriye, (bölüm, kalan) şeklinde bir tuple döner.
# 23'ün 4'e bölümünden, bölüm 5 ve kalan 3'tür

sonuc = divmod(23, 4)
print(sonuc)
# (5, 3)


# bölüm ve kalan'ı ayrı ayrı alalım
bolum = sonuc[0]
print(bolum)

kalan = sonuc[1]
print(kalan)
# 5
# 3


# Alıştırma:
# Parametre sayısı belli olmayan bir fonksiyon yazın.
# *args ile, sayısı belli olmayan çoklu parametre alabilir.

# toplam, çarpım değerlerini dönecek
def toplam_ve_carpim(*args):
    
    print(args)
    print(type(args))

print(toplam_ve_carpim(2, 5, 4, 3))
#  (2, 5, 4, 3)
# <class 'tuple'>


# *args yapısı aslında bir Tuple'dır.
# şimdi fonksiyonu yazalım

def toplam_ve_carpim(*args):
    
    # toplam çok kolay -> sum()
    toplam = sum(args)
    
    # çarpım için -> döngü
    carpim = 1
    for arg in args:
        carpim *= arg
        
    
    # şimdi toplam ve çarpım ikilisini bir tuple olarak dönelim
    return (toplam, carpim)


toplam, carpim = toplam_ve_carpim(2, 5, 4, 3)
print("toplam:", toplam)
print("çarpım:", carpim)    
# toplam: 14
# çarpım: 120