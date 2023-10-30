# Metin Karşılaştırma

# Bazen iki metni karşılaştırmamız gerekir.
       # eşitler mi?
       # hangisi büyük?


meyve = 'armut'
if meyve == 'armut':
    print('evet armut')
else:
    print('değil armut')



if meyve == 'elma':
    print('elma')
else:
    print('değil elma')    




armut = 'armut'
elma = 'elma'

if armut < elma:
    print("{0} {1}'dan küçüktür.".format(armut, elma))
else:
    print("{0} {1}'dan büyüktür.".format(armut, elma))


    
# armut elma'dan küçüktür.
# Neden?
# Çünkü -> 'a' harfi 'e' harfinden önce gelir.
# ASCII karakteri daha küçüktür. (American Standard Code for Information Interchange)
# ASCII karakterlerini görmek için -> ord() fonksiyonu kullanılır.
print(ord('a'))
print(ord('A'))
print(ord('e'))
print(ord('E'))


# ASCII'ye göre bütün büyük harfler, küçük harflerden önce gelir. (Yani insan algısının tersidir.)
print(ord('a'),ord('A'))
print(ord('a'), ord('z'))


# insan algısının tersi
print('A' > 'a')
print('f' > 'F')



# Python'daki tüm String Metodları aşağıdaki linkten inceleyebilirsiniz:
# https://docs.python.org/3/library/stdtypes.html#string-methods