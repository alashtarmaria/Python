# Python'da List'ler için hazır (built-in) metodlar vardır:

# append(): Listenin sonuna yeni bir eleman ekler
# insert(): Belli bir index ile listeye eleman ekler
# extend(): Listeye başka bir liste ekler
# sort(): Listeyi belli bir sıraya göre sıralar (yerinde yapar)
# sorted(): Listeyi sıralar ve sıralı olarak yeni bir liste verir.

harfler = ["a", "b", "c", "d", "e"]
print(harfler)


# append()
# yeni bir eleman ekle
harfler.append('f')
print(harfler)


# append() sona ekler
# birkaç eleman ekleyelim
harfler.append('a')
harfler.append('x')
harfler.append('t')
print(harfler)

# insert()
# listeye eleman eklerken sona değil de, belli bir sıraya ekleyelim
# insert(index, eleman)
print("insert öncesi harfler:", harfler)
# insert 
harfler.insert(2, 'R')
print("insert sonrası harfler:", harfler)

# extend()
# listeye başka bir liste ekler
sesli_harfler = ["a", "e", "ı", "u", "o"]
noktali_sesliler = ["i", "ü", "ö"]

sesli_harfler.extend(noktali_sesliler)
print(sesli_harfler)

# sort()
# sort() listeyi yerinde sıralar
t = ['d', 'c', 'e', 'b', 'a']
print("Sıralamadan önce       :",t)

t.sort()
print("Sıraldıktan sonr       :",t)

t.sort(reverse=True)
print("Ters Sıraldıktan sonra :",t)



# sorted()
# sorted() listenin sıralı kopyasını verir

a = [4,2,1,6,3]
print(a)
# [4, 2, 1, 6, 3]

b = sorted(a)
print(b)
# [1, 2, 3, 4, 6]

print(a)
# [4, 2, 1, 6, 3]

c = sorted(a, reverse=True)
print(c)
# [6, 4, 3, 2, 1]

print(a)
# [4, 2, 1, 6, 3]

# clear()
# listeyi temizler 
meyve = ["muz", "erik", "ananas"]
meyve.clear()
print(meyve)

# copy()
# listenin kopyasını oluşturur
meyve = ["muz", "erik", "ananas"]
x = meyve.copy()
print(x)


# count()
meyve = ["muz", "erik", "ananas"]
x = meyve.count("muz")
print(x)


# index()
# What is the position of the value "cherry":
meyve = ["muz", "erik", "ananas"]
x = meyve.index("muz")
print(x)


# reverse()
meyve = ["muz", "erik", "ananas"]
meyve.reverse()
print(meyve)




