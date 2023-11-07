# Soru 6:

# Parametre olarak bir liste alan bir fonksiyon yazın. Fonksiyonun adı, tuple_sonunu_degistir olsun.
# Bu listenin elemanları birer Tuple olsun.
# Her bir tuple farklı uzunlukta olabilir. Dolayısı ile Listenin elemanlarının uzunlukları sabit değil.
# Yazacağınız fonksiyon, Liste içindeki her bir Tuple elamanının son üyesini silsin, yerine karesini yazsın.

# İpuçları:
    # Liste yerinde değişsin, yani parametre olarak gelen orjinal liste değişsin
    # Tuple'ın son elemanını index ile nasıl alacağınızı düşünün
    # Listenin içinde for ile dönerken, döngüdeki elemanı değiştirseniz de liste değişmez.
    # Listeyi değiştirmenin bir yolunu bulmalısınız (enumerate())
    # Tuple birleştirmeye dikkat ediniz (tek elemanlı bir Tuple nasıl olur?)

# Parametre:
    # tuple_listesi = [(2,5,8), (4,3), (1,7,9,6), (5,)]

# Sonuc:
    # tuple_listesi = [(2,5,64), (4,9), (1,7,9,36), (25,)]

# Çözüm 6:

def tuple_sonunu_degistir(liste):
    
    for index, tup in enumerate(liste):
        
        # önce tuple'in son elemanına kadar al
        son_elemana_kadar = tup[:-1]
        
        # son eleman için -> kare al
        son_eleman = tup[-1]**2
        
        # şimdi bu ikisini birleştir
        tup = son_elemana_kadar + (son_eleman,)
        
        # şimdi yeniden atanmış tup'u listeye geri gönder
        liste[index] = tup
tuple_listesi = [(2,5,8), (4,3), (1,7,9,6), (5,)]
print('Fonksiyondan önce tuple_listesi:', tuple_listesi)

tuple_sonunu_degistir(tuple_listesi)
print('Fonksiyondan sonra tuple_listesi:', tuple_listesi)    

# Fonksiyondan önce tuple_listesi: [(2, 5, 8), (4, 3), (1, 7, 9, 6), (5,)]
# Fonksiyondan sonra tuple_listesi: [(2, 5, 64), (4, 9), (1, 7, 9, 36), (25,)]