# 2'den 20'ye kadar olan tüm çift sayıları, kendileri key olacak ve çarpanları da bir value listesi olacak şekilde bir Dictionay içinde tutalım:

# Şu şekilde bir sonuç üretelim:

# cift_carpanlar = {
#  2: [2],
#  4: [2, 4],
#  6: [2, 3, 6],
#  8: [2, 4, 8],
#  10: [2, 5, 10],
#  12: [2, 3, 4, 6, 12],
#  14: [2, 7, 14],
#  16: [2, 4, 8, 16],
#  18: [2, 3, 6, 9, 18],
#  20: [2, 4, 5, 10, 20]}

# klasik yöntem -> for döngüleri ile

cift_carpanlar = {}

for i in range(2, 21):
    if i % 2 == 0:
        for j in range(2, i+1):
            if i % j == 0:
                if not i in cift_carpanlar:
                    cift_carpanlar[i] = [j]
                else:
                    cift_carpanlar[i].append(j)

print(cift_carpanlar)


# comprehension ile

cift_carpanlar_comp = {i: [j for j in range(2, i+1) if i % j == 0]
                       for i in range(2, 21) if i % 2 == 0}

print(cift_carpanlar_comp)