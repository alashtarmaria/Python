# 'lorem impsum' ifadesinin harflerini büyük harfler yapıp bir listeye ekleyelim.

text = 'lorem ipsum'

# Klasik Yöntem

buyuk = []

for t in text:
    buyuk.append(t.upper())
    
print(buyuk)
# ['L', 'O', 'R', 'E', 'M', ' ', 'I', 'P', 'S', 'U', 'M']


# Comprehension

buyuk_comp = [t.upper()
              for t in text]

print(buyuk_comp)
# ['L', 'O', 'R', 'E', 'M', ' ', 'I', 'P', 'S', 'U', 'M']
