# Soru 9:

# Parametre olarak bir Tuple alan bir fonksiyon yazın. Adı tuple_sirala olsun.

# Parametre olarak gelen Tuple, içinde Tuple'lar tutan bir yapı olsun. Yani elemanlar da Tuple olsun. Ve bu elemanlardan herbiri 2 elemanlı bir Tuple olacak.

# Fonksiyon, parametre olarak gelen Tuple'i sıralayacak ve sıralı bir Tuple dönecek.

# Sıralama kuralı, 2. eleman olacak. Yani içerideki Tuple'ların 2. elemanına bakıp ona göre sıralayacak.

# İpuçları:

# lambda fonksiyon kullanınız
# Parametre:
# tuple_of_tuples = (('a', 12), ('e', 8), ('b', 16), ('c', 22))

# Sonuc:
# [('e', 8), ('a', 12), ('b', 16), ('c', 22)]

# Çözüm 9:

def tuple_sirala(tuple_of_tuples):
    
    # gelen tuple_of_tuples, içinde tuple'lar olan bir tuple
    # herbir eleman, 0,1 olarak index ile iç eleman alabiliriz
    # ilk eleman tup[0]
    # tuple_of_tuples[0][1]
    
    return sorted(tuple_of_tuples, key = lambda x: x[1])


tuple_of_tuples = (('a', 12), ('e', 8), ('b', 16), ('c', 22))

ikinci_sirali_tupler = tuple_sirala(tuple_of_tuples)
print(ikinci_sirali_tupler)    



# Çözüm 9:
# [('a', 12), ('b', 16), ('c', 22), ('e', 8)]

def tuple_sirala_2(tuple_of_tuples):
     
     return sorted(tuple_of_tuples, key = lambda x: x[0])


tuple_of_tuples = (('a', 12), ('e', 8), ('b', 16), ('c', 22))
ikinci_sirali_tupler = tuple_sirala_2(tuple_of_tuples)
print(ikinci_sirali_tupler)        