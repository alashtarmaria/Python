# Soru 5:

# Sıfırdan 20'e (dahil) kadar olan tüm sayıların karesini alan bir fonksiyon yazın. Adı kareler_sozlugu olsun.

# Fonksiyon kareleri bir Dictionary olarak dönsün. Dictionary'nin key'i sayının kendisi, value'su ise sayının karesi olsun.

# {sayi: karesi} şeklinde.

# İpuçları:

# döngü kullanmayın
# direk comprehension ile yapın
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}


# Çözüm 5:

# Sıfırdan 20'ye kadar olan tüm sayıların karesini alalım
# {sayi: karesi}

def kareler_sozlugu():
    
    kareler = {num: num**2 for num in range(0, 21)}
    
    return kareler

kare_sozlugu = kareler_sozlugu()
print(kare_sozlugu)


# Çözüm 2:
def kareler_sozlugu():
    
    sozluk ={}
    
    for i in range(0,21):
        sozluk[i] = i**2
        
    return sozluk