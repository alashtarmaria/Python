# Soru 2:

# Parametre olarak, cümlelerden oluşan bir paragraf listesi alan bir fonksiyon yazın. Adı cumleleri_ver olsun.

# Fonksiyon bu paragraf listesi içindeki cümleleri dönsün.

# Önce for döngüsü sonra comprehension ile yapınız. Comprehension ile fonksiyon adı cumleleri_ver_comp olsun.

# paragraph = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
#              "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
#              "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
#              "Excepteur sint occaecat cupidatat non proident."]


# Çözüm 2:

# for döngüsü ile
# paragraph içindeki cümleleri yazalım
def cumleleri_ver(paragraph):
    
    cumleler = []
    
    for cumle in paragraph:
        cumleler.append(cumle)

    return cumleler


paragraph = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
             "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
             "Excepteur sint occaecat cupidatat non proident."]


cumleler = cumleleri_ver(paragraph)
print(cumleler)


# cumleleri comprehension ile alalım şimdi

def cumleleri_ver_comp(paragraph):
    
    cumleler = [cumle for cumle in paragraph]
    
    return cumleler


cumleler = cumleleri_ver_comp(paragraph)
print(cumleler)