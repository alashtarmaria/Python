
# issubset():
# Bir küme başka bir kümenin alt kümesi mi? issubset()

notlar = ['A', 'A', 'B', 'C', 'B', 'C']
notlar = set(notlar)
print("notlar:", notlar)
#  {'A', 'B', 'C'}


dereceler = ['A', 'L', 'T', 'B', 'F']
dereceler = set(dereceler)
print("dereceler:", dereceler)
# {'A', 'F', 'T', 'B', 'L'}

# notlar'da olup dereceler kümesinde olmayanlar
print(notlar.issubset(dereceler))
# False

print(dereceler.issubset(notlar))
# False

print(set({'F', 'L'}).issubset(dereceler))
# True

print({'A', 'C'}.issubset(notlar))
# True
