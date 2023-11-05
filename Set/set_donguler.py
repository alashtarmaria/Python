
# Set Üzerinde Döngü: for ... in ...

notlar = ['A', 'A', 'B', 'C', 'B', 'C']
notlar = set(notlar)
print("notlar:", notlar)
#  {'A', 'B', 'C'}


dereceler = ['A', 'L', 'T', 'B', 'F']
dereceler = set(dereceler)
print("dereceler:", dereceler)
# {'A', 'F', 'T', 'B', 'L'}

for o_not in notlar:
    print(o_not)
    
# A
# C
# B

for d in dereceler:
    print(d)

# A
# F
# T
# B
# L

    