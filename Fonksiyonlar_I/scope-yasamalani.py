# Python'da değişkenler tanımlandıkları alanda ve o alanın alt alanlarında geçerlidir.
# Buna scope yani yaşam alanı denir.
# Python'da scope girinti (indent) ile tanımlanır.


# Fonksiyon scope'u içinde bir değişken tanımlayalım
def scope():
    scope_degiskeni = 100
    print(scope_degiskeni)


# Fonksiyonu çağır
scope()


# Şimdi bu değişkene dışarıdan erişmeye çalışalım
# print(scope_degiskeni)
# Değişkenin scope'unun dışından ona ulaşmaya çalışırsak Python Interpreter hata verir. ->NameError
# Ama daha üstte yani **global scope**ta tanımlanmış bir değişkene erişebilirsiniz.


# örnek :
kisa = 4
uzun = 6

# En tepede tanımlanmış kisa ve uzun değişkenlerine tüm fonksiyonlar erişebilir
def cevre():
    dikdortgen_cevresi = 2 * (kisa + uzun) 
    print(dikdortgen_cevresi)

cevre()    

# Peki `global scope` içindeki bir değişkeni fonksiyon içinden değiştirebilir miyiz?
# kisa değişkeninin mevcut halini görelim 
kisa 
# 4


# global scope'u değiştirmeye çalışan fonksiyon
def global_degisken_degistir():
    kisa = 400
    print(kisa)

# fonksiyonu çağır 
global_degisken_degistir()   
# 400

# fonksiyon çağrıldıktan sonra -> kisa değişkeni ne oldu
kisa 
# 4


# Fonksiyon içinden değiştirmemize rağmen, globaldeki değişkenin değeri değişmedi.

# Sebebi:
# Python, globaldeki 'kisa' değişkenine dokunmadı. 
# Siz, fonksiyon içinde 'kisa' değişkenine atama yaptığınız anda, Python sizin yeni bir değişken tanımlar.
# Globaldeki değişkenin kopyasıdır. Bu yeni kopya sadece fonksiyon scope'u içinde yaşar.

# Çözümü:
# Global Scope'taki değişkeni gerçekten değiştirmek istiyorsak istiyorsak:
# Değişken başına **global** anahtar kelimesi yazılır.
    

# fonksiyonu tekrar tanımlayalım
def global_degisken_degistir():
    global kisa
    kisa = 400
    print(kisa)    

global_degisken_degistir()   
#400

# globaldeki kisa değişkenini tekrar gör
kisa 
#400    
