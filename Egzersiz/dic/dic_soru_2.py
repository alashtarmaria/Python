# Soru 2:

# kelimeler.txt dosyasını okuyan ve buradaki kelimelerden bir dictionary yaratan bir fonksiyon yazın. Fonskiyon sadece 19 karakter ve üstü olan kelimeleri alsın.

# Dictionary'nin key'i karakter sayısı (uzunluk) olacak, ve değeri de bu karakter sayısına sahip kelimeleri içeren bir liste (List) olacak.

# Fonksiyon'un adı uzunluk_kelimeler olsun ve yarattığı Dictionary'yi dönsün.

# İpucu:

# kelimeler.txt dosyasını okumak için Kelimeler Uygulaması nı tekrar gözden geçirebilirsiniz.

# Örnek Çıktı:
# {19: ['anticonservationist', 'comprehensivenesses', 'counterdemonstrator', ...], 
#  20: ['counterdemonstration', 'counterdemonstrators', 'hypersensitivenesses', ...],
#  21: ['counterdemonstrations', 'hyperaggressivenesses', 'microminiaturizations']}


# Çözüm 2:
# global değişken
MIN_KARAKTER_UZUNLUGU = 19

def uzunluk_kelimeler():
    
    # boş sözlük yarat
    sozluk = dict()
    
    # kelimeler.txt oku
    dosya = open(r'C:\Users\Marya\Desktop\python\Egzersiz\dic\kelimeler.txt')
    
    # dosya üzerinde döngü ile gezelim
    for i ,satir in enumerate(dosya):
        
        satir_dizisi = satir.split()

        kelime = satir_dizisi[0]
        
        uzunluk = len(kelime)
        
        # uzunluk kontrolü
        if uzunluk >= MIN_KARAKTER_UZUNLUGU:
            
            # bu uzunluk'u sözlüğe ekle
            if not uzunluk in sozluk:
                sozluk[uzunluk] = [kelime]
            else:
                sozluk[uzunluk].append(kelime)
                
    return sozluk


sozluk = uzunluk_kelimeler()
print(sozluk)     
# {19: ['anticonservationist',
#   'comprehensivenesses',
#   'counterdemonstrator',
#   'counterinflationary',
#   'counterpropagations',
#   'counterretaliations',
#   'disinterestednesses',
#   'electrocardiographs',
#   'extraconstitutional',
#   'hyperaggressiveness',
#   'inappropriatenesses',
#   'inconsideratenesses',
#   'interdenominational',
#   'irreconcilabilities',
#   'miscellaneousnesses',
#   'multidenominational'],
#  20: ['counterdemonstration',
#   'counterdemonstrators',
#   'hypersensitivenesses',
#   'microminiaturization',
#   'representativenesses'],
#  21: ['counterdemonstrations',
#   'hyperaggressivenesses',
#   'microminiaturizations']}