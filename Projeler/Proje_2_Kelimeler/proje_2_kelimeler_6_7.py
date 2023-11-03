# Alıştırma 6:

# Adı hepsini_kullanir olan bir fonksiyon yazalım.
# Metin ve harfler alacak.
# Eğer metin, verilen harflerin tümünü en az bir kere kullanıyorsa, True, Herhangi bir harfi kullanmıyorsa False.

def hepsini_kullanir(metin, harfler):
    
    tumunu_kullanir = True
    
    for harf in harfler:
        # eğer herhangi bir harf metin içinde yoksa -> False
        if not harf in metin:
            tumunu_kullanir = False
            
    # döngü bitti
    return tumunu_kullanir
    

            
        
harfler = 'aecbd'
metin = 'Araba demir yolundan geçti'

print(hepsini_kullanir(metin, harfler))
# False

# yukarıda sadece 'c' harfini kullanmıyordu
harfler = 'aecbd'
metin = 'Araba demir yolundan gecti'
print(hepsini_kullanir(metin, harfler))
# True



# Alıştırma 7:
# 6 numaralı Alıştırma'da tanımladığımız hepsini_kullanir fonksiyonunu kullanarak:
# Lorem kelimelerinden hangilerinin aei harflerinin hepsini kullandığını bulalım.
def hepsini_kullanir_lorem(harfler):
    
    # dosyayı okuyalım
    file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')

    for satir in file:
        
        kelime_dizisi = satir.split()
        kelime = kelime_dizisi[0]
        
        # şimdi bu kelime, harfler içindeki harflerin hepsini kullanıyor mu?
        if hepsini_kullanir(kelime, harfler):
            print(kelime)

harfler = 'aei'
print(hepsini_kullanir_lorem(harfler))
# feugiat
# penatibus
# parturient
# venenatis
# vitae
# aliquet
# sapien
# viverra
# vehicula
# habitasse