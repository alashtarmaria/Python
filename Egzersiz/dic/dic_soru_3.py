# Soru 3:

# İsimleri arac_yarat_1, arac_yarat_2 ,arac_yarat_3, arac_yarat_4 olan 4 fonksiyon yazın.

# Bu fonksiyonlar aşağıdaki gibi bir dictionary yaratsın ve dict'in adı arac olsun:
       # {'marka': 'Ford',
       #  'model': 'Mustang',
       #  'yil': 1964,
       #  'renk': 'Kırmızı',
       #  'fiyat': 30000,
       #  'km': 89000,
       #  'motor': 1.6}
# Fonksiyonlar dictionary'yi birbirinden farklı yöntemler ile yaratsın. Fonksiyonlar arac sozlüğünü geri dönsün.

# İpuçları:
    # {}
    # dict()
    # update()    

# Çözüm 3:

# 1. Yol
def arac_yarat_1():
    arac = {}
    arac['marka'] = 'Ford'
    arac['model'] = 'Mustang'
    arac['yil'] = 1964
    arac['renk'] = 'Kırmızı'
    arac['fiyat'] = 30000
    arac['km'] = 89000
    arac['motor'] = 1.6
    
    return arac

print(arac_yarat_1())


# 2. Yol
def arac_yarat_2():
    arac = dict()
    arac['marka'] = 'Ford'
    arac['model'] = 'Mustang'
    arac['yil'] = 1964
    arac['renk'] = 'Kırmızı'
    arac['fiyat'] = 30000
    arac['km'] = 89000
    arac['motor'] = 1.6

    return arac

print(arac_yarat_2())



# 3. Yol
def arac_yarat_3():
    arac = dict()
    arac.update(
        {'marka': 'Ford',
         'model': 'Mustang',
         'yil': 1964,
         'renk': 'Kırmızı',
         'fiyat': 30000,
         'km': 89000,
         'motor': 1.6
        }
    )

    return arac

print(arac_yarat_3())


# 4. Yol
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
print(arac_yarat_4())

