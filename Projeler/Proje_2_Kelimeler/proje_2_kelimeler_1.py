# Alıştırma 1:

# Uzunluğu 10 karakterden fazla olan kelimeleri yazalım:

# dosyayı  okuyalım
file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')

for satir in file:
    
    # satir'i kelime dizisine dönüştürelim
    kelime_dizisi = satir.split()
    
    # şimdi kelime_dizisi (tek elemanlı liste) içindeki kelimeyi alalım
    kelime = kelime_dizisi[0]
    
    # 10 karakter kontrolü
    if len(kelime) > 10:
        print(kelime)
    
