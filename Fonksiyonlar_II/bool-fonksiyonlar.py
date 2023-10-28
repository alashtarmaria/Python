#----------------------------------------------------------------------------------#
# **Bool Fonksiyonlar**:
#---------------------------------------#
# Çoğu zaman bir karar verirken doğru yada yanlış olduğunu bilmemiz gerekir.
# İşte bize bu durum içi doğru mu yoksa yanlış mı, sonucunu veren fonksiyonlar tanımalarız.
# Bu tür fonksiyonlara bool fonksiyonlar denir.
# True ya da False döner.

#----------------------------------------------------------------------------------#
# Örnek :
# Sayı tek mi çift mi -> x % 2 == 0 : çift

#---------------------------------------#
# Çift mi fonksiyonu
def cift_mi(x):
    return x % 2 == 0

#---------------------------------------#
# Tek mi fonksiyonu
def tek_mi(x):
    return x % 2 == 1


#---------------------------------------#
odd = tek_mi(11)
print(odd)

#---------------------------------------#
even = cift_mi(7)
print(even)
