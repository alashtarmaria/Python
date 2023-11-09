# Elimizde iki liste olsun.

# Proramlama Dilleri ve Çıkış Yılları:

# diller = ['Python', 'Java', 'JavaScript', 'C#']
# yillar = [1989, 1995, 1995, 2000]
# Bu iki listeyi dictionary ile birleştireceğiz.
# {'Python': 1989, 'Java': 1995, 'JavaScript': 1995, 'C#': 2000}


diller = ['Python', 'Java', 'JavaScript', 'C#']
yillar = [1989, 1995, 1995, 2000]

# Klasik Yöntem

diller_yillar = {}

for dil, yil in zip(diller, yillar):
    
    diller_yillar[dil] = yil

print(diller_yillar)


# Comprehension

diller_yillar_comp = {dil: yil 
                      for dil, yil in zip(diller, yillar)}

print(diller_yillar_comp)



diller_yillar_comp_2 = {dil:yil for dil, yil in zip(diller, yillar)}
print(diller_yillar_comp_2)