####  F-Strings
# Değişkenlerimizin değerlerini direkt olarak string'lerin içine koymak isteyebiliriz.
# f-string de yaptığımız tek şey aslında değişkenlerin değerlerini veya hesaplamaların sonucunu stringin içine gömmek.
# f"..." diye göreceğimiz yapının adını String Interpolation diye görebilirsiniz.

# örnek :
x = 5
# Diyelim ki ekrana x'in değerini bastırmak istiyorum. Bu durumda istediğim şey "x in değeri 2" diye bastırmak. Bunu şöyle yapabilirim:
print("x in değeri" + " " + str(x))

# Ama ayrı ayrı yazmaya ihtiyaç olmadan direkt x'in değerini string'in içine gömebilseydim daha iyi olmaz mıydı ?
# İçine değer gömeceğimiz string'i tanımlarken başına f yazarak başlıyoruz f"....". Gömmek istediğimiz değeri/değişkeni süslü parantez içine yazıyoruz f".....{}....".
#  Birden çok değer de gömmek isteyebiliriz, 
# o zaman kaç tane yapacaksak o kadar süslü parantez koymamız gerekirdi f".....{}....{}.."
print(f"x in değeri {x}")


# Python'ın yaptığı şey süslü parantezin içini hesaplayıp stringin içine gömmek.
print(f"x in değerinin iki fazlası {x+2}")
# {x+2} kısmında python x+2'yi hesapladı ve string'in içine cevabın değerini gömdü.

# örnek :
isim = input("İsim:")
print(f"verilen isim {isim}")

# örnek :
l = [1,2,3,4]
print(f"verilen liste {l}")


### {} içerisine değeri hesaplanacak herhangi bir şey yazılabilir.

# örnek :
def kare(x):
    return x**2

x = 10
print(f"{x} sayısının karesi {kare(x)}")
