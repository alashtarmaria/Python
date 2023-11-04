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