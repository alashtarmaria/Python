# Dictionary'ler ve List'ler
# Listeler, Dictionary'lerde değer olarak kullanılabilir.

# Örneğin, İngilizce bir kelimenin, Türkçe birden fazla karşılığı olabilir. İşte bu karşılıkları bir liste olarak tutabilirsiniz.

# Yukarıda tanımladığımız, harf_say fonksiyonu harfleri anahtar, adetleri değer olarak tutuyordu.

# {'B': 1, 'u': 1, 'm': 1, 'e': 4, 't': 1, 'i': 2, 'n': 2}
# şeklinde.
# Diyelim ki tersten bir dictionary tutmak istedik. Yani adetler anahtar, harfler değer olsun.

# O durumda, örneğin 1 için birden fazla harf geliyor olacaktı. Ve onları da bir listede tutmamız gerekecekti:

# {1: ['B', 'u', 'm', 't'], 2: ['i', 'n'], 4: ['e']}  
# şeklinde.
# Hadi bu şekilde harfleri liste içinde dönen bir fonksiyon yazalım.

# Önce harf_say fonksiyonuna metin verip sözlük alacak, sonra bu sözlüğü anahtar-değer -> değer-anahtar şeklinde terse çevirecek.


# Çözüm
def harf_say(metin):
    
    # harf ve sayıları tutacak sözlük -> dict
    harfler = dict()
    
    for harf in metin:
        
        # harf istediğimiz için -> isalpha()
        
        if harf.isalpha():
            
            # harf'i harfler sözlüğüne ekle -> içinde var mı?
            # varsa değerini 1 artır
            if harf in harfler.keys():
                harfler[harf] += 1
            
            # yoksa, ilk defa geliyordur -> 1 değeri ile eklenecek
            else:
                harfler[harf] = 1
                
    return harfler
    


def harf_listele(metin):
    
    # önce metin verip sözlük alalım
    sozluk = harf_say(metin)
    
    # boş sözlüğümüzü yaratalım
    # harfler = {}
    harfler = dict()
    
    # şimdi sözlük üzerinde dönelim
    for key in sozluk:
        
        # değerini alalım
        deger = sozluk[key]
        
        # bu değer daha önceden harfler'e eklenmiş mi?
        # in ifadesi ile kontrol et
        if deger not in harfler:
            # yoksa ekle -> liste olarak ekle: []
            harfler[deger] = [key]
        
        # eğer zaten varsa -> listeye append et
        else:
            harfler[deger].append(key)
            
    return harfler


metin = 'Bu metinde hangi harf kaç kere var?'
harfler = harf_listele(metin)
print(harfler)

# {1: ['B', 'u', 'm', 't', 'd', 'g', 'f', 'ç', 'v'],
#  4: ['e', 'a'],
#  2: ['i', 'n', 'h', 'k'],
#  3: ['r']}


# Önemli Not:
# List'ler, Dictionary'lerde value olarak kullanılabilir,
# Ama key olarak kullanılamazlar.

# Örnek :
# bir liste
a = [1, 2]

# bir sözlük
s = dict()

# şimdi bu sözlüğe a listesini key yapıp değer ekleyelim
s[a] = 'hooooop'
# TypeError: unhashable type: 'list'


# Daha önce, Dictionary'nin hashtable yapısını kullandığını söylemiştik, bu da demektir ki,
# key'ler yani anahtarlar hashable olmalı. (Hashlanabilir olmalı.)

# hash, herhangi bir türde bir değer alan ve onun karşılığında size bir tamsayı (integer) dönen bir fonksiyondur.
# İşte Dictionary'ler bu dönen tam sayıları, hash values alır ve key-value değerlerini saklamak için kullanır. Bir nevi index olarak kullanır yani.


# Eğer, Dictionary'nin key'leri immutable (yani değiştirilemez) ise, hiçbir sorun yoktur. Key'ler değişmeyeceği için onlara karşlık gelen hash value de değişmeyecektir.

# Fakat eğer key'leri Mutable olan nesnelerden yaparsanız, o zaman başlar. Neden mi?

# Diyelim ki bir dictionary yarattınız ve key'leri List tipinde (List'leri Mutable yani değiştirilebilir olduğunu hatırlayalım.) Ve Dictionary bu key'ler için hash değerini aldı ve RAM'de bir adrese sakladı.

# Şimdi key'in içinde olan List'in değiştiğini farzedelim. O zaman hash değeri de değişecektir, ve Dictionary bu değişen hash değeri ile eski adresi bulamayacaktır.

# O yüzden, için Mutable Tip'ler, Dictionary'e key olamazlar. Python bunu kesin bir dille yasaklar.
 
# Değişebilen tipler; Dictionary'e Key olamazlar:
         # List
         # Dictionary (kendisi de kendisine key olamaz)
         # Set


# Dictionary'ler ve Key'leri için unutulmaması gereken iki kuralı tekrar hatırlatalım:
    # Key'ler tekil yani unique olmalı. Aynı key bulunamaz.
    # Key'ler Immutable yani Değiştirelemez. Hashtable yapısından ötürü.
             # Key olabilecek tipler: int, float, bool, str, tuple, frozenset         