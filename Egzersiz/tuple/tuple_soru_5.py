# Soru 5:

# Tuple üzerinde dilimleme işlemleri daha önce String ve List'lerde gördüğümüz gibidir.

# Elimizde şu şekilde bir Tuple olsun:

#  tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j') 
# Aşağıdaki sorulara slicing yani dilimleme ile (index bazlı) cevap veriniz:

# 4'cü eleman (dahil) ile 7'ci eleman (dahil) arasını bulun
# İlk 5 elemanı bulun
# 6'cı elemandan (dahil) sonrasını bulun
# Tüm elemanları bulun
# Sondan 2. elemanı bulun
# Son 4 elemanı bulun
# 2'ci elemandan başlayıp, 8'ci elemana kadar 2'şer atlayarak yazın
# Tüm elemanları 3'er atlayarak yazın
# 9'uncu elemandan, 3'cü elemana (hariç) kadar tersten yazın
# tup'u tersten yazın
# tup'u tersten 2'şer atlayarak yazın
# Son elemana (hariç) kadar olan tüm elemanlarını ters index ile alınız

# Çözüm:

tup = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j') 
print(tup)
# Her soru kendi hücresi içinde cevaplandı 
# ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

# 1.soru
# 4'cü eleman (dahil) ile 7'ci eleman (dahil) arasını bulun
# 4. eleman -> index 3 demektir (index 0 dan başlar)
# 7. eleman dahil olduğuna göre son 7 olacak (son dahil değildir dilimlemede)
print(tup[3:7])
# ('d', 'e', 'f', 'g')

# 2.soru
# İlk 5 elemanı bulun
print(tup[:5])
# ('a', 'b', 'c', 'd', 'e')


# 3.soru
# 6'cı elemandan (dahil) sonrasını bulun
print(tup[5:])
# ('f', 'g', 'h', 'i', 'j')


# 4.soru
# Tüm elemanlar)ı bulun
print(tup[::])
# ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

# 5.soru
# Sondan 2. elemanı bulun
print(tup[-2])
# 'i'

# 6.soru
# Son 4 elemanı bulun
print(tup[-4:])
# ('g', 'h', 'i', 'j')


# 7.soru
# 2'ci elemandan başlayıp, 8'ci elemana kadar 2'şer atlayarak yazın
print(tup[1:8:2])
# ('b', 'd', 'f', 'h')


# 8.soru
# Tüm elemanları 3'er atlayarak yazın
print(tup[::3])
# ('a', 'd', 'g', 'j')

# 9.soru
# 9'uncu elemandan, 3'cü elemana (hariç) kadar tersten yazın
print(tup[8:2:-1])
# ('i', 'h', 'g', 'f', 'e', 'd')

# 10.soru
# tup'u tersten yazın
# ('j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')
print(tup[::-1])

# 11.soru
# tup'u tersten 2'şer atlayarak yazın
# ('j', 'h', 'f', 'd', 'b')
print(tup[::-2])

# 12.soru
# Son elemana (hariç) kadar olan tüm elemanlarını ters index ile alınız
print(tup[:-1])
# ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')