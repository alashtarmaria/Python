# Soru 7:

# Soru 6.'teki fonksiyonu biraz daha geliştirelim.

# Fonskiyonunuz aynı şekilde;

# Verilen iki sözlüğü içinde key'leri aynı olan elemanların değerlerini toplasın.

# Eğer key ikisinde ortak değilse hangisinde varsa onu alsın.

# Yani ortak elemanları toplam değer olarak, ayrık elemanları kendi değerleri ilde dönsün.

# Fonksiyonun adı ayni_key_toplamlari_farkli_key_kendileri olsun.

# İpuçları

# Parametrelerin ikisinin de sözlük olmasını kontrol edin
# değilse hata fırlatın -> 'Parametrelerin ikisi de sözlük olmalı'
# kontrol için -> 'type' yerine bu sefer 'isinstance' kullanın
# isinstance(<değişken>, )
# Sözlüklerin uzunluklarının aynı olmasını kontrol edin
# değilse hata fırlatın -> 'Sözlüklerin uzunluğu aynı olmalı'
# Parametre sözlükler:
# d1 = {'a': 10, 'b': 30, 'c':50}
# d2 = {'a': 40, 'b': 60, 'd':90}

# Sonuç:
# {'a': 50, 'b': 90, 'c': 50, 'd': 90}

# Çözüm 7:

def ayni_key_toplamlari_farkli_key_kendileri(d1, d2):
    
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
        else:
            sozluk[key] = d1[key]
    
    for key in d2:
        if not key in d1:
            sozluk[key] = d2[key]

    return sozluk

d1 = {'a': 10, 'b': 30, 'c':50}
d2 = {'a': 40, 'b': 60, 'd':90}
print(ayni_key_toplamlari_farkli_key_kendileri(d1, d2))