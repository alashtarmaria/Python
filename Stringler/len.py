### Stringin Uzunluğu
# Bir dizinin uzunluğunu almak için, standart Pyton fonksiyonu olan len() fonksiyonu kullanılır.

meyve = 'portakal'
print(meyve)

# meyve değişkenin uzunluğu
print(len(meyve))

# `meyve` değişkeninin uzunluğu 8 olduğuna göre, **son index değeri 7'dir.**
# meyve'nin son harfini alalım
# tek tek saymamıza gerek yok

# index değeri len() değerinin 1 eksiğidir
# index = len() - 1

son_index = len(meyve) - 1
print('son index:', son_index)

son_eleman = meyve[son_index]
print("son eleman:", son_eleman)

# meyve'nin son elemanı
print(meyve[len(meyve) - 1])


# Eğer index değeri uzunluğa eğitse ne olur
# IndexError: string index out of range
# print(meyve[len(meyve)])


x = 'makine öğrenmesi'
y = 'ALAN TURING'

print(x)
print(y)
print(len(x), len(y))
