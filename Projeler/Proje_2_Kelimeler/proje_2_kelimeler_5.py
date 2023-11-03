# Alıştırma 5:

# 4 numaralı alıştırma'daki fonksiyonu kullanarak:
# Lorem kelimelerinden sadece 'ens' harflerini kullanan kelimeleri bulalım.

def lorem_sadece_sunlari_kullanir(harfler):
    
    # dosyayı tekrar okuyalım
    file = open('kelimeler.txt')
    
    for satir in file:
        
        kelime_dizisi = satir.split()
        kelime = kelime_dizisi[0]
        
        if sadece_sunlari_kullanir(kelime, harfler):
            print(kelime)
    
harfler = 'ens'
print(lorem_sadece_sunlari_kullanir(harfler)    )