# in Operatorü
# Bir karakter ya da metnin başka bir metnin içinde olup olmadığını kontrol etmek için kullanılır.
# Varsa True döner.

agac = 'ahlat ağacı'
at = 'at'


# şimdi 'ahlat ağacı' içinde 'at' kelimesi var mı?
print(at in agac)

print('a' in agac)
print('b' in agac)


if at in agac:
    print(agac + " içinde " + at + ' var.')
else:
    print(agac + " içinde " + at + ' yok.')


# Alıştırma:
# Kullanıcıdan bir metin isteyelim ve metnin içinde 'a' harfi var mı söyleyelim.
# Varsa True, yoksa False döneceğiz.
# Uzun Yol
def a_var_mi():
    
    metin = input("Lütfen bir cümle giriniz: ")
    
    # şimdi bu metin harfleri içinde gezelim
    for harf in metin:
        
        # harf'in a harfi olup olmadığını kontrol et
        if harf == 'a':
            return True
    
    # eğer döngü içerisindeki return'e hiç girmediyse, buraya gelir
    return False


print(a_var_mi())




# Kısa Yol
def a_var_mi():
    
    metin = input("Lütfen bir cümle giriniz: ")
    
    return 'a' in metin


print(a_var_mi())





# En Kısa Yol
def a_var_mi():    
    return 'a' in input("Lütfen bir cümle giriniz: ")


print(a_var_mi())
