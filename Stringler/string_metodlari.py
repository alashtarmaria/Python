# String Metodları
# upper(): Metni BÜYÜK yapar

kelime = 'bilgisayar'
yeni_kelime = kelime.upper()
print(yeni_kelime) 


# direk büyük harf yapabiliriz
print('kalem'.upper())


# lower(): Metni küçük yapar
buyuk = 'KarAkaLEM'
kucuk = buyuk.lower()
print(kucuk)


# strip(): Metnin başındaki ve sonundaki boşluk karakterlerini siler.
tumce = '    Bu bir tümcedir.   '
tumce.strip()
print(tumce)


# yukarıdaki örnekte, tumce değişmedi, yeni bir tumce yaratıldı
yeni_tumce = tumce.strip()
print(yeni_tumce)
print(tumce)


# lstrip(): Metnin başındaki (left) boşluk karakterlerini siler.
# rstrip(): Metnin sonundaki (right) boşluk karakterlerini siler.
# lstrip() :
s = "    bu metnin başında boşluk var."
print(s)
print(s.lstrip())

# rstrip() :
s = "bu metnin sonunda boşluk var.    "
print(s)
print(s.rstrip())


# format(): Metni değişkenler ile süsler.
A = 'Pyhton'
B = 'Yapay'
C = 'Zeka'
print("{0} ile {1} {2}".format(A, B, C))


# find(): Metnin içindeki bir karakter ya da metin parçası bulur.
# Bulursa, ilk bulduğu index'i döner
# Bulamazsa, -1

kelime = 'pencereler'
index = kelime.find('e')
print(index)


index = kelime.find('ce')
print(index)



# Standart olarak find() fonksiyonu en baştan yani 0 index'ten aramaya başlar.
# Ama bunu değiştirebiliriz:
# find(metin, başlangıç) -> şeklinde nereden aramaya başlayacığını söylebiliriz

index = kelime.find('e', 2)
print(index)


# find(metin, başlangıç, bitiş)
index = kelime.find('l', 2, 6)
print(index)

index = kelime.find('l', 2, 20)
print(index)


# capitalize(): Metnin İlk Harfini büyük hapar.
film_adi = 'batman dark knight'
film_adi = film_adi.capitalize()
print(film_adi)


#title(): Metnin bütün kelimelerinin İlk Harfini büyük hapar.
film_adi = 'batman dark knight'
film_adi = film_adi.title()
print(film_adi)



#isdigit(): Metin tam sayı mı, değil mi?
girdi = '48'
print(girdi.isdigit())

print('-20'.isdigit())

print('4.5'.isdigit())



# startswith(): Metin verilen karakter ya da metin parçası ile başlar mı?
# endswith()
# örnek :
gezegen = 'Mars'
print(gezegen.startswith('M'))


gezegen = 'Merkür'
print(gezegen.startswith('Mers'))


print(gezegen.endswith('r'))
print(gezegen.endswith('re'))


# replace(): Metnin içindeki bir karakter ya da metin parçasını, başka bir karakter ya da metin parçası ile değiştirir.
bilmece = 'Çarşıdan aldım bir tane, eve geldim bin tane.'
bilmece = bilmece.replace('bir', '*')
print(bilmece)


bilmece = bilmece.replace('bin', '***')
print(bilmece)


txt = 'Atlar elma yemeyi çok sever.'
x = txt.replace('elma', 'havuç')
print('txt:', txt)
print("x:", x)


# split()
# örnek :
a = "this is a string"
a = a.split(" ") # a is converted to a list of strings.
print (a)
#['this', 'is', 'a', 'string']


# join()
# Joining a string is simple:
# örnek :
a = "this is a string"
a = "-".join(a)
print(a)

# count()
# örnek :
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


# swapcase() Make the lower case letters upper case and the upper case letters lower case:
# örnek :
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)



