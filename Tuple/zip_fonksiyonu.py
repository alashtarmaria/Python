# zip() Fonksiyonu
# Python'da List ve Tuple tipleri beraber kullanıldıklarında çok işlevesel olurlar.
#  Bunu detaylı görmek için önce zip() fonksiyonunu inceleyelim:

# zip() Python içinde hazır bir fonksiyondur.

# İki veya daha fazla Dizi (index ile erişilebilen tipler: List, Tuple, String, Range) tipinde değişken alır.
# Zip yani fermuar fonksiyonu adından da anlaşılacağı gibi, her bir dizideki 
# karşlıklı elemanları alarak bir tuple oluşturur. Böylece tuple'lardan oluşan bir zip nesnesi döner.
metin = 'xyzt'
liste = [1, 2, 3, 4]

# metin ve listeyi zip'leyelim

fermuar = zip(metin, liste)

print(fermuar)
# <zip object at 0x000001B5E3BB05C0>

# zip() fonksiyonun geriye döndüğü zip nesnesi bir iterator döner.

# Iterator'ler içinde sayılabilir değerler tutan ve üzerinde döngü kurulabilen 
# (iterate olabilen) nesnelerdir.

# Iteratorler, Listelere benzer fakat List'ler gibi onların üzerinde index ile işlem 
# yapamazsınız.


# fermuar nesnesi bir iterator -> döngü kuralım
# fermuar dişleri üzerinde
for dis in fermuar:
    print(dis)

# ('x', 1)
# ('y', 2)
# ('z', 3)
# ('t', 4)    

# Görüğünüz gibi, fermuar içindeki her bir eleman bir Tuple.
# Ve her Tuple'in ilk elemanı metin dizisinden, ikinci elemanı liste dizisinden.
# Böylece elemanlar kaşlılıklı olarak (aynı index'teki) birbirine fermuarlandı.


# index ile zip() çağıralım
# fermuar[0]
# TypeError: 'zip' object is not subscriptable


# Eğer zip nesnesini List olarak almak ve index'lemek istersek -> list()
fermuar_listesi = list(fermuar)
print(fermuar_listesi)
# []



# Nasıl olur diyorsunuz değil mi? Bir yukarıda aynı işlem bir tuple listesi vermişti, 
# şimdi ise boş bir liste verdi?

# Bunun sebebi, Python'da iterator'lerin iterate etme yani elemanları üzerinde dönme 
# işlemini bir kere yapıyor olmalarıdır.

# Dönme işlemi bir kere yapılıp tamamlandıktan sonra, iterator artık boş listeye döner.

# Bunun da amacı sonsuz döngüyü engellemektir.

# list() işlemi yapmak da aslında üzerinde dönmek demek, dolayısı ile o da sadece bir
# kere yapılabilir.

# Soru:
# Peki zip() fonksiyonuna parametre olan gelen iki dizi eğer aynı uzunlukta değilse
# ne olacak?

# Cevap: 
# Kısa olan dizi kadar zip olurlar.
d1 = ['A', 'B', 'C', 'D', 'E']
d2 = [10, 20, 30]

yeni_fermuar = zip(d1, d2)
print(yeni_fermuar)
# <zip object at 0x000001B5E3CF60C0>

# yeni_fermuar zip'ini liste yap
yeni_fermuar_listesi = list(yeni_fermuar)
print(yeni_fermuar_listesi)
# [('A', 10), ('B', 20), ('C', 30)]


# For ile Dönerken, Tuple alma:
# yeni_fermuar_listesi elemanlarını tek tek alalım

for dis in yeni_fermuar_listesi:
    print(dis)

# ('A', 10)
# ('B', 20)
# ('C', 30)




for d1_eleman, d2_eleman in yeni_fermuar_listesi:
    
    print("d1'den gelen: {},  d2'den gelen: {}".format(d1_eleman, d2_eleman))
    
# d1'den gelen: A,  d2'den gelen: 10
# d1'den gelen: B,  d2'den gelen: 20
# d1'den gelen: C,  d2'den gelen: 30


# Alıştırma:
# Verilen iki listedeki karşılıklı elemanları kontrol edelim.
# İkisi de eşitse yazdıralım:
l1 = ['a', 'B', 'C', 'd', 'e', 'F']
l2 = ['A', 'B', 'c', 'd', 'E', 'F']

for e1, e2 in zip(l1, l2):
    
    if e1 == e2:
        print(e1)

# B
# d
# F        