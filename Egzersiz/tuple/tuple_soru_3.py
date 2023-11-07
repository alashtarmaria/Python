# Soru 3:

# Parametre olarak verilen bir String'i önce List'e sonra da bu List'i Tuple'a dönnüştüren bir fonksiyon yazın.
# Adı string_to_list_to_tuple olsun ve Tuple'ı geri dönsün.

# İpuçları:
     # sadece constructor metodlarını kullanın
     # list()
     # tuple()

# Parametre:
    # python_babasi = 'Guido van Rossum'

# Sonuc:
#  ('G', 'u', 'i', 'd', 'o', ' ', 'v', 'a', 'n', ' ', 'R', 'o', 's', 's', 'u', 'm')

# Çözüm 3:

def string_to_list_to_tuple(metin):
    
    # önce String'i List'e çevir
    liste = list(metin)
    
    # şimdi de list'i Tuple'a çevir
    tup = tuple(liste)
    
    return tup
    

python_babasi = 'Guido van Rossum'
baba_tuple = string_to_list_to_tuple(python_babasi)
print(baba_tuple)    