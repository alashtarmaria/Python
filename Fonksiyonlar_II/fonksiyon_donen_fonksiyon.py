### Fonksiyon Dönen Fonksiyon

def katini_al(n):
    """
    Jenerik çarpma fonksiyonu.
    Parametreler: n (int)
    Return: lambda a: a * n şeklinde bir lambda fonksiyon
    """
    
    return lambda a: a * n


ikili_katlar = katini_al(2)
print(ikili_katlar(15))


uclu_katlar = katini_al(3)
print(uclu_katlar(15))


besinci_katlar = katini_al(5)
print(besinci_katlar(15))

