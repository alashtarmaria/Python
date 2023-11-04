# Soru 9:

# Parametre olarak iki liste alan bir fonksiyon yazın. Fonksiyonunuzun adı listeleri_sozluk_yap olsun.

# Fonksiyon ilk listedeki elemanları key, ikinci listedeki elemanları value yaparak ikisinden bir dictionary üretsin.

# İpucu:

# enumerate()
# Parametreler:
# l_1 = ['ad', 'soyad', 'yas', 'cinsiyet']
# l_2 = ['John', 'Doe', 100, 'Erkek']

# Sonuc:
# {'ad': 'John', 'soyad': 'Doe', 'yas': 100, 'cinsiyet': 'Erkek'}


# Çözüm 9:
def listeleri_sozluk_yap(list1, list2):
    
    sozluk = {}
    
    for index, eleman1 in enumerate(list1):
        
        sozluk[eleman1] = list2[index]
        
    return sozluk


l_1 = ['ad', 'soyad', 'yas', 'cinsiyet']
l_2 = ['John', 'Doe', 100, 'Erkek']
calisan = listeleri_sozluk_yap(l_1, l_2)

print(calisan)    