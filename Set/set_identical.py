# identical: is

a = {2, 5, 7}
b = a


print(a is b)
# True

# equivalent
print(a == b)
# True

print(a.issubset(b))
# True

print(a.issuperset(b))
# True


# şimdi a'ya eleman ekle
a.add('YYY')

print('a:', a)
print('b:', b)
# a: {'YYY', 'YENİ', 2, 5, 7}
# b: {'YYY', 'YENİ', 2, 5, 7}