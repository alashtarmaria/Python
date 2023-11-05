# Soru 10:

# Parametre olarak iki küme alan bir fonksiyon yazın. İsmi hangisi_üst_kume olsun.

# Eğer birinci küme, ikincinin üst kümesi ise fonksiyon kume bilgisi ile bunu dönsün:

# 'birinci {.....} kümesi, ikinci {.....} kümesinin üst kümesidir' diye dönsün Eğer tersi ise:
# 'ikinci {.....} kümesi, birinci {.....} kümesinin üst kümesidir' diye dönsün
# İpuçları:

# döngü kullanmayın
# issuperset()
# Parametreler:
# kume1 = {'a', 'b', 'c', 'd'}
# kume2 = {'d', 'b', 'e', 'f', 'a', 'c'}
# Sonuç:
# "ikinci {'c', 'a', 'b', 'f', 'd', 'e'} kümesi, birinci {'b', 'c', 'd', 'a'} kümesinin üst kümesidir"

# ----------------------------
# Parametreler:
# kume1 = {'d', 'b', 'e', 'f', 'a', 'c'}
# kume2 = {'a', 'b', 'c', 'd'}
# Sonuç:
# "birinci {'c', 'a', 'b', 'f', 'd', 'e'} kümesi, ikinci {'b', 'c', 'd', 'a'} kümesinin üst kümesidir"

# Çözüm 10:

def hangisi_üst_kume(kume1, kume2):
    
    if kume1.issuperset(kume2):
        return 'birinci {0} kümesi, ikinci {1} kümesinin üst kümesidir.'.format(kume1, kume2)
    else:
        return 'ikinci {0} kümesi, birinci {1} kümesinin üst kümesidir.'.format(kume2, kume1)
    

kume1 = {'a', 'b', 'c', 'd'}
kume2 = {'d', 'b', 'e', 'f', 'a', 'c'}
print(hangisi_üst_kume(kume1, kume2))


kume1 = {'d', 'b', 'e', 'f', 'a', 'c'}
kume2 = {'a', 'b', 'c', 'd'}
print(hangisi_üst_kume(kume1, kume2))
