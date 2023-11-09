# 2'den 20'ye kadar olan tüm sayıları, kendileri key olacak ve çarpanları da bir value listesi olacak şekilde bir Dictionay içinde tutalım:

# Şu şekilde bir sonuç üretelim:

# carpanlar = {
# 2: [2],
# 3: [3],
# 4: [2, 4],
# 5: [5],
# 6: [2, 3, 6]
# 7: [7],
# 8: [2, 4, 8],
# 9: [3, 9],
# 10: [2, 5, 10],
# ...
# }

# klasik yöntem -> for döngüleri ile

carpanlar = {}

for i in range(2, 21):
    for j in range(2, i+1):
        if i % j == 0:
            if not i in carpanlar:
                carpanlar[i] = [j]
            else:
                carpanlar[i].append(j)

print(carpanlar)


# comprehension ile

carpanlar_comp = {
    i: [j for j in range(2, i+1) if i % j == 0]
    for i in range(2, 21)
}

print(carpanlar_comp)