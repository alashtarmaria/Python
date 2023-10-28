#----------------------------------------------------------------------------------------------------------------------------#

# Şartlı İfade, Bir Yargıdı
# Şartlı İfade sonucu True ya da False olan ifadelerdir. Yani bir yargı bildirirler.
# Şartlı ifadeler Şart Operatörleri ve Mantıksal Operatörler ile kontrol edilir.


# Şart Operatörleri:

# x == y : x, y'ye eşit midir?
# x != y : x, y'ye eşit değil midir?
# x < y : x, y'den küçük müdür?
# x > y : x, y'den büyük müdür?
# x <= y : x, y'den küçük eşit midir?
# x >= y : x, y'den büyük eşit midir?

x = 12
y = 8

print("x == y :", x == y)
print("x != y :", x != y)
print("x < y :", x < y)
print("x > y :", x > y)
print("x <= y :", x <= y)
print("x >= y :", x >= y)


# **Mantıksal Operatörler**:

# * `and`: ve (her iki taraf da True ise, sonuç True; taraflardan biri False ise sonuç False
# * `or` : veya (her iki taraftan biri bile True ise, sonuç True; her ikisi de False ise sonuç False

# a -> True
a = 6 == 6
print("a is" ,a)     


# b -> False
b = 6 == 8
print("b is ",b)


# and
print("---- and ----")

print("{0} and {1}: {2}".format(a, b, a and b))
print("{0} or {1}: {2}".format(a, b, a or b))


#----------------------------------------------------------------------------------------------------------------------------#

#IF
# Bilgisayar programlarında, kod yukarıdan aşağı doğru çalışır.
# Siz belli şartlara göre, farklı bölümleri çalıştırmak isteyebilirsiniz. Kodu dallandırmak.
# Ör: Verilen bir sayı pozitif ise kabul et, değilse, tekrar iste.
# İşte kod içinde bu kararları veren yapıya if blokları denir.
# if yapılarına karar yapıları da denir.

#--------------------------------------------------------------------#
# Örnek :
# Eğer x sayısı 0'dan büyükse, bunu ekrana yaz
# değilse, birşey yapma
x = 7

if x > 0:
    print("{} sayısı 0'dan büyüktür.".format(x))

#--------------------------------------------------------------------#

# Örnek :
x = -8

if x > 0:

    print("{} sayısı 0'dan büyüktür.".format(x))
    
print("if bloğu sonrası")
    
#--------------------------------------------------------------------#

# Örnek :
# Eğer x sayısı 0'dan büyük ama (ve) 10'dan küçük eşitse bunu ekrana yazalım
x = 10

print("-----------")

if x > 0 and x <= 10:
    print("{} sayısı 0'dan büyük ve 10'dan küçük eşittir.".format(x))
    
print("-----------")        

#--------------------------------------------------------------------#

# Örnek :
x = 17

print("-----------")

if x > 0 and x <= 10:
    print("{} sayısı 0'dan büyük ve 10'dan küçük eşittir.".format(x))
    
print("-----------") 

#--------------------------------------------------------------------#

# Örnek :
x = 6

print("-----------")

if x > 0 and x <= 10:
    print("{} sayısı 0'dan büyük ve 10'dan küçük eşittir.".format(x))
    
print("-----------")  

#--------------------------------------------------------------------#

# Örnek :
# Eğer x sayısı 0'dan büyük eşit ve 20'den küçükse bunu ekrana yazalım
x = 19

print("-----------")

if x >= 0 and x < 20:
    print("{} sayısı 0'dan büyük eşit ve 20'den küçüktür.".format(x))
    
print("-----------")

#--------------------------------------------------------------------#

# Örnek :
x = 49

print("-----------")

if x >= 0 and x < 20:
    print("{} sayısı 0'dan büyük eşit ve 20'den küçüktür.".format(x))
    
print("-----------")

#--------------------------------------------------------------------#

# Örnek :
x = -6

print("-----------")

if x >= 0 and x < 20:
    print("{} sayısı 0'dan büyük eşit ve 20'den küçüktür.".format(x))
    
print("-----------")

#--------------------------------------------------------------------#

# Örnek :
# or ile
# x sayısı 100'den büyük veya (or) 0'dan küçükse ekrana yazdır
x = 80

print("-----------")

if x > 100 or x < 0:
    print("{} sayısı 100'den büyük veya 0'dan küçüktür.".format(x))
    
print("-----------")

#--------------------------------------------------------------------#

# Örnek :
x = 280

print("-----------")

if x > 100 or x < 0:
    print("{} sayısı 100'den büyük veya 0'dan küçüktür.".format(x))
    
print("-----------")

#--------------------------------------------------------------------#

# Örnek :
x = -300

print("-----------")

if x > 100 or x < 0:
    print("{} sayısı 100'den büyük veya 0'dan küçüktür.".format(x))
    
print("-----------")

#--------------------------------------------------------------------#

