# genelde import işlemleri 

import string
from collections import Counter



# global değişken
# noktalama işaretleri '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

noktalama_isaretleri = string.punctuation


# global değişken
# boşluk karakterleri  ' \t\n\r\x0b\x0c'

bosluk_karakterleri = string.whitespace


# dosyadan file getirme 
def dosyadan_oku(kitap_adi):
    kitap_yolu = kitap_adi + '.txt'
    return open(kitap_yolu, encoding='utf-8')



# başlangıç bölümünü atlar
# bu bölüm okuduğumuz kitaba dahil değildir
def baslangici_atla(file):
    
    atlama_metni = '*** START OF THIS PROJECT'
    
    # file her okumada, okuduğu yere kadar ilerlediği için
    # '*** START OF THIS PROJECT' ile başlayan bölüme kadar okutup
    # çıkarsak, okuma yeri artık, bu ifadenin sonrası olur
    
    for satir in file:
        if satir.startswith(atlama_metni):
            break


# sona gelinip gelinmediği kontrol eden fonksiyon
# bu bölüm okuduğumuz kitaba dahil değildir
def sona_gelindi_mi(satir):
    
    bitirme_metni = '*** END OF THIS PROJECT'
    
    # eğer mevcut satir bitirme metni ile başlıyorsa True dön
    # '*** END OF THIS PROJECT' ile başlayan satır
    
    return satir.startswith('*** END OF THIS PROJECT')




# Satırdaki Kelimeleri Getiren Fonksiyon
def satirdaki_kelimeler(satir):
    
    satir_kelimeleri = []
    
    kelime_dizisi = satir.split()
    
    for kelime in kelime_dizisi:
        
        # eğer kelimede noktalama işareti varsa
        kelime = kelime.strip(noktalama_isaretleri)

        # küçük harf yap
        kelime = kelime.lower()
        
        # alfanumerik mi
        if kelime.isalpha() and len(kelime) > 0:
            satir_kelimeleri.append(kelime)
            
    return satir_kelimeleri



# Kelimeleri Dolduran Fonksiyon
def kelimeleri_doldur(file, kelimeler):
    
    # Python dosyayı satır satır okuyacak
    for satir in file:
        
        # sona gelmiş mi diye bak
        if not sona_gelindi_mi(satir):
            # satir içindeki kelimeleri al
            satir_kelimleri = satirdaki_kelimeler(satir)
            
            # şimdi kelimeler listemize satir_kelimleri
            kelimeler.extend(satir_kelimleri)
    


 # Kitap Okuma Fonksiyonu
def kitap_oku(kitap_adi):
    """
        Verilen kitap adına göre ilgili kitabı okur.
        Parametre: string kitap_adi
        Return: list kelimeler
    """
    
    # kelimeleri tutalım
    kelimeler = list()
    
    # önce file olarak okuylaım
    file = dosyadan_oku(kitap_adi)
    
    # şimdi '*** START OF THIS PROJECT' kısma kadar atlayalım
    baslangici_atla(file)
    
    # şimdi kelimeleri dolduralım
    kelimeleri_doldur(file, kelimeler)
    
    return kelimeler
   

# Şimdi Pride and Prejudice'i okuyalım
kitap_adi = 'C:\\Users\\Marya\\Desktop\\python\\Veri_Yapilari\\Pride_and_Prejudice'
pride_kelimeleri = kitap_oku(kitap_adi)
print("Pride kelimeleri :",pride_kelimeleri[:20])


# Şimdi Alice Adventures in Wonderland'i okuyalım
kitap_adi = 'C:\\Users\\Marya\\Desktop\\python\\Veri_Yapilari\\Alice_Adventures_in_Wonderland'
alice_kelimeleri = kitap_oku(kitap_adi)
print("Alice kelimeleri : ",alice_kelimeleri[:15])



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


# Şimdi Alices Adventures in Wonderland'deki kelimeleri uzundan kısaya sıralayalım
alice_kelimeleri = liste_sirala(alice_kelimeleri, True)
print(alice_kelimeleri[:20])


##############################
# Tekrarları Silelim:
# Tekrarları silen fonksiyon yaz
def tekrarlari_sil(liste):
    
    # tekrarları silmenin en tatlı -> set() -> set döner
    kume = set(liste)
    
    # sonra tekrar list yap
    tekrarsiz_liste = list(kume)
    
    return tekrarsiz_liste


# Şimdi Pride and Prejudice'deki kelimeleri tekarsız görelim
pride_kelimeleri_farkli = tekrarlari_sil(pride_kelimeleri)
print(pride_kelimeleri_farkli[:20])


# Şimdi Alices Adventures in Wonderland'deki kelimeleri tekarsız görelim
alice_kelimeleri_farkli = tekrarlari_sil(alice_kelimeleri)
print(alice_kelimeleri_farkli[:20])