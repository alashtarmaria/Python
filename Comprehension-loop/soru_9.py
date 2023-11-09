# Soru 9:

# Parametre olarak bir sayı listesi alan bir fonksiyon yazın. Adı sadece_pozitifler olsun.

# Fonksiyon liste içinden sadece pozitif sayıları alsın, tam sayı yapsın ve yeni bir liste olarak dönsün. Comprehension ile yapınız.

# Parametre:
# [12.8, -27.2, -34.5, 58.4, -82.0, 66.6, 14.9]

# Sonuc:
# [12, 58, 66, 14]

# Çözüm 9:

def sadece_pozitifler(liste):
    
    return [int(x) for x in liste if x > 0]
    


sayilar = [12.8, -27.2, -34.5, 58.4, -82.0, 66.6, 14.9]

pozitifler = sadece_pozitifler(sayilar)

print(pozitifler)    




# 2.yol
def sadece_pozitifler(sayilar):
    
    sayi_listesi = []
    
    for sayi in sayilar :
        if sayi > 0:
            sayi =int(sayi)
            sayi_listesi.append(sayi)
    return sayi_listesi    