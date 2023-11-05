# Set'lerde Atama İşlemi:
# Alising: Yeniden adlandırma
# Set'lerde atama işlemi, aslında bir Alising İşlemidir.


# bir set yaratalım
a = {2, 5, 7}

# atama işlemi
b = a

# b'ye yeni bir eleman ekle
b.add('YENİ')

# şimdi a ve b'yi yazdır
print('a:', a)
print('b:', b)

# a: {'YENİ', 2, 5, 7}
# b: {'YENİ', 2, 5, 7}