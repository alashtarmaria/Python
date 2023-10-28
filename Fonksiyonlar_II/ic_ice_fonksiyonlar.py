### İç İçe Fonskiyonlar - Nested Functions
# Bazen, bir fonksiyonun içinde başka bir fonksiyon tanımalamanız gerekebilir.
# Buna **Nested Functions** denir. (İç İçe fonksiyonlar)


# Örnek:

# İç içe fonksiyonlar kullanıp bir sayının 5 ve 8'in ortak katı olup olmadığını bulalım.

 

def ortak_kat_mi(n):
    """
    Verilen bir sayının hem 5'in hem de 8'in katı olup olamdığını kontrol eder.
    Parametre: n (int)
    Return: Eğer sayı hem 5, hem 8'in katı ise True, değilse False
    """
    
    # İç Fonksiyon 1: 5'e bölünmeyi kontrol edicek
    def besin_kati_mi(n):
        if n % 5 == 0:
            return True
        else:
            return False
    
    
    # İç Fonksiyon 2: 8'e bölünmeyi kontrol edicek
    def sekizin_kati_mi(n):
        if n % 8 == 0:
            return True
        else:
            return False
    
    
    # Hem 5 hem de 8 kontrolüne göre karar ver
    if besin_kati_mi(n) and sekizin_kati_mi(n):
        return True
    else:
        return False    
    


print(ortak_kat_mi(24))
print(ortak_kat_mi(40))
print(ortak_kat_mi(120))
print(ortak_kat_mi(12))
