# Alıştırma 9:
# Eğer bir kelimenin harfleri alfabetik sırada ise, bu kelimeye düzgün kelime diyelim.
# İsmi duzgun_kelime_mi olan bir fonksiyon tanımalayalım.
# Eğer kelime, düzgün kelime ise True, değilse False dönsün.
# Düzgün kelime örnekleri: buz, ago

def duzgun_kelime_mi(kelime):
    
    # Python'da alfabetik sıra -> ASCII
    
    # önce ilk harfi önceki kelime olarak alalım
    onceki = kelime[0]
    
    # şimdi harfler üzerinde dönelim
    for harf in kelime:
        
        # bu harf onceki değişkeninin değerinden önce mi geliyor?
        if harf < onceki:
            # eğer harf, öncekinden önce geliyorsa -> düzgün değildir
            return False
        
        onceki = harf
        
    # eğer buraya geldiyse sıralıdır
    return True
    
print(duzgun_kelime_mi('buz'))
# true

print(duzgun_kelime_mi('buz'))
# false




# Alıştırma 10:
# 9 numaralı Alıştırmadaki duzgun_kelime_mi fonksiyonunu kullanarak;
# Lorem kelimelerinden hangilerinin düzgün kelime olduğunu bulalım.

def duzgun_kelime_mi_lorem():
    
    # dosyayı tekrar okuyalım
    file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')
    
    for satir in file:
        
        kelime_dizisi = satir.split()
        kelime = kelime_dizisi[0]
        
        # şimdi bu kelime düzgün kelime mi?
        if duzgun_kelime_mi(kelime):
            print(kelime)

duzgun_kelime_mi_lorem()  
# in
# at
# In
# eu
# et
# dis
# ac
# ex
# a
# Nam
# est
print('N' < 'a')
#True