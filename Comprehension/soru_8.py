# Soru 8:

# Parametre olarak İngilizce bir metin alan bir fonksiyon yazınız. Fonksiyonun adı kelime_uzunluklari olsun.

# Fonksiyon iki liste dönsün. Listelerden biri kelimeleri içersin. Diğer liste ise kelime uzunluklarını.

# Eğer kelime ('the', 'in', 'as', 'at') kelimelerinden biri ise onu almasın.

# İpuçları:

# bir fonksiyon nasıl iki liste döner? -> Tuple
# döngü kullanmayın
# comprehension ile yapın
# Parametre:
# "It takes all the running you can do, to keep in the same place. If you want to get somewhere else, you must run at least twice as fast as that!"

# Sonuc:
# ['It', 'takes', 'all', 'running', 'you', 'can', 'do,', 'to', 'keep', 'same', 'place.', 'If', 'you', 'want', 'to', 'get', 'somewhere', 'else,', 'you', 'must', 'run', 'least', 'twice', 'fast', 'that!']
# [2, 5, 3, 7, 3, 3, 3, 2, 4, 4, 6, 2, 3, 4, 2, 3, 9, 5, 3, 4, 3, 5, 5, 4, 5]

# Çözüm 8:

def kelime_uzunluklari(metin):
    
    #önce kelimeleri alalım
    kelimeler = metin.split()
    
    # yasak kelimeler 
    yasaklar = ('the', 'in', 'as', 'at')
    
    # comprehension
    kelime_listesi = [kelime 
                      for kelime in kelimeler 
                          if kelime not in yasaklar]
    uzunluklar = [len(kelime) 
                  for kelime in kelimeler 
                      if kelime not in yasaklar]
    
    return (kelime_listesi, uzunluklar)

# Alice Harikalar Diyarında kitabından şu metni verelim.

alice_in_wonderland = """It takes all the running you can do, to keep in the same place. 
If you want to get somewhere else, you must run at least twice as fast as that!"""

print(alice_in_wonderland)



# fonksiyonu çağıralım ve tuple olarak dönen değerleri ayrı ayrı listelere atayalım
kelimeler, uzunluklar = kelime_uzunluklari(alice_in_wonderland)

# şimdi bu listeleri yazdıralım

print(kelimeler)
print(uzunluklar)


# Bu arada Alice Harikalar Diyarında'dan verdiğimiz bu enfes metnin Türkçesi şu :)
# Gördüğün gibi burada, bütün gücünle koşarsan ancak durduğun yerde durursun. 
# Başka bir yere ulaşmak için bundan en azından iki kat fazla koşmalısın!