 # raise hata fırlatır -> Exception
# raise KeyError("Aradığınız değere ait key bulunamadı!")


sozluk = {
    'a': 2,
    'b': 1,
    'c': 4,
    'd': 3,
    'e': 2
}

def tersten_arama(sozluk, deger):
    
    # sozlük içinde dönelim ve bulduğumuz ilk değeri geri dönelim
    for key in sozluk:        
        # bakalım elimizdeki değer -> bu key'e ait değer mi
        if sozluk[key] == deger:
            # bu değeri bulduk -> key dön
            return key
    else:
        # raise hata fırlatır -> Exception
        # raise KeyError("Aradığınız değere ait key bulunamadı!")
        raise LookupError("Aradığınız değere ait key bulunamadı!")
    

deger = 8
anahtar = tersten_arama(sozluk, deger)
print(anahtar)
# LookupError: Aradığınız değere ait key bulunamadı!