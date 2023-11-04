# Soru 5:
# Aşağıdaki Dictionary'leri birleştirip ortaya yeni bir dictionary çıkaran ve bunu geri dönen bir fonksiyon yazın.
# Fonksiyon bu 3 dictionary'yi parametre olacak alacak ve adı sozluk_birlestir olacak.

# İpuçları
    # tek bir for döngüsü kullanın
    # update()
    # Birleşek sözlükler:
    # d1={4:120, 7:60}
    # d2={'A': 300, 'B':400}
    # d3={True: 'Doğru', False: 'Yanlış'}

# Olası Sonuç:
   # {4: 120, 7: 60, 'A': 300, 'B': 400, True: 'Doğru', False: 'Yanlış'}


# Çözüm 5:
def sozluk_birlestir(d1, d2, d3):
    
    sozluk = {}
    
    # Python'da birden fazla sözlük üzerinde tek seferde dönebiliriz
    # önce birini bitirip, sonra diğerine geçer
    
    for e in (d1, d2, d3):
        sozluk.update(e)
        
    return sozluk
    

d1={4:120, 7:60}
d2={'A': 'AAA', 'B':'BBB'}
d3={True: 'Doğru', False: 'Yanlış'}

d = sozluk_birlestir(d1, d2, d3)
print(d)   
# {4: 120, 7: 60, 'A': 'AAA', 'B': 'BBB', True: 'Doğru', False: 'Yanlış'}