# List'den Eleman Silmek (Delete)
# Listeden eleman silmek bir kaç yöntem ile yapılır:

       # 1- Eğer silinecek elemanın index'ini biliyorsak -> pop(index) 
           # *Eğer pop()'a index geçmezseniz ne olur? En sondaki elemanı siler.
       # 2- Eğer silinen elemana ihtiyacınız yoksa: del
       # 3- Eğer silinecek elemanın kendisini biliyorsak (index değil) -> remove(eleman)

# Tek seferde birden fazla eleman silmek için -> slice (dilim)

# ÖRNEKLER :
dizi = ['x', 'y', 'z', 't']
# pop() fonksiyonu bize silinen elemanı geri döner
silinen = dizi.pop(2)
print("Dizi : ",dizi)
print("Silinen : ",silinen)
# Dizi :  ['x', 'y', 't']
# Silinen :  z


dizi.pop()
print("Dizi : ",dizi)
# t silinir


# del
# dizinin 2. index'teki yani 'm' yi silelim
dizi = ["k", "l", "m", "n", "o"]
del dizi[2]
print("Dizi : ",dizi)
print("Dizi 2.elman sildikten sonra : ",dizi)


# 3. index'teki elemanı sil
del dizi[3]
print("Dizi 3.elman sildikten sonra : ",dizi)


# Tek seferde birden fazla eleman silmek için -> slice (dilim)
# 1. indexten 5. indexe kadar sil
yeni_dizi = ['a', 'b', 'c', 'd', 'e', 'f']
print("yeni_dizi elemanları silmeden önce =",yeni_dizi)
del yeni_dizi[1:5]
print("yeni_dizi =",yeni_dizi)


dizi_2 = ['a', 'b', 'c', 'd', 'e', 'f']
print("dizi_2 elemanları silmeden önce =",dizi_2)
# d harfini sil
dizi_2.remove('d')
print("d elemanları sildikten sonra =",dizi_2)

dizi_2.remove('a')
print("a elemanları sildikten sonra =",dizi_2)

# dizi_2.remove('k')
# print("k elemanları sildikten sonra =",dizi_2)
# ValueError: list.remove(x): x not in list)