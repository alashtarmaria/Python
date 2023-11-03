# Dictionary'den Eleman Silme
# List'lerde eleman silmek için -> pop() ve del
# Dictionary için de bu metodlar kullanılır.

# pop()
ingTR = {}

ingTR['one'] = 'bir'
ingTR['two'] = 'iki'
ingTR['three'] = 'üç'
ingTR['for'] = 'dört'
ingTR['seven'] = 'yedi'
ingTR['eight'] = 'sekiz'
ingTR['nine'] = 'dokuz'
ingTR['ten'] = 'on'
print(ingTR)
# {'one': 'bir', 'two': 'iki', 'three': 'üç', 'for': 'dört', 'seven': 'yedi', 'eight': 'sekiz', 'nine': 'dokuz', 'ten': 'on'}

ingTR.pop('nine')
print(ingTR)
# {'one': 'bir', 'two': 'iki', 'three': 'üç', 'for': 'dört', 'seven': 'yedi', 'eight': 'sekiz', 'ten': 'on'}

silinen = ingTR.pop('for')
print(silinen)
#  'dört'

del ingTR['ten']
print(ingTR)
# {'one': 'bir', 'two': 'iki', 'three': 'üç', 'eight': 'sekiz'}

# del ingTR['ten']
# print(ingTR)
# KeyError: 'ten'
