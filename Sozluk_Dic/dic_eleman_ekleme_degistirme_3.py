# Dictionary'e Eleman Ekleme - Değiştirme
# Dictionary'ler {key: value} şeklinde yapılardır.

# Önemle Not:
# Listelerde eleman eklemek için -> append(), insert()
# Dictionary için bu metodlar yoktur.
# dict[key] = value

ingTR = dict()
print(ingTR)


# bir kaç eleman ekleyelim
ingTR['one'] = 'bir'
print(ingTR)
# {'one': 'bir'}


ingTR['two'] = 'iki'
ingTR['three'] = 'üç'
print(ingTR)
#  {'one': 'bir', 'two': 'iki', 'three': 'üç'}


# ingTR.append({'four': 'dört'})
# AttributeError: 'dict' object has no attribute 'append'

# key değeri yanlış girelim : 
ingTR['fayf'] = 'beş'
print(ingTR)
# {'one': 'bir', 'two': 'iki', 'three': 'üç', 'fayf': 'beş'}


# key değeri düzeltmek için: 
ingTR['five'] = 'beş'
print(ingTR)
# {'one': 'bir', 'two': 'iki', 'three': 'üç', 'fayf': 'beş', 'five': 'beş'}


ingTR['six'] = 'alttti'
print(ingTR)
# {'one': 'bir','two': 'iki','three': 'üç','fayf': 'beş','five': 'beş','six': 'alttti'


ingTR['six'] = 'altı'
print(ingTR)
{'one': 'bir','two': 'iki','three': 'üç','fayf': 'beş','five': 'beş','six': 'altı'}



# update()
arac = {
    'marka': 'Ford',
    'model': 'Mustang',
    'yil': 1964
}

print(arac)
# {'marka': 'Ford', 'model': 'Mustang', 'yil': 1964}

# arac sözlüğüne renk ekleyelim
eklenecek = {'renk': 'kırmızı'}
arac.update(eklenecek)
print(arac)
# {'marka': 'Ford', 'model': 'Mustang', 'yil': 1964, 'renk': 'kırmızı'}


# tek seferde birden fazla eleman eklemek istiyoruz -> update
eklenecekler = {
        'fiyat': 300000, 
        'km': 89000, 
        'motor': 1.6
}

arac.update(eklenecekler)
print(arac)
# {'marka': 'Ford', 'model': 'Mustang','yil': 1964,'renk': 'kırmızı','fiyat': 300000,'km': 89000,'motor': 1.6}