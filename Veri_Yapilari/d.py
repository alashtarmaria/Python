def dosyadan_oku(kitap_adi):
    kitap_yolu = kitap_adi + '.txt'
    return open(kitap_yolu, encoding='utf-8')


kitap_adi = 'C:\\Users\\Marya\\Desktop\\python\\Veri_Yapilari\\Pride_and_Prejudice'
pride_kelimeleri = dosyadan_oku(kitap_adi)
print(pride_kelimeleri)


##############################
# Kelimeleri Uzunluk Sırasına Dizelim:


# Listleri sıralayan fonksiyon
def liste_sirala(liste, azalan_mi):
    
    # uzunluk ile sıralayacaksak -> key parametresini vermemiz lazım -> lambda
    return sorted(liste, reverse=azalan_mi, key = lambda x: len(x))


# Şimdi Pride and Prejudice'deki kelimeleri kısadan uzuna sıralayalım
pride_kelimeleri = liste_sirala(pride_kelimeleri, False)
print(pride_kelimeleri[:20])


# Şimdi Pride and Prejudice'deki kelimeleri uzundan kısaya sıralayalım
pride_kelimeleri = liste_sirala(pride_kelimeleri, True)
print(pride_kelimeleri[:20])
