# Soru 6:

# Verilen iki sözlüğü içinde key'leri aynı olan elemanların değerlerini toplayan bir fonksiyon yazın.
# Eğer key ikisinde ortak değilse almasın, sadece ortak key'leri alsın.
# Fonksiyonun adı ayni_key_toplamlari olsun.

# İpuçları
          # değilse hata fırlatın -> 'Parametrelerin ikisi de sözlük olmalı'
          # kontrol için -> 'type' yerine bu sefer 'isinstance' kullanın
          # isinstance(<değişken>, )
          # Sözlüklerin uzunluklarının aynı olmasını kontrol edin
          # değilse hata fırlatın -> 'Sözlüklerin uzunluğu aynı olmalı'
          # Parametre sözlükler:
          # d1 = {'a': 10, 'b': 30, 'c':50}
          # d2 = {'a': 40, 'b': 60, 'd':90}

# Sonuç:
# {'a': 50, 'b': 90}


# Çözüm 6:
def ayni_key_toplamlari(d1, d2):
    
    # kontrol 1 -> ikisi de sözlük mü
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise Exception('Parametrelerin ikisi de sözlük olmalı')
    
    # kontrol 2 -> uzunlukları aynı mı
    if len(d1) != len(d2):
        raise Exception('Sözlüklerin uzunluğu aynı olmalı')
    
    # boş sözlük
    sozluk = {}
    
    for key in d1:
        
        if key in d2:
            
            sozluk[key] = d1[key] + d2[key]
    
    return sozluk

d1 = {'a': 10, 'b': 30, 'c':50, 'd': 100}
d2 = {'a': 40, 'b': 60, 'd':90, 'e': 50}
print(ayni_key_toplamlari(d1, d2))
# {'a': 50, 'b': 90, 'd': 190}