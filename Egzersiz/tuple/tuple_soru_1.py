# Soru 1:

# Aşağıdaki şekilde bir fonksiyon yazın. Adı tuple_yarat olsun.
# Fonksiyonumuz önce içinde 1'den 10'a kadar değerlerin olduğu bir Tuple yaratsın.
# Ardından bu Tuple'a 11'den 20'ye kadar olan sayıları eklesin ve Tuple'ın son halini dönsün.

# İpuçları:
    # Tuple'lar Immutable'dır. O Tuple'a nasıl yeni eleman eklenir?
    # for döngüsü ve range() kullanın

# Sonuc: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

# Çözüm 1:
# 1.yol
def tuple_yarat():
    
    # önce bir tuple yarat
    tup = (1,2,3,4,5,6,7,8,9,10)
    
    # şimdi tuple'a değer ekle
    for i in range(11, 21):
        
        # Tuple Immutable olduğuna göre -> direk değer ekleyemeyiz
        # önce değer eklenmiş yeni bir tuple yaratıp -> eski tuple'a yeniden atama yapıcaz
        yeni_tup = tup + (i,)
        tup = yeni_tup
        
    return tup


# 2.yol
def tuple_yarat():
    
    t = (1,2,3,4,5,6,7,8,9,10)
    
    for eleman in range(11,21):
        t = t+ (eleman,)
           
    return t

t = tuple_yarat()
print(t)