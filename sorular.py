
def flatter(liste):

    bos_liste = []

    for eleman in liste :
        if type(eleman) == list :
            bos_liste.extend(flatter(eleman))

        else :    
           bos_liste.append(eleman)

    return bos_liste  

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatter(liste))


def tersine_cevir(liste):
    bos_liste = []
    for eleman in liste :
        if type(eleman) == list :
            bos_liste.append(tersine_cevir(eleman))
        else :    
            bos_liste.append(eleman)

    return bos_liste[::-1]

liste = [[1, 2], [3, 4], [5, 6, 7]]
print(tersine_cevir(liste))