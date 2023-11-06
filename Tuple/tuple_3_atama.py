# Tuple Ataması

a = 99
b = 1

# a'nın değerini b'ye, b'nin değerini de a'ya atamak istiyoruz
# karşılıklı atama

# Yöntem 1 -> Geçici değişken

print("a:", a)
print("b:", b)

gecici = a

a = b

b = gecici

print("a:", a)
print("b:", b)
# a: 99
# b: 1
# a: 1
# b: 99

# Yöntem 2 -> Geçici değişken tutmadan 
a = 100
b = 1
print("a önce = " ,a)
print("b önce =",b)
a = a-b 
#99

b = a+b
# 100
a = b-a
# 1
print("a = " ,a)
print("b =",b)

# Yöntem  3 ->
# Python'da Tuple Ataması bu işlemi (swap) otomatik yapar.
# Tuple Ataması

a = 99
b = 1

print("a:", a)
print("b:", b)

a, b = b, a

print("a:", a)
print("b:", b)
# a: 99
# b: 1
# a: 1
# b: 99


# Önemli:
# Tuple Ataması için iki taraftaki değişken sayısının aynı olması lazım
a, b = 500, 800

print("a:", a)
print("b:", b)
# a: 500
# b: 800


# a, b = 500, 800, 600
# ValueError: too many values to unpack (expected 2)