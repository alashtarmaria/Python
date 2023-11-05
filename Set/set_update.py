# Set'e tek seferde, çok sayıda eleman eklemek: update()
# Set'lere update() metodu ile tek seferde, çoklu eleman eklenir.

meyveler = {'elma', 'armut', 'kiraz'}
print(meyveler)
#{'armut', 'elma', 'kiraz'}

daha_cok_meyve = ['çilek', 'muz', 'portakal']
print(daha_cok_meyve)
# ['çilek', 'muz', 'portakal'] 

meyveler.update(daha_cok_meyve)
print(meyveler)
# {'armut', 'elma', 'kiraz', 'muz', 'portakal', 'çilek'}
