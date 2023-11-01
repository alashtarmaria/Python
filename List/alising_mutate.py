# Alising (Yeni Bir Ad Verme)
# Python'da Tip Türleri:
    # 1- Primitive Tipler: 
        # int, float, string, boolean
    # 2- Non-Primitive Tipler: 
        # list, dict, tupe ...

# 1- Primitive Tipler:
x = 24
y = x

print(x==y)
# True

print(x is y)
# True

# y'i tekrar ataylım
y = 40
print(x == y)
# False

print(x is y)
# False

# 2- Non-Primitive Tipler
a = [1,2,3,4,5,6]
b = a

print(a == b)
# True

print(a is b)
# True

print('a:', a)
print('b:', b)
# a: [1, 2, 3, 4, 5, 6]
# b: [1, 2, 3, 4, 5, 6]

# Non-Primitive Tipler -> Yeniden Atama
b = [10, 20, 30, 40]
print('a:', a)
print('b:', b)
# a: [1, 2, 3, 4, 5, 6]
# b: [10, 20, 30, 40]


print(a == b)
# False

print(a is b)
# False

# Non-Primitive Tipler -> Mutate Etseydik (Bir parçasını değiştirseydik)
# Mutasyon nesneleri ayırmaz. İkisini de aynı anda değiştirir.
# O yüzden, Non-Primitive tiplerde, atama işlemi normal bir atama değil,
# bir yeniden adlandırma işlemidir. (alising)

a = [1,2,3,4,5,6]
b = a

print('a:', a)
print('b:', b)
# a: [1, 2, 3, 4, 5, 6]
# b: [1, 2, 3, 4, 5, 6]


b[0] = 'B'
b[1] = 'C'

print('a:', a)
print('b:', b)
# a: ['B', 'C', 3, 4, 5, 6]
# b: ['B', 'C', 3, 4, 5, 6]

print(a is b)
# True


