# Alıştırma:

# Tuple ataması ile email içindeki kullanıcı adı ve domain adını ayıralım:

print('johnsnow@got.com'.split('@'))
# ['johnsnow', 'got.com']


kullanici_adi, domain = 'johnsnow@got.com'.split('@')
print(kullanici_adi)
print(domain)
# johnsnow
# got.com