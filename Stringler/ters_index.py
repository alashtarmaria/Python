#### Ters Index (Negatif Index)

# Soldan sağa giden index' normal index veya index denir ve 0'dan başlar.
# Sağdan sola gelen index'e ters index veya negatif index denir ve -1'den başlar.
# Diyelim ki rakamlar'ın sadece son elemanını almak istiyoruz: 123456789
rakamlar = '123456789'
print(rakamlar)


# son elemanı normal index ile alalım
print(rakamlar[8])


# son elemanın ters index'i -1 dir
print(rakamlar[-1])


s = 'Derin Öğrenme'
print(s)

# Yani
# baştan sona (soldan sağa) giderken index 0 ile başlar
# sondan başa (sağdan sola) gelirken index -1 ile başlar


# s          |  D  |  e  |  r  |  i  |  n  |     |  Ö  |  ğ  |  r  |  e  |  n  |  m  |  e  |  

#            >>>>>>>>>>>
# index      |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  |

#            <<<<<<<<<<<
# ters index | -13 | -12 | -11 | -10 | -9  | -8  | -7  | -6  | -5  | -4  | -3  | -2  | -1  |



# son harf 
print(s[12])
print(s[-1])


# ilk harf
print(s[0])
print(s[-13])


# 6. index (soldan)
print(s[6])
print(s[-7])


# Ters index'in aklınızda kalması için şöyle düşünebilirsiniz:
# Artı ve eksi index'lerin mutlak değelerinin toplamları (işaretsiz) her zaman dizinin uzunluğuna (len) eşittir.

# Ör: -3 ve 10 aynı elemandır
print(s[-3])
print(s[10])


# Ör: -6. index'teki eleman hangisidir?
print(s[-6])
print(s[7])


# Negatif index'leri daha kolay okumak için pratik yol:
   # Dizinin sol tarafına kendisini yazarız.
   # Dizinin ilk başı zaten sıfır'dır.
   # Sola gelenler de sayı doğrusu üzerinde, -1, -2, -3 şeklinde devam eder.


dizi = 'Python'
print(dizi)


# dizi       |  P  |  y  |  t  |  h  |  o  |  n  |  P  |  y  |  t  |  h  |  o  |  n  |  

#                                             <<<   |   >>>

# index      | -6  | -5  | -4  | -3  | -2  | -1  |  0  |  1  |  2  |  3  |  4  |  5  |