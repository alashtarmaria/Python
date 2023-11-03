# Tersten Arama 

# Dictionary ile alakalı örneklerimizde hep anahtar (key) ile arama yaptık. Bir key ile arayıp değeri bulmaya çalıştık.
# Şimdi diyelim ki, tersinden yani değer ile arayıp key'i (anahtarı) bulmaya çalışalım.
# Normalde, Dictionary'nin yapılma amacı bu değildir. Dolayısı ile yapacağımız arama işleminde iki büyük sorun var bizi bekleyen:
     # Aynı değeri gösteren birden fazla anahtar olabilir Bu durumda ya ilkini döneriz ya da tümünü içeren bir liste dönmemiz lazım.
     # Maalesef, bu tersten arama işlemi için basit bir yöntem yok. Dolayısı ile search'ü kendimiz yazmak zorundayız.     

def tersten_arama(sozluk, deger):
    
    # sozlük içinde dönelim ve bulduğumuz ilk değeri geri dönelim
    for key in sozluk:
        
        # bakalım elimizdeki değer -> bu key'e ait değer mi
        if sozluk[key] == deger:
            # bu değeri bulduk -> key dön
            return key
    

sozluk = {
    'a': 2,
    'b': 1,
    'c': 4,
    'd': 3,
    'e': 2
}    

deger = 2
anahtar = tersten_arama(sozluk, deger)
print(anahtar)
# a

deger = 8
anahtar = tersten_arama(sozluk, deger)
print(anahtar)
# None

# Diyelim ki, None dönmek yerine hata fırlatsak: 'Aradığınız değere ait key bulunamadı!'
print(sozluk['c'])
# 4

# print(sozluk['k'])
# KeyError: 'k'


def tersten_arama(sozluk, deger):
    
    # sozlük içinde dönelim ve bulduğumuz ilk değeri geri dönelim
    for key in sozluk:        
        # bakalım elimizdeki değer -> bu key'e ait değer mi
        if sozluk[key] == deger:
            # bu değeri bulduk -> key dön
            return key
    else:
        # raise hata fırlatır -> Exception
        # raise KeyError("Aradığınız değere ait key bulunamadı!")
        raise LookupError("Aradığınız değere ait key bulunamadı!")
    

# deger = 8
# anahtar = tersten_arama(sozluk, deger)
# print(anahtar)
# LookupError: Aradığınız değere ait key bulunamadı!



# Bu örnekte ilk defa raise yapısını görüyoruz. Raise ifadesi bir Exception yani programatik hata oluşturur. Bu örnekte biz LookupError tipinde bir Exception döndürdük.
# Arama işlemlerinin başarısız olduğunu göstermek için genelde LookupError kullanılır.
# Bu şekilde hata fırlatmanın güzel tarafı bu fonksiyonu çağıran kodların hatanın yerini ve sebebini takip edebilmeleri (trace etmek).
# İlerleyen derslerde Exception Handling yani Hata Ayıklama bölümünde detaylı bir şekilde işleyeceğiz bu konuları. Şimdilik bu kadar yeterli.


# Önemli Not: 
   # Python Dictionary'leri hashtable yapısını kullandığı için çok güçlü yapılardır.
   # Ama bu güç, eğer doğru arama yaparsanız yani key ile ararsanız geçerli.
   # Eğer dictionary'yi değer ile aramaya çalışırsanız, bu hem performans kaybı hem de hatalara açık hale getirir kodunuzu.   
   # Çok dikkat edilmelidir.