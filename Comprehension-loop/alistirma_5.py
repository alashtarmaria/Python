# 'papatya' kelimesinin harflerini bir kümede gösterelim:

papatya = 'papatya'

# Klasik
harfler = set()

for harf in papatya:
    harfler.add(harf)

print(harfler)

# comprehension
harfler = {harf for harf in papatya}
print(harfler)
