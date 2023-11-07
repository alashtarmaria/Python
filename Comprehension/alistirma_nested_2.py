# 1'den 10'a kadar olan tüm sayıları, kendileri key ve kendinden küçük pozitif tam sayılar da value listesi olacak şekilde bir dict kuralım:

# kucukler = {
#     1: [1],
#     2: [1, 2],
#     3: [1, 2, 3],
#     4: [1, 2, 3, 4],
#     ...
#     10: []
# }

# Klasik Yöntem
kucukler = {}

for i in range(1, 11):    
    for j in range(1, i + 1):        
        # bu key var mı kontrol et
        if not i in kucukler:
            kucukler[i] = [j]
        else:
            kucukler[i].append(j)
            
print(kucukler)


# Comprehension
kucukler_comp = {i: [j for j in range(1, i+1)] 
                 for i in range(1, 11)}

print(kucukler_comp)