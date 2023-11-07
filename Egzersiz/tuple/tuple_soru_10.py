# Soru 10:

# Parametre olarak sayılardan oluşan bir Tuple ve bir sayı alan bir fonksiyon yazın. Adı kac_kere_var olsun.

# Fonksiyon, Tuple içinde verilen sayının kaç kere geçtiğini versin.

# Bunu yaparken Soru 4'teki kac_kere_geciyor fonksiyonunu kullansın. Kendi bir hesaplama yapmasın yani.

# Eğer bu Tupple içinde sayı yoksa, 'Sayı bulunumadı' diye hata dönsün.

# İpuçları:

# fonksiyon dönen fonksiyon
# raise
# index()


# Parametreler:
# tup = (5, 2, 3, 3, 4, 2, 1, 3, 4, 5, 2, 1, 2)
# sayi = 2

# Sonuc:
# 4




# kac_kere_geciyor():
def kac_kere_geciyor(tup, index):
    
    # bu index'teki elemanı bul
    eleman = tup[index]
    
    # Tuple'in count() fonksiyonu var
    # verilen eleman Tuple içinde kaç kere geçtiğini verir
    return tup.count(eleman)

# Çözüm 10:

def kac_kere_var(tup, sayi):
    
    # Tuple içinde sayı var mı?
    if not sayi in tup:
        raise Exception('Sayı bulunamadı!')
    else:
        # Soru 4'te kac_kere_geciyor(tup, index) fonksiyonu bu işi yapıyordu
        # fakat index istiyordu
        
        # tuple.index(sayi) -> bulduğu ilk index'i döner
        index = tup.index(sayi)
        
        # fonksiyon'u çağır -> gelen değeri return et
        return kac_kere_geciyor(tup, index)
    
tup = (5, 2, 3, 3, 4, 2, 1, 3, 4, 5, 2, 1, 2)
sayi = 2

print(kac_kere_var(tup, sayi))
