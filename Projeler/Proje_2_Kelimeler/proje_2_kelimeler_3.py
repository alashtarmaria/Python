# dosyayı okuyalım

file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')

# Şimdi içinde 'ae' harflerinin beraber bulunduğu kelimeleri bulalım:
for line in file :

    char = "ae"

    for satir in file :

        kelime_dizi = satir.split()

        kelime = kelime_dizi[0]

        if char in kelime:
            print(kelime)



    