# Soru 6:

# Parametre olarak bir sözlük alan bir fonksiyon yazın. Adı numaralari_ve_adlar olsun.

# Parametre olarak gelen sözlük şu şekilde olacak:

# {1: ['Aziz Vefa', 24],
#  2: ['Kaiser Soze', 100],
#  3: ['Zozo The Kid', 45],
#  4: ['Jonny Lash', 70]}
# Fonksiyonunuz sadece numaraları ve adları alarak yeni bir sözlük yaratacak ve bu sözlüğü dönecek.

# Önce for döngüsü sonra comprehension ile yapınız. Comprehension ile fonksiyon adı numaralari_ve_adlar_comp olsun.

# Sonuc:
# {1: 'Aziz Vefa', 2: 'Kaiser Soze', 3: 'Zozo The Kid', 4: 'Jonny Lash'}

# Çözüm 6:

def numaralari_ve_adlar(ogrenci_bilgileri):
    
    adlar_sozlugu = {}
    
    for key, value in ogrenci_bilgileri.items():
        adlar_sozlugu[key] = value[0]
        
    return adlar_sozlugu
    

ogrenci_bilgileri = {1: ['Aziz Vefa', 24], 
                     2: ['Kaiser Soze', 100], 
                     3: ['Zozo The Kid', 45], 
                     4: ['Jonny Lash', 70]}

adlar_sozlugu = numaralari_ve_adlar(ogrenci_bilgileri)
print(adlar_sozlugu)




# dictionary comprehension ile dönelim şimdi

def numaralari_ve_adlar_comp(ogrenci_bilgileri):
    
    return {sira: ad[0] for sira, ad in ogrenci_bilgileri.items()}

ogrenci_bilgileri = {1: ['Aziz Vefa', 24], 
                     2: ['Kaiser Soze', 100], 
                     3: ['Zozo The Kid', 45], 
                     4: ['Jonny Lash', 70]}

adlar_sozlugu = numaralari_ve_adlar_comp(ogrenci_bilgileri)
print(adlar_sozlugu)
