# Soru 4:
# Adı yeni_arac_yarat bir fonksiyon yazın. Bu fonksiyon Soru 3'teki fonksiyonlardan birini çağırsın ve arac sözlüğünü alsın.
# Sonra arac sozlüğünün elemanlarını bir döngü ve update() kullanarak başka bir sözlüğe kopyalayasın.
# Kopyalarken, hem orijinal elemanı alsın hem de her bir key'in sonuna "_2" eki ekleyerek yeni bir eleman olarak eklesin.
# Yeni sözlüğümüzün adı yeni_arac olsun. Ve fonksiyon bu sözlüğü dönsün.

# İpuçları:
    # copy()
    # update()
    # items()
    # Örnek Çıktı:

# {'marka': 'Ford',
#  'model': 'Mustang',
#  'yil': 1964,
#  'renk': 'Kırmızı',
#  'fiyat': 30000,
#  'km': 89000,
#  'motor': 1.6,
#  'marka_2': 'Ford',
#  'model_2': 'Mustang',
#  'yil_2': 1964,
#  'renk_2': 'Kırmızı',
#  'fiyat_2': 30000,
#  'km_2': 89000,
#  'motor_2': 1.6}


#  Çözüm 4:


# arac_yarat_4()
def arac_yarat_4():
    arac = dict(
        {
             'marka': 'Ford',
             'model': 'Mustang',
             'yil': 1964,
             'renk': 'Kırmızı',
             'fiyat': 30000,
             'km': 89000,
             'motor': 1.6
        }
    )

    return arac




def yeni_arac_yarat():
    
    # önce arac al
    arac = arac_yarat_4()
    
    # önce direk olarak arac sözlüğünü kopyala
    yeni_arac = arac.copy()
    
    # şimdi arac sözlüğünün elemanlarında dön
    for item in arac.items():
        
        # print(item)
        key = item[0]
        value = item[1]
        
        key += "_2"
        
        yeni_arac[key] = value
        
    return yeni_arac

print(yeni_arac_yarat())

# {'marka': 'Ford',
#  'model': 'Mustang',
#  'yil': 1964,
#  'renk': 'Kırmızı',
#  'fiyat': 30000,
#  'km': 89000,
#  'motor': 1.6,
#  'marka_2': 'Ford',
#  'model_2': 'Mustang',
#  'yil_2': 1964,
#  'renk_2': 'Kırmızı',
#  'fiyat_2': 30000,
#  'km_2': 89000,
#  'motor_2': 1.6}


# 2.yol
def yeni_arac_yarat():
    arac = arac_yarat_4()
    yeni_arac = arac.copy()
    
    for key, value in arac.items():
        
        
        key = key +"_2"
        
        yeni_arac[key] = value
        
        
    return yeni_arac   