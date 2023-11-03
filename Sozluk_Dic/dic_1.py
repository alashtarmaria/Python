# Dictionary¶
# Bir önceki bölümüzde List yapısını görmüştük.

# Bu bölümümüzde ise, Python'un bir diğer hazır veri yapısı olan Dictionary yani Sözlük yapılarını göreceğiz.

# Örneğin çalışanlarımızı tutacağımız bir veri yapısı:

# calisan = {
#     'ad': 'Klark Kent',
#     'yas': 37,
#     'bolum': 'Haber Servisi'
# }
# Dictionary Bir Eşlemedir
# Dictionary'yi, List'in daha genel yapısı olarak düşünebiliriz.

# Listede index'ler tam sayı (int) olmak zorundadır ve Python bu index'leri kendi belirler.

# Dictionary'de ise index'leri biz belirleriz ve sadece tam sayı değil istediğimiz hemen hemen her tür olabilir.

# Dictionary'nin eleman yapısı şu şekildedir:

# { key: value }
# Buna key-value pair yani anahtar-değer ikilisi denir.

# İşte Dictionary, bir anahtarı (key) bir değere (value) eşlediği için, Dictionay'ye bir eşlemedir dedik.

# Dictionary yani Sözlük adının tam karşlığı olarak eşleme yapar.

# Tıpkı İngilizce-Türkçe Sözlük'te olduğu gibi.

# Örneğin bir İngilizce-Türkçe Sözlüğe (ingTRSozluk) bakıp, İngilizce 'hello' kelimesinin Türkçe karşılığını alırsanız aşağıdaki şekilde sonuç döner:

# ingTRSozluk['hello'] = 'selam'
# Çalışan örneğimizde, Dictionary'yi şu şekilde görebiliriz:

               # Key	Value
               # ad	Klark Kent
               # yas	37
               # bolum	Haber Servisi


# Adından da anlaşılacağı gibi, key unique yani tekildir ve aynı key'e (anahtar) ait iki kayıt olamaz.