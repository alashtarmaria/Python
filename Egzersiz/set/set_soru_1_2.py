# Soru 1:
# Adı kume_yarat_ve_ekle olan bir fonksiyon yazın. Parametre olarak bir liste alsın.
# Bu fonksiyon önce içinde aşağıdaki elemanlar olan bir Set yaratsın.
# "Elma", "Armut", "Karpuz", "Çilek"

# Ardından parametre olarak gelen listenin elemanlarını tek tek bu kümeye eklesin ve kümeyi geri dönsün.

# İpuçları:
# {}
# add()
# Parametre:
# eklenecekler = ['Vişne', 'Kiraz', 'Kayısı', 'Karadut']

# Sonuç:
# {'Vişne', 'Elma', 'Karpuz', 'Karadut', 'Çilek', 'Kayısı', 'Armut', 'Kiraz'

# Çözüm 1:

def kume_yarat_ve_ekle(liste):
    
    # önce setimizi yaratalım
    meyveler = {"Elma", "Armut", "Karpuz", "Çilek"}
    
    # şimdi listenin elemanlarını ekle
    for e in liste:
        meyveler.add(e)
        
    return meyveler    

eklenecekler = ['Vişne', 'Kiraz', 'Kayısı', 'Karadut']

tum_meyveler = kume_yarat_ve_ekle(eklenecekler)

print(tum_meyveler)   



# Soru 2:
# Adı kume_yarat_ve_tek_seferde_ekle olan bir fonksiyon yazın. Parametre olarak bir liste alsın.
# Bu fonksiyon önce içinde aşağıdaki elemanlar olan bir Set yaratsın.
# "Elma", "Armut", "Karpuz", "Çilek"
# Ardından parametre olarak gelen listenin elemanlarını tek seferde bu kümeye eklesin ve kümeyi geri dönsün.

# İpuçları:
# set() constructor'ı
# update()
# Parametre:
# eklenecekler = ['Vişne', 'Kiraz', 'Kayısı', 'Karadut']

# Sonuç:
# {'Vişne', 'Elma', 'Karpuz', 'Karadut', 'Çilek', 'Kayısı', 'Armut', 'Kiraz'}

# Çözüm 2:

def kume_yarat_ve_tek_seferde_ekle(liste):
    
    meyveler = {"Elma", "Armut", "Karpuz", "Çilek"}
    
    # şimdi tek seferde eleman ekle -> update()
    meyveler.update(liste)
    
    return meyveler


eklenecekler = ['Vişne', 'Kiraz', 'Kayısı', 'Karadut']
tum_meyveler = kume_yarat_ve_tek_seferde_ekle(eklenecekler)
print(tum_meyveler)