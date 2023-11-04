# Soru 10:

# Key'leri harf ve sayı olarak karışık olan bir sözlük düşününün.

# Örneğin: {'a': 'A', 'b': 'B', 2: 200, 'd': 'D', 5: 300, 'f': 'F', 1: 50}

# Yazacağınız fonksiyon, sadece harf olan key'leri bıraksın, diğerlerini silsin. Yani sadece alfanumerik (alphanumeric) olan key'li elemanları bıraksın.

# Fonksiyonun adı alfanumerik olsun.

# İpuçları:

# Parametre olarak gelen orijinal dictionary'yi değiştirin (yerinde : inplace)
# iki döngü olsun
# döngüler için keys()
# silme için pop()
# alfanumerik mi diye bakmak için str.isalpha()
# dikkat isalpha() bir string (str) fonksiyonudur.
# Parametre sözlük:
# sozluk = {'a': 'A', 'b': 'B', 2: 200, 'd': 'D', 5: 300, 'f': 'F', 1: 50}

# Sonuç:
# sozluk = {'a': 'A', 'b': 'B', 'd': 'D', 'f': 'F'}

# Çözüm 10:

def alfanumerik(sozluk):
    
    # silinecek keyleri tutacak liste
    silinecek_keyler = []
    
    # önce silinecek keyleri al
    for key in sozluk.keys():
        
        if not str(key).isalpha():
            silinecek_keyler.append(key)
    
    # silinecek key'ler üzerinde dön -> dict'ten sil
    for key in silinecek_keyler:
        if key in sozluk.keys():
            sozluk.pop(key)
    


sozluk = {'a': 'A', 'b': 'B', 2: 200, 'd': 'D', 5: 300, 'f': 'F', 1: 50}
print("alfanumerik'i çağırmadan önce sözlük:", sozluk)


alfanumerik(sozluk)
print("alfanumerik'i çağırdıktan sonra sözlük:", sozluk)

# alfanumerik'i çağırmadan önce sözlük: {'a': 'A', 'b': 'B', 2: 200, 'd': 'D', 5: 300, 'f': 'F', 1: 50}
# alfanumerik'i çağırdıktan sonra sözlük: {'a': 'A', 'b': 'B', 'd': 'D', 'f': 'F'}
