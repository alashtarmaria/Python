# Dictionary'nin Elemanları Üzerinde Dönme

arabalar = {
    'Audi': 'Almanya',
    'Mazda': 'Japonya',
    'Fiat': 'İtalya',
    'Ford': 'Amerika'
}

##############   items(), keys(), values() ###################### 
for araba in arabalar.items():
    print(araba)
    

# destructuring
for marka, ulke in arabalar.items():
    print(marka, "-", ulke)


for k in arabalar.keys():
    print(k)
    

for v in arabalar.values():
    print(v)
    
