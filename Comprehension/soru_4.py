# Soru 4:

# Soru 2'deki paragrafı alıp bu sefer tüm cümlelerdeki sadece sesli harfle başlayan kelimeleri tek bir liste içinde dönen bir fonksiyon yazalım. Adı sesli_kelimeleri_ver olsun.

# Önce for döngüleri ile sonra comprehension ile yapınız. Comprehension ile adı sesli_kelimeleri_ver_comp olsun.


# Sonuç:
# ['ipsum', 'amet,', 'adipiscing', 'elit.', 'Ut', 'enim', 'ad', 'exercitation', 'ullamco.', 'aute', 'irure', 'in', 'in', 'esse.', 'Excepteur', 'occaecat']

# Çözüm 4:

# for döngüleri ile
# paragraph içindeki sesli harf ile başlayan kelimeleri bulalım

def sesli_kelimeleri_ver(paragraph):
    
    sesliler = ['a', 'e', 'i', 'o', 'u']
    
    sesli_kelimeler = []
    
    for cumle in paragraph:
        for kelime in cumle.split():
            if kelime[0].lower() in sesliler:
                sesli_kelimeler.append(kelime)
                
    return sesli_kelimeler


paragraph = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
             "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
             "Excepteur sint occaecat cupidatat non proident."]

sesli_kelimeler = sesli_kelimeleri_ver(paragraph)
print(sesli_kelimeler)


# sesli harf ile başlayan kelimeleri list comprehension ile bulalım

def sesli_kelimeleri_ver_comp(paragraph):
    
    sesliler = ['a', 'e', 'i', 'o', 'u']
    
    return [kelime
            for cumle in paragraph
            for kelime in cumle.split()
            if kelime[0].lower() in sesliler]          

sesli_kelimeler = sesli_kelimeleri_ver_comp(paragraph)
print(sesli_kelimeler)