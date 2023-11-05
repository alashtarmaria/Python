# Set'lerde Eleman ve Atama İşlemleri
# Set'e Eleman Eklemek: add()

notlar = ['A', 'A', 'B', 'C', 'B', 'C']
notlar = set(notlar)
print(notlar)


dereceler = ['A', 'L', 'T', 'B', 'F']
dereceler = set(dereceler)
print(dereceler)


notlar.add('P')
print(notlar)

notlar.add('Q')
print(notlar)
