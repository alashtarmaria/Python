# Python iki değişkenin :
    # değeri aynı ve
    # değişkenler Immutable (str)
    # olduğu için iki farklı farklı değişken yaratmak yerine, ikisini aynı adrese yolladı.

a = 'kivi'
b = 'kivi'


print(id(a))
#2440275187696

print(id(b))
#2440275187696

print(a == b)
# True

print(id(a) == id(b))
# True

b = 'kivis'
print(b)
# kivis

print(id(b))
# 1879941558128 idi değişti

print(a == b)
# False

print(id(a) == id(b))
# False

# Artık a ve b farklı değerler aldığına göre, b için yeni bir adres yarattı.

# Acaba değişkenler List olsaydı?
x = [1, 2, 3]
y = [1, 2, 3]

print(x)
print(y)

# == değerlere bakar
print(x == y)
# True

print(id(x))
# 1971640723840

print(id(y))
# 1971654579648

print(id(x) == id(y))
# False

# == kontrolü -> eşitlik (equivalent) -> değer

# id(x) == id(y) kontrolü -> aynılık (identical) -> nesneler