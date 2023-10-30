# Tersten Dilimleme (Geri Dilimleme)
# Dizi dilimleme işlemleri, bazen geriye doğru yapılır.

# Geriye Dilimleme:
     # dizi[bitiş : başlangıç : -artış]
     # Sondan başa doğru gelir
     # Son elemanın index'i -1 dir (0 değil)


rakamlar = '123456789'
print(rakamlar)


# rakamlar dizisini tersten başa doğru sıralayalım
print(rakamlar[::-1])


# rakamları baştan sonra ikişer atlayarak yazın
print(rakamlar[::2])



# rakamları sondan başa ikişer atlayarak yazın
print(rakamlar[::-2])




# rakamlar    |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |

#             >>>>>>>>>>>
# index       |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |

#             <<<<<<<<<<<
# ters index  | -9  | -8  | -7  | -6  | -5  | -4  | -3  | -2  | -1  |


# Normal Index ile '456' ve '654' dilimlerini alalım



# normal index ------->
# 456 için -> 3. index'ten başla, 6. index'e kadar gel (6 dahil eder) -> 3, 4, 5
print(rakamlar[3:6:1])


# ters index <--------
# 456 için -> -6. index'ten (dahil) başlar, -3. index'e (hariç) kadar git -> -6, -5, -4
print(rakamlar[-6:-3:1])


# Ters Index ile 654 ü alalım
print(rakamlar[-4:-7:-1])