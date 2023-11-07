# Verilen iki listeyi birleştirip, içinde tüm ikili kombinasyonları Tuple olarak tutan yeni bir liste yaratalım:
# listeler
harfler = ['A', 'B']
sayilar = [1, 2, 3]

# Beklenen Sonuç:
# [
#  ('A', 1),
#  ('A', 2),
#  ('A', 3),
#  ...
# ]

# Klasik Yöntem
sonuc = []

for harf in harfler:
    for sayi in sayilar:
        tup = (harf, sayi)
        sonuc.append(tup)
    
print(sonuc)



# Comprehension
sonuc = [(harf, sayi) 
         for harf in harfler 
         for sayi in sayilar]

print(sonuc)
