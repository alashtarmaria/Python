# Soru 8:

# Parametre olarak 4 liste alan bir fonksiyon yazın. Adı oyuncu_film_karakteri_yil olsun.

# Gelen 4 liste şu şekilde olacak:

# Liste 1 -> Oyuncunun gerçek adı
# Liste 2 -> Filmin Adı
# Liste 3 -> Filmin Çekildiği Yıl
# Liste 4 -> Karakter Adı
# Fonksiyon bu 4 listedeki, karşılıklı elemanları alacak ve 2'şer elemanlı 2 Tuple haline getirecek. Ve geriye bir Dictionary dönecek.

# İlk Tuple -> (Oyuncu Adı, Karakter Adı)
# İkinci Tuple -> (Film Adı, Çekim Yılı)
# Bu Dictionary'nin key'leri İlk Tuple, value'ları ise İkinci Tuple olacak.

# İpuçları:

# zip()
# Parametreler:
# oyuncular = ['Marlon Brando', 'Heath Ledger', 'Natalie Portman', 'Emma Stone']
# karakterler = ['Don Vito Corleone', 'Joker', 'The Swan Queen', 'Mia']
# filmler = ['The Godfather', 'The Dark Knight', 'Black Swan', 'La La Land']
# yillar = [1972, 2008, 2010, 2016]

# Sonuc:
# {('Marlon Brando', 'Don Vito Corleone'): ('The Godfather', 1972),
#  ('Heath Ledger', 'Joker'): ('The Dark Knight', 2008),
#  ('Natalie Portman', 'The Swan Queen'): ('Black Swan', 2010),
#  ('Emma Stone', 'Mia'): ('La La Land', 2016)}

# Çözüm 8:

def oyuncu_film_karakteri_yil(oyuncular, karakterler, filmler, yillar):
    
    # sözlüğümüzü yaratalım
    sozluk = {}
    
    # 4 listeyi tek bir zip() fonskiyonu ile birleştir
    for oyuncu, karakter, film, yil in zip(oyuncular, karakterler, filmler, yillar):
        
        # ikili olarak Tuple haline getirelim -> sozluk'e ekle
        sozluk[(oyuncu, karakter)] = (film, yil)
        

    return sozluk


# listeler:
oyuncular = ['Marlon Brando', 'Heath Ledger', 'Natalie Portman', 'Emma Stone']
karakterler = ['Don Vito Corleone', 'Joker', 'The Swan Queen', 'Mia']
filmler = ['The Godfather', 'The Dark Knight', 'Black Swan', 'La La Land']
yillar = [1972, 2008, 2010, 2016]

# fonksiyonu çağıralım
oyuncu_film_sozluk = oyuncu_film_karakteri_yil(oyuncular, karakterler, filmler, yillar)
print(oyuncu_film_sozluk)