# Python'da yapı itibari ile dizi olan tipler (str, list...) 
# için uzunluk len() fonksiyonu ile bulunur.

# Örnek :
print(len("Python"))

# Örnek :
dizi = [1, 2, 3, 'A', 'B']
print(len(dizi))


# Örnek:
# Kullanıcıdan bir metin isteyip, uzunluğunu dönelim.

metin = input("Lütfen bir metin giriniz: ")

# aldığımız metnin uzunluğuna bakalım
uzunluk = len(metin)

print(uzunluk)