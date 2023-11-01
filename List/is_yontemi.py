# is İfadesi :
       # x == y          -> Değer Kontolü  (Equivalent)
       # id(x) == id(y)  -> Nesne Kontrolü (Identical) -> is

# ÖRNEKLER:
a = [1,2,3,4,5]
b = [1,2,3,4,5]


# şimdi a ile b aynı nesne mi bakalım?
# identical
print(a is b)
# False

s1 = 'bilgisayar'
s2 = 'bilgisayar'
print(s1 is s2)
# True

print(a == b)
# True

print(s1 == s2)
# True

print(b is a)
# False

print(s2 is s1)
# True



