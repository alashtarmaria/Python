# print(arac) print(arac)

# Dictionary'den Eleman Okuma

# dict[key] = value

ingTR = {}

ingTR['one'] = 'bir'
ingTR['two'] = 'iki'
ingTR['three'] = 'üç'
ingTR['for'] = 'dört'
ingTR['seven'] = 'yedi'
ingTR['eight'] = 'sekiz'
ingTR['nine'] = 'dokuz'
ingTR['ten'] = 'on'
# print(ingTR)
# {'one': 'bir', 'two': 'iki', 'three': 'üç', 'for': 'dört', 'seven': 'yedi', 'eight': 'sekiz', 'nine': 'dokuz', 'ten': 'on'}

print(ingTR['seven'])
print(ingTR['ten'])


#  ******* dict.items() ********** #
print(ingTR.items())

#  ******* dict.keys() ********** #
print(ingTR.keys())


#  ******* dict.values() ********** #
print(ingTR.values())

# Örnek 1 :
# for ile key-value okumak
for key, value in ingTR.items():
    print("{} keyinde: {} değeri vardır.".format(key, value))


# Örnek 2 :
for k, v in ingTR.items():
    print(k, ":", v)


# Örnek 3 :
# sadece anahtarlar
for anahtar in ingTR.keys():
    print(anahtar)
    

# Örnek 4 :
# sadece değerler
for deger in ingTR.values():
    print(deger)


# Örnek 5 :
arac = {
    'marka': 'Ford',
    'model': 'Mustang',
    'yil': 1964,
    'renk': 'kırmızı',
    'fiyat': 300000
}

print(arac)

#  ******* get() ********** #
print(arac.get('model'))
print(arac['model'])


# olmayan key ile sorarsanız
# KeyError: 'km' alınır 
# arac['km']

print(arac.get('km'))


#  ******* len() ********** #
print(len(arac))


#  ******* in ********** #

# bu şekilde key içinde arar
print('yil' in arac)
# True

print('seven' in ingTR)
# True

print('five' in ingTR)
# False

# Değerler içinde aramak istesek
print('dört' in ingTR.values())
# True

print('sekiz' in ingTR.values())
# True

print('onsekiz' in ingTR.values())
# False

