# Birleşim:
   # İki set'in (kümenin) birleşimi -> Birleşim Kümesi -> union
   # 𝐴∪𝐵

notlar = ['A', 'A', 'B', 'C', 'B', 'C']
notlar = set(notlar)
print(notlar)
#  {'A', 'B', 'C'}


dereceler = ['A', 'L', 'T', 'B', 'F']
dereceler = set(dereceler)
print(dereceler)
# {'A', 'F', 'T', 'B', 'L'}


print(dereceler.union(notlar))
#  {'A', 'B', 'C', 'F', 'L', 'T'}
