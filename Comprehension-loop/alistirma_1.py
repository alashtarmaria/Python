# 1'den 10'a kadar olan sayıların karelerini içeren bir liste yapalım:

# Klasik Yöntem

kareler = []

for i in range(1, 11):
    kareler.append(i**2)
    
print(kareler)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Comprehension

kareler_comp = [i**2 for i in range(1, 11)]

print(kareler_comp)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]