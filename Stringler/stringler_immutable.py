# Stringler Değiştirilemezler (Immutable)
# Python'da Stringler (Metinler) değiştirilemezler. (Immutable)
# Değiştirilmek istenirse Yeniden Atanması gerekir.

# String bir değişken yeniden atanabilir, ama içindeki bir parça değiştirilemez.

selamlama = 'Selam Dünya!'
print(selamlama)


# yeniden atayabiliriz
selamlama = 'Hello World!'
print(selamlama)


# ama içindeki bir parçasını değiştiremeyiz
# diyelim ki ilk harfini 'h' yapmak istedik
# TypeError: 'str' object does not support item assignment
selamlama[0] = 'h'



# str immutable olduğuna göre, ilk harfini nasıl değiştireceğiz?
selamlama = 'hello World!'
print(selamlama)

print(selamlama[6])

# selamlama[6] = 'w'
# TypeError: 'str' object does not support item assignment

print(selamlama[:6])
print(selamlama[7:])


selamlama = selamlama[:6] + "w" + selamlama[7:]
print(selamlama)