# List'ler ve String'ler
# String bir karakter dizisi, List ise değerler dizisidir.
# İkisi de dizidir.

# Eğer bir String'i, List'e çevirmek istersek 
# list() yapıcısını (constructor) kullanılır.

# Önemli : 
     # kelimelere ayırmak istesek spilt() kullanırız
     # harflere ayırmak istesek list()
     # join() split()'in tam tersidir


# ÖRNEKLER:
gun = "Pazartesi"
print(gun)
print(type(gun))

gun_harflerini = list(gun)
print(gun_harflerini)
print(type(gun_harflerini))

metin = 'bugün hava biraz soğuk'
print(metin)

# metnin kelimelerini split() edelim
# ['bugün', 'hava', 'biraz', 'soğuk']
kelimeler = metin.split()
print(kelimeler)
print(type(kelimeler))


# metnin harflerini almak istesek
harfler = list(metin)
print(harfler)

# örnek :
# ['spam', 'spam', 'spam', 'spam']
mailbox = 'spam-spam-spam-spam'
karakter = '-'

mailler = mailbox.split(karakter)
print(mailler)

# örnek :
kelimeler = ['güneş', 'açar', 'yüzler', 'güler']
# join()
cumle = ' '.join(kelimeler)
print(cumle)

cumle = '-'.join(kelimeler)
print(cumle)
