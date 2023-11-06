# Alıştırma:

# Parametre olarak bir tam sayı listesi alan ve bu listenin minimum, maximum ve aritmetik ortalama değerlerini dönen bir fonksiyon yazın.

# İpuçları:

# ortalama (mean) fonksiyonu için statistics yani istatistik paketini kullanın
# modülü import etmek için -> import

# önce paketleri import edelim
import statistics

def basit_istatistik(liste):
    
    # minimum
    minimum = min(liste)
    
    # maximum
    maximum = max(liste)
    
    # ortalama
    ortalama = statistics.mean(liste)
    
    # return et -> tuple içinde paketleyerek (pack)
    return (minimum, maximum, ortalama)


liste = [1, 2, 3, 4, 5]
minimum, maximum, ortalama = basit_istatistik(liste)

print("min:", minimum)
print("max:", maximum)
print("mean:", ortalama)
# min: 1
# max: 5
# mean: 3