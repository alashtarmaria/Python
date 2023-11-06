# Tuple'lar Immutable (Değiştirilemezler)

t = tuple([0,1,2,3,5,5,6,7,8,9])
print(t)


# t[4] = 4
# TypeError: 'tuple' object does not support item assignment

# Yeniden atama yaparız
t = tuple([0,1,2,3,4,5,6,7,8,9])
print(t)


# Tuple Karşılaştırma
# Aynı stringlerdeki gibi alfabetik karşılaştırır.
print((1, 2, 3) < (5, 4 , 3))
#True

print((5, 40, 200) < (6, 3, 5))
#True

print('abckl' < 'abcde')
# False

print(tuple('abckl') < tuple('abcde'))
# False
