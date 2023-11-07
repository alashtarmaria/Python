# Alıştırma:

# zip() ve range fonksiyonlarını kullanarak haftanın günlerini bir Dictionary içinde index'leyelim:

# 1: Pazartesi
# 2: Salı
# 3: Çarşamba
# 4: Perşembe
# 5: Cuma
# 6: Cumartesi
# 7: Pazar

# Çözüm:

gun_adlari = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
numaralar = range(1, 8)

gunler = zip(numaralar, gun_adlari)
print(gunler)
# <zip object at 0x0000025CF1A1B140>


# şimdi gunler zip'ni bir Dictionary'ye çevirelim
gunler = dict(gunler)
print(gunler)
# {1: 'Pazartesi', 2: 'Salı', 3: 'Çarşamba', 4: 'Perşembe', 5: 'Cuma', 6: 'Cumartesi', 7: 'Pazar'}


# yukarıdaki örneği tek satır kod ile 

gunler = dict(zip(numaralar, gun_adlari))
print(gunler)
