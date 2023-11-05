
# Fark:
   # İki set arasındaki fark -> Kümelerin Farkı -> difference
   # 𝐴∖𝐵

notlar = ['A', 'A', 'B', 'C', 'B', 'C']
notlar = set(notlar)
print("notlar:", notlar)
#  {'A', 'B', 'C'}


dereceler = ['A', 'L', 'T', 'B', 'F']
dereceler = set(dereceler)
print("dereceler:", dereceler)
# {'A', 'F', 'T', 'B', 'L'}

# notlar'da olup dereceler kümesinde olmayanlar
print(notlar.difference(dereceler))
# {'C'}

print(dereceler.difference(notlar))
#  {'F', 'L', 'T'}