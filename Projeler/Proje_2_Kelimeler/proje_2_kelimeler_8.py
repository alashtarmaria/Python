# Alıştırma 8:
# Alıştırmadaki sadece_sunlari_kullanir fonksiyonunu ve
# Alıştırmadaki hepsini_kullanir fonksiyonlarını beraber kullanarak:
# Lorem kelimelerinden hangilerinin sadece fir harflerini ama bu harflerin tümünü kullandığını bulalım.

# Fonksiyon adı sadece_tumunu_kullanir olsun.
# 4
def sadece_sunlari_kullanir(metin, harfler):
    
    for harf in metin:
        
        # harf gerçekten harf mi, yoksa noktalama işareti mi? -> isalpha()
        if harf.isalpha() and not harf in harfler:
            return False
    else:
        return True

# 6
def hepsini_kullanir(metin, harfler):
    
    tumunu_kullanir = True
    
    for harf in harfler:
        # eğer herhangi bir harf metin içinde yoksa -> False
        if not harf in metin:
            tumunu_kullanir = False
            
    # döngü bitti
    return tumunu_kullanir
    

            

def sadece_tumunu_kullanir(harfler):
    
    # dosyayı tekrar okuyalım
    file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')
    
    for satir in file:
        
        kelime_dizisi = satir.split()
        kelime = kelime_dizisi[0]
        
        # şimdi bu kelime sadece harfler ama tüm harfleri mi kullanıyor
        if sadece_sunlari_kullanir(kelime, harfler) and hepsini_kullanir(kelime, harfler):
            print(kelime)


harfler = 'fir'
sadece_tumunu_kullanir(harfler)      
# frifirri