# List'ler Değiştirilebilir (Mutable)

# Stringler'in değiştirilemez (Immutable) olduğunu gördük.

# List'ler değiştirilebilir (Mutable).
peynirler = ['Ezine', 'Hellim', 'Tulum']
print(peynirler)


# ilk peyniri değiştir
peynirler[0] = 'Beyaz Peynir'
print(peynirler)


sayilar = [1, 2, 3, 4, 5]
print(sayilar)


sayilar[4] = 55555
print(sayilar)

# sayilar[6] 
# IndexError: list index out of range

    #    'Beyaz Peynir', 'Hellim', 'Tulum'  | 'Beyaz Peynir', 'Hellim', 'Tulum'
    #        -3             -2          -1             0              1        2

print(peynirler[-3])
print(peynirler[-1])

