# Dictionary Yaratma

# List'ler [] ile yaratılır. -> list()
# Dictionary ise {} ile yaratılır. -> dict()

# Önemli Not:
# Listelere index ile erişilir. -> list[0]
# Dictionary için [] ile index alma yok.
# [] içine index numarası değil -> key yazılır.


# örnekler :
# İngilizce Türkçe Sözlük
ingTR = {}

print(type(ingTR))
# <class 'dict'>

# araba
araba = {
    'Audi': 'Almanya',
    'Mazda': 'Japonya',
    'Fiat': 'İtalya'
}
print(araba)
print(type(araba))
#  {'Audi': 'Almanya', 'Mazda': 'Japonya', 'Fiat': 'İtalya'}
# <class 'dict'>


# dict() ile yaratma
trING = dict()

print(type(trING))
# <class 'dict'>


araba2 = dict(
    {
        'Audi': 'Almanya',
        'Mazda': 'Japonya',
        'Fiat': 'İtalya'
    }
)
print(araba2)
#  {'Audi': 'Almanya', 'Mazda': 'Japonya', 'Fiat': 'İtalya'}


# print(araba[0])
# KeyError: 0

print(araba['Audi'])
# 'Almanya'


# olmayan bir Key ile eleman iste
# KeyError: 'BMW'
# print(araba['BMW'])