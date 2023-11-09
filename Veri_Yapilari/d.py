def dosyadan_oku(kitap_adi):
    kitap_yolu = kitap_adi + '.txt'
    return open(kitap_yolu, encoding='utf-8')


kitap_adi = 'C:\\Users\\Marya\\Desktop\\python\\Veri_Yapilari\\Pride_and_Prejudice'
pride_kelimeleri = dosyadan_oku(kitap_adi)
print(pride_kelimeleri)