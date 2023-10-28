### Fonksiyonun Değer Dönmesi (return) 
# Fonksiyonlar işlerini bitirdikten sonra geriye değer dönebilirler.
# Buna geriye değer return etmek denir ve return anahtar kelimesi ile sağlanır.
# Geriye değer dönmeyen fonksiyonlara, **void** fonksiyonlar denir.


# örnek :
# Kendisine parametre olarak verilen bir sayının küpünü hesaplayıp geri dönen bir fonksiyon yazalım
def cube(n):
    
    # sayının küpünü hesapla
    n_kup = n**3
    
    # bu küp değerini geri dön
    return n_kup

# Şimdi fonksiyonu çağırdığımız zaman, fonksiyon bize bir değer döner
# o değeri alıp bir değişkene atayabiliriz
sayi = 5
kup = cube(5)
print(kup)

# 
n = 4
dordun_kupu = cube(4)
print(dordun_kupu)


# birleşim -> chain
# örnek:
n = 6
print(cube(n))

# örnek :
def cube(n):
    n_kup = n**3
    return n_kup
 
print(cube(3))
    