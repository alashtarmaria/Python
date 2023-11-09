# 1'den 7'ye kadar olan sayıların küplerini ekrana yazalım: 

# Klasik Yöntem:

kupler = []

for k in range(1,7):
    kupler.append(k**3)
    
print(kupler)
# [1, 8, 27, 64, 125, 216]

# Comprehensin

kupler_comp = [k**3
               for k in range(1, 7)]

print(kupler_comp)
# [1, 8, 27, 64, 125, 216]