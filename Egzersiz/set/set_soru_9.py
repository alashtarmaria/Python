# Soru 9:

# Parametre olarak iki küme alan bir fonksiyon yazın. Fonksiyonun adı ayni_olanlari_sil olsun.

# Fonksiyon, birinci küme içinden, ikinci küme ile ortak olan elemanları silsin.

# Silme işlemini yerinde yapsın. Yani parametre olarak gelen küme kendisi değişsin.

# İpuçları:

# döngü kullanmayın
# difference_update()
# Parametreler:
# kume1 = {'a', 'b', 'c', 'd', 'e', 'f'}
# kume2 = {'d', 'b', 'e', 'f', 'h', 'g'}

# Sonuç:
# fonksiyon çağırmadan önce kume1: {'c', 'a', 'b', 'f', 'd', 'e'}
# fonksiyon çağırdıktan sonra kume1: {'c', 'a'}

# Çözüm 9:

def ayni_olanlari_sil(s1, s2):
    
    # difference_update() metodu bir kümeyi farkları olarak update eder.
    s1.difference_update(s2)

kume1 = {'a', 'b', 'c', 'd', 'e', 'f'}
kume2 = {'d', 'b', 'e', 'f', 'h', 'g'}

print('fonksiyon çağırmadan önce kume1:', kume1)

ayni_olanlari_sil(kume1, kume2)

print('fonksiyon çağırdıktan sonra kume1:', kume1)    