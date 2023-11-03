# Alıştırma 6:

# Adı hepsini_kullanir olan bir fonksiyon yazalım.
# Metin ve harfler alacak.
# Eğer metin, verilen harflerin tümünü en az bir kere kullanıyorsa, True, Herhangi bir harfi kullanmıyorsa False.

file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')

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