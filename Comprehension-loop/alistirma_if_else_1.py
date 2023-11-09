# 1'den 20'ye kadar olan tek sayıları önce döngü sonra comprehension ile bulalım:

# klasik yöntem -> döngü ile
tekler = []

for i in range(1, 21):
    if i % 2 == 1:
        tekler.append(i)
    
print(tekler)



# comprehension ile
tekler_comp = [i
               for i in range(1, 21)
               if i % 2 == 1]

print(tekler_comp)