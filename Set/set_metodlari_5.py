
# issuperset():
# Bir küme başka bir kümenin üst kümesi mi? issuperset()
notlar = ['A', 'A', 'B', 'C', 'B', 'C']
notlar = set(notlar)
print("notlar:", notlar)
#  {'A', 'B', 'C'}


dereceler = ['A', 'L', 'T', 'B', 'F']
dereceler = set(dereceler)
print("dereceler:", dereceler)
# {'A', 'F', 'T', 'B', 'L'}

print(dereceler.issuperset(notlar))
# False

print(dereceler.issuperset(set({'F', 'L'})))
# True

print(notlar.issuperset({'A'}))
# True
