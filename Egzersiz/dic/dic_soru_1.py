# Soru 1:
# kelimeler.txt dosyasını okuyan ve buradaki kelimelerden bir dictionary yaratan bir fonksiyon yazın. Fonskiyon sadece 19 karakter ve üstü olan kelimeleri alsın.
# Dictionary'nin key'i kelime olacak, ve değeri de kelimenin harf sayısı yani uzunluğu olacak.
# Fonksiyon'un adı kelimeler_sozlugu olsun ve yarattığı Dictionary'yi dönsün.

# İpucu:
# kelimeler.txt dosyasını okumak için Kelimeler Uygulaması nı tekrar gözden geçirebilirsiniz.

# Örnek Çıktı:
# {'anticonservationist': 19, 
#  'comprehensivenesses': 19, 
#  'counterdemonstration': 20,
#  'counterdemonstrations': 21,
#  ...}

# Çözüm 1:

# Minimum karakter uzunluğu bir sabit (CONSTANT) olduğu için
# bunu bir GLOBAL DEĞİŞKEN de tutalım
MIN_KARAKTER_UZUNLUGU = 19

# Çözüm 1:

# Minimum karakter uzunluğu bir sabit (CONSTANT) olduğu için
# bunu bir GLOBAL DEĞİŞKEN de tutalım
MIN_KARAKTER_UZUNLUGU = 19

def kelimeler_sozlugu():
    
    # boş sözlük yarat
    sozluk = dict()
    
    # kelimeler.txt oku
    dosya = open(r'C:\Users\Marya\Desktop\python\Egzersiz\dic\kelimeler.txt')
    
    # dosya üzerinde döngü ile gezelim
    for i ,satir in enumerate(dosya):
        
        # satir içinde \n, \t gibi karakterler var
        #if i < 20:
        #    print(satir.split())
        #else:
        #    break
        
        satir_dizisi = satir.split()

        kelime = satir_dizisi[0]
        
        # kelime uzunluğuna bak
        if len(kelime) >= MIN_KARAKTER_UZUNLUGU:
            # print(kelime)
            
            if not kelime in sozluk:
                sozluk[kelime] = len(kelime)
    
    return sozluk


sozluk = kelimeler_sozlugu()
print(sozluk)   

# {'anticonservationist': 19,
#  'comprehensivenesses': 19,
#  'counterdemonstration': 20,
#  'counterdemonstrations': 21,
#  'counterdemonstrator': 19,
#  'counterdemonstrators': 20,
#  'counterinflationary': 19,
#  'counterpropagations': 19,
#  'counterretaliations': 19,
#  'disinterestednesses': 19,
#  'electrocardiographs': 19,
#  'extraconstitutional': 19,
#  'hyperaggressiveness': 19,
#  'hyperaggressivenesses': 21,
#  'hypersensitivenesses': 20,
#  'inappropriatenesses': 19,
#  'inconsideratenesses': 19,
#  'interdenominational': 19,
#  'irreconcilabilities': 19,
#  'microminiaturization': 20,
#  'microminiaturizations': 21,
#  'miscellaneousnesses': 19,
#  'multidenominational': 19,
#  'representativenesses': 20}