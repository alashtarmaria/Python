# Soru 7:

# Parametre olarak bir sözlük alan bir fonksiyon yazın. Adı tek_numarali_adlar olsun.

# Parametre olarak gelen sözlük şu şekilde olacak:

# {1: ['Aziz Vefa', 24],
#  2: ['Kaiser Soze', 100],
#  3: ['Zozo The Kid', 45],
#  4: ['Jonny Lash', 70]}
# Fonksiyonunuz sadece tek numaraları ve adları alarak yeni bir sözlük yaratacak ve bu sözlüğü dönecek.

# İpuçları:

# dongu kullanmayın
# direk comprehension ile yapınız
# Sonuc:
# {1: 'Aziz Vefa', 3: 'Zozo The Kid'}



# Çözüm 7:

# Şimdi tek numaralı adları alalım sadece

def tek_numarali_adlar(ogrenci_bilgileri):
    
    tek_adlar_sozlugu = {key: value[0] 
                         for key, value in ogrenci_bilgileri.items()
                         if key % 2 == 1}
    
    return tek_adlar_sozlugu

ogrenci_bilgileri = {1: ['Aziz Vefa', 24], 
                     2: ['Kaiser Soze', 100], 
                     3: ['Zozo The Kid', 45], 
                     4: ['Jonny Lash', 70]}

tek_adlar_sozlugu = tek_numarali_adlar(ogrenci_bilgileri)
print(tek_adlar_sozlugu)