# Key Olarak lambda Fonksiyonu

# Bazı hazır Python fonksiyonları, işlemlerini yapabilmek için sizden işlemin nasıl yapılacağını anlatan bir fonksiyon isterler.
# Yani parametre olarak bir fonksiyon isterler.
#  Daha önce lambda fonksiyonu görmüştük. Şimdi lambda fonksiyonu kullanıp çok zor görünen işleri çok rahatça yapacağız.

# Örneğin, sıralama için kullanılan sort() ve sorted() fonksiyonları.

# Bu fonksiyonlar şu şekilde çalışır:
# sort()
    # list.sort(reverse=True|False, key=myFunc)

# sorted()
    # sorted(iterable, key=myFunc, reverse=True|False)


# İşte yukarıdaki iki fonksiyonda da key parametresine geçen myFunc fonksiyonu, işlemin nasıl yapılacağını anlatan fonksiyonlardır.
# Önce normal bir fonksiyon yaratıp onu parametre olarak geçelim, sonra aynı işlemi lambda ile yaparız.
# Örneklerimizde kullanmak için diyelim ki elimizde şu şekilde bir Tuple var:

arabalar = ('Mercedes', 'Audi', 'BMW', 'Porsche', 'VW')

# Örnek: Normal Fonksiyon ile
# Şimdi arabalar Tuple'ını harf uzunluklarına küçükten büyüğe sıralayalım.
# Önce sıralama olarak fonksiyonu normal bir fonksiyon kullanalım:
# önce sıralama fonksiyonunu yaz

def myFunc(e):
    return len(e)

print(myFunc('Audi')) 
# 4   


# Şimdi bu fonksiyonumuzu parametre olarak kullanıp sıralama yaptıralım.
# sorted()
    # sorted() yeni bir liste yaratır
sorted(arabalar, key = myFunc)
# ['VW', 'BMW', 'Audi', 'Porsche', 'Mercedes']

# sort()
  # sort() fonskiyonu listeyi yerinde değiştirir
# arabalar.sort(key = myFunc)
# AttributeError: 'tuple' object has no attribute 'sort'


# sort()
# sort() fonskiyonu listeyi yerinde değiştirir
arabalar_listesi = list(arabalar)
print(arabalar_listesi)

arabalar_listesi.sort(key = myFunc)

print(arabalar_listesi)
# ['Mercedes', 'Audi', 'BMW', 'Porsche', 'VW']
# ['VW', 'BMW', 'Audi', 'Porsche', 'Mercedes']


# Örnek: lambda Fonksiyonu ile
# Şimdi aynı sıralama işlemini, hem sorted() hem de sort() için lambda fonksiyon kullanarak yapalım.
# lambda fonksiyon, tek satır, isimsiz fonksiyondur ve bazı yerlerde çok işe yaramaktadır.
# Biraz önce myFunc olarak yaptığımız işlemi direk aynı satır içinde lambda ile yapacağız:

# sorted()
print(sorted(arabalar, key = lambda x: len(x)))
# ['VW', 'BMW', 'Audi', 'Porsche', 'Mercedes']


# sort()
arabalar_listesi = list(arabalar)
arabalar_listesi.sort(key = lambda x: len(x))
print(arabalar_listesi)
# ['VW', 'BMW', 'Audi', 'Porsche', 'Mercedes']



# Soru:
# Biz şimdiye kadar, sort() ve sorted() fonksiyonları bir key parametresi vermeden kullandık.
# Peki neye göre sıralıyordu o zaman?

# Cevap:
# sort() ve sorted() fonksiyonlarına eğer key parametresi vermezseniz, defult olarak elemanlar üzerinde standart sıralama yapar.

# Standart sıralamadan kasıt;
      # eğer elemanlar sayısal ise sayısal sıralama
      # eğer elemanlar metin (str) ise o zaman alfabetik sıralama

# Örnek:
sayilar = (2, 1, 3, 7, 6, 4, 5)
print(sorted(sayilar)) 


# key parametresini biz verseydik
print(sorted(sayilar, key = lambda x: x))


# Örnek:
harfler = ['c', 'f', 'b', 'a', 'e', 'd']
harfler.sort(key = lambda a: a)
print(harfler)