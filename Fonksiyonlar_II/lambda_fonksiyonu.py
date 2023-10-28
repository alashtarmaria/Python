######################################################################################
#--------------------------------------------#

# Lambda Fonksiyonu : lambda
# **lambda** fonksiyonu (lambda expression) **tek satır fonksiyonu** olarak da bilinir.
#--------------------------------------------#

# Bazen, bir fonksiyonu isim vermeden direk kullanmak isteyebiliriz.
# Bunun için `lambda` anahtar kelimesi kullanılır.

#--------------------------------------------#
# Örnek :
metin = "Selam sana Kartal Gözü"
print(metin.split()) 
# ['Selam', 'sana', 'Kartal', 'Gözü']

#--------------------------------------------#
# Örnek :
metni_parcala = lambda x: x.split()

metni_parcala(metin)

print(metni_parcala("Python Deep Learning"))
# ['Python', 'Deep', 'Learning']

#--------------------------------------------#
# Örnek :
# Çarpma yapan bir lambda fonksiyonu tanımlayalım
multiply = lambda x, y: x * y

print(multiply(4, 8))
print(multiply(10, 6))

#--------------------------------------------#
# Üstel hesaplama yapan bir lambda fonksiyon
ustel = lambda sayi, ust: sayi**ust

print(ustel(2, 5))
print(ustel(4, 3))