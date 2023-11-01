# Range Fonksiyonu ile List Üretmek

# Örnek :
for i in range(1, 10, 2):
    print(i)

# Örnek :
# bize 2'den 30'a kadar giden, 3'er artan sayılar lazım
# [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
liste = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
print(liste)

# Örnek :
# [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
aralik = range(2, 30, 3)
range_liste = list(aralik)
print(range_liste)


# Örnek :
# en kısa yol 
# [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
print(list(range(2, 30, 3)))


# Örnek :
# 2'den başla 100' kadar, 4'er artan sayılar
# [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]
print(list(range(2, 100, 4)))


# Örnek :
