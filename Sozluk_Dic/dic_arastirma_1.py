# Alıştırma:

# Fonksiyon yaratalım.

# Metnin harflerini saysın, kaç kere geçtiğini bir sözlükte dönsün.

# Ör: {'a': 3, 't': 5, 'c': 2...}

# Çözüm
def harf_say(metin):
    
    # harf ve sayıları tutacak sözlük -> dict
    harfler = dict()
    
    for harf in metin:
        
        # harf istediğimiz için -> isalpha()
        
        if harf.isalpha():
            
            # harf'i harfler sözlüğüne ekle -> içinde var mı?
            # varsa değerini 1 artır
            if harf in harfler.keys():
                harfler[harf] += 1
            
            # yoksa, ilk defa geliyordur -> 1 değeri ile eklenecek
            else:
                harfler[harf] = 1
                
    return harfler

metin = 'Bu metinde hangi harf kaç kere var?'
harf_sozlugu = harf_say(metin)
print(harf_sozlugu)    


# Çözüm 2:
# Pythonic
def harf_say_2(metin):
    
    harfler = dict()
    
    for harf in metin:
        
        if harf.isalpha():
            
            harfler[harf] = harfler.get(harf, 0) + 1
            
    return harfler

print(harf_sozlugu.get('e'))
# 4

# dict.get(key, <yoksa_gelecek_deger>)
# get() bulamazsa, geriye sizin istediğiniz değeri verir
print(harf_sozlugu.get('x', 0))
# 0


metin = 'Bu metinde hangi harf kaç kere var?'
harf_sozlugu = harf_say_2(metin)
print(harf_sozlugu)
# {'B': 1, 'u': 1, 'm': 1, 'e': 4, 't': 1, 'i': 2, 'n': 2, 'd': 1, 'h': 2, 'a': 4, 'g': 1, 'r': 3, 'f': 1, 'k': 2, 
# 'ç': 1, 'v': 1}
