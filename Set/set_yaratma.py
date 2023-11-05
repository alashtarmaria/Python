# Set
#  Önemli: Set'ler sırasız yapılardır. Sıra aranmaz. Index de yoktur.
# Set Yaratma
# Şimdiye kadar, List, Dictionary ve Tuple tiplerini işledik. Şimdi sıra geldi, bir diğer hazır Python Data Structer (Veri Yapısı) olan Set (Küme) tipine.

   # Set'ler birden çok değeri tek bir değişkende tutmak için kullanılır.
   # Set'ler sırasız (unordered) ve indexlenmemiş (unindexed) koleksiyonlardır.
   # Set'ler iki şekilde yaratılır:
      # süslü parantez ile (ama içine eleman vererek)
      # set() constructor'ı ile
   # Set'in elemanları tekildir. (Matematikteki Kümeler gibi)



# Süslü Parantez ile {} Set Yaratmak
# ama süslü parantez boş olursa -> dicitonary yaratır
# süslü parantez içerisine eleman vermek lazım

kume = {}
print(type(kume))
# dict()

kume = {'at', 'kedi', 'köpek', 'at', 'tavşan', 'kedi'}
print(kume)
print(type(kume))
# set


# set() constructor'ı ile küme yaratmak:
# set() -> set({})
harfler = set({'A', 'B', 'C', 'D', 'E'})
print(harfler)


# Set içinde aynı eleman birden fazla yer alamaz.
notlar = ['A', 'A', 'B', 'C', 'B', 'C']
print(notlar)

notlar_seti = set(notlar)
print(notlar_seti)
# ['A', 'A', 'B', 'C', 'B', 'C']
# {'A', 'B', 'C'}

metin = 'Python Veri Tipleri'
print(set(metin))
#  {'l', 'P', 'o', 'h', 'e', 'r', ' ', 'p', 'T', 't', 'n', 'V', 'i', 'y'}

print(notlar_seti)
#  {'A', 'B', 'C'}

notlar_seti[0]
# TypeError: 'set' object is not subscriptable







