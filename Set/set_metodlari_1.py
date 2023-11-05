# Set Metodları

# Kesişim:
   # İki set'in (kümenin) ortak elemanlarını bulmak -> Kesişim Kümesi -> intersection
   # 𝐴∩𝐵

notlar = ['A', 'A', 'B', 'C', 'B', 'C']
notlar = set(notlar)
print(notlar)
#  {'A', 'B', 'C'}


dereceler = ['A', 'L', 'T', 'B', 'F']
dereceler = set(dereceler)
print(dereceler)
# {'A', 'F', 'T', 'B', 'L'}


print(notlar.intersection(dereceler))
#  {'A', 'B'}

