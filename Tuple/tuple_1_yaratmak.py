# Tuple Yaratmak
# Aynı String ve List, gibi Tuple da Dizi (sequence) tipinde bir değişkendir.
# Tuple'lar herhangi bir türde değer alabilirler ve tam sayılar ile indexlenirler.
# Dolayısı ile List'lere çok benzerler.
# Tuple ile List arasındaki en önemli fark; List Mutable (Değiştirilebilir) iken Tuple Immutable (Değiştirilemez) dir.


# Tuple virgül ile ayrılmış bir listedir.

# Virgül ile Ayrılmış Değer Girerek Tuple Yaratmak:
t = 'x', 'y', 'z', 'q', 'p'
print(t)
print(type(t))
# ('x', 'y', 'z', 'q', 'p')
# <class 'tuple'>

t2 = (1, 2, 3, 4, 5)
print(t2)
print(isinstance(t2, tuple))
# (1, 2, 3, 4, 5)
# True
print(isinstance(t2, list))
# False

# Soru:
# Tek elemanlı bir Tuple nasıl yaratılır?

tek_tuple = 'x'
print(tek_tuple)
print(type(tek_tuple))
# str

tek_tuple = ('x')
print(tek_tuple)
print(type(tek_tuple))
# str

# Cevap:
# Tek elemanlı tuple, sonunda virgül ile yaratılır.
tek_tuple = ('x',)
print(tek_tuple)
print(type(tek_tuple))
#('x',)
# tuple

# tuple() Constructor'ı ile Tuple Yaratmak
tup = tuple()
print(tup)

# tuple() constructor'ı ile eleman vererek yaratalım
tek = tuple('t')
print(tek)

# tuple() yapıcısı (constructor) içine string, list verirseniz (dizi tipinde) her bir 
# elemanını ayrı bir tuple elemanı haline getirir:
dil = tuple('Python')
print(dil)
# ('P', 'y', 't', 'h', 'o', 'n')


listem = ['A', 'B', 'C', 'D']
tup_liste = tuple(listem)
print(tup_liste)
# ('A', 'B', 'C', 'D')


# List Operasyonlarının çoğu Tuple için de geçerlidir.

# index
tup = ('t', 'u', 'p', 'l', 'e')
print(tup)
# ('t', 'u', 'p', 'l', 'e')

print(tup[0])
# 't'

print(tup[2])
# 'p'


# Index varsa, dilim (slice) da vardır.
# slice -> [başlangıç : bitiş : artış]

print(tup[1:4])
# ('u', 'p', 'l')

ay = tuple("Ay, Dünya'nın uydusudur.")
print(ay)
# ('A', 'y', ',', ' ', 'D', 'ü', 'n', 'y', 'a', "'", 'n', 'ı', 'n', ' ', 'u', 'y', 'd', 'u', 's', 'u', 'd', 'u', 'r', '.')
# bu cümleden 'Dünya' kelimesini al (slice)
print(ay[4:9])
# ('D', 'ü', 'n', 'y', 'a')


# cümleyi tersten yazdıralım
# düzden -> kopyası
print(ay[::])

# tersten kopyası
print(ay[::-1])

# ('A', 'y', ',', ' ', 'D', 'ü', 'n', 'y', 'a', "'", 'n', 'ı', 'n', ' ', 'u', 'y', 'd', 'u', 's', 'u', 'd', 'u', 'r', '.')
# ('.', 'r', 'u', 'd', 'u', 's', 'u', 'd', 'y', 'u', ' ', 'n', 'ı', 'n', "'", 'a', 'y', 'n', 'ü', 'D', ' ', ',', 'y', 'A')