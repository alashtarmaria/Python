
# Alıştırma 2:

# Şimdi yeni bir fonksiyon yazalım.

# Bu fonksiyon içinde sesli harf bulunmayan tüm kelimeleri bize versin.

# dosyayı okuyalım

file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')


for satir in file:
    
    # İngilizce sesli harfler: a, e, i, o, u
    
    # satir'i kelime dizisine dönüştür
    kelime_dizisi = satir.split()
    
    # şimdi kelime'yi al
    kelime = kelime_dizisi[0]
    
    # tüm seslileri tek tek kontrol et
    if not 'a' in kelime and \
       not 'e' in kelime and \
       not 'i' in kelime and \
       not 'o' in kelime and \
       not 'u' in kelime:
        print(kelime)

# In
# trylyk
# Antryl

# Şimdi içinde 'ae' harflerinin beraber bulunduğu kelimeleri bulalım:
# dosyayı tekrar okuyalım

file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')

for line in file:
    
    # satir'i kelime dizisine dönüştür
    kelime_dizisi2 = satir.split()
    
    # şimdi kelime'yi al
    kelimea = kelime_dizisi2[0]
    
    if 'ae' in kelimea:
        print(kelimea)        

# vitae
# Praesent
# Maecenas