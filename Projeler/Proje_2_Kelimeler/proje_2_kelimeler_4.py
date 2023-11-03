# Alıştırma 4:
#============#
# Adı sadece_sunlari_kullanir olan bir fonksiyon tanımlayalım.
# Parametresi, metin ve harflerden oluşan iki string olsun.
# Eğer metin, sadece bu harfleri kullanıyorsa, True dönecek.
# Bu harfler dışında başka bir harf kullanıyorsa, False dönecek.

file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')

def sadece_sunlari_kullanir(metin, harfler):
    
    for harf in metin:
        
        # harf gerçekten harf mi, yoksa noktalama işareti mi? -> isalpha()
        if harf.isalpha() and not harf in harfler:
            return False
    else:
        return True
  

cumle = 'ey edip adanada pide ye'
harfler = 'adeinpy'
print(sadece_sunlari_kullanir(cumle, harfler))
# True

print(set('ey edip adanada pide ye'))
# {'a', 'i', 'y', 'd', 'n', ' ', 'p', 'e'}

cumle = 'ey edip adanada pide ye k'
harfler = 'adeinpy'
print(sadece_sunlari_kullanir(cumle, harfler))
# False


# =======================================================================================#

# Alıştırma 5:
#============#
# 4 numaralı alıştırma'daki fonksiyonu kullanarak:
# Lorem kelimelerinden sadece 'ens' harflerini kullanan kelimeleri bulalım.

def lorem_sadece_sunlari_kullanir(harfler):
    
    # dosyayı tekrar okuyalım
    file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')
    
    for satir in file:
        
        kelime_dizisi = satir.split()
        kelime = kelime_dizisi[0]
        
        if sadece_sunlari_kullanir(kelime, harfler):
            print(kelime)
    
harfler = 'ens'
lorem_sadece_sunlari_kullanir(harfler)

# sesse
# nesnes
# senesses
