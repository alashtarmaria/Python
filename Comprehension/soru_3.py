# Soru 3:

# Soru 2'deki paragrafı alıp bu sefer tüm cümlelerdeki tüm kelimeleri tek bir liste içinde dönen bir fonksiyon yazalım. Adı kelimeleri_ver olsun.

# Önce for döngüleri ile sonra comprehension ile yapınız. Comprehension ile adı kelimeleri_ver_comp olsun.
             
# Sonuç:
# ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.', 'Ut', 'enim', 'ad', 'minim', 'veniam,', 'quis', 'nostrud', 'exercitation', 'ullamco.', 'Duis', 'aute', 'irure', 'dolor', 'in', 'reprehenderit', 'in', 'voluptate', 'velit', 'esse.', 'Excepteur', 'sint', 'occaecat', 'cupidatat', 'non', 'proident.']


# Çözüm 3:

# for döngüleri ile
# paragraph'taki tüm kelimeleri alalım

def kelimeleri_ver(paragraph):
    
    kelimeler = []
    
    for cumle in paragraph:
        for kelime in cumle.split():
            kelimeler.append(kelime)
    
    return kelimeler


paragraph = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
             "Ut enim ad minim veniam, quis nostrud exercitation ullamco.",
             "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
             "Excepteur sint occaecat cupidatat non proident."]


kelimeler = kelimeleri_ver(paragraph)
print(kelimeler)



# şimdi paragraph'taki tüm kelimeleri list comprehension ile alalım

def kelimeleri_ver_comp(paragraph):
    
    kelimeler = [kelime
                 for cumle in paragraph
                 for kelime in cumle.split()]
    
    return kelimeler



kelimeler = kelimeleri_ver_comp(paragraph)
print(kelimeler)