# Stringler immutable veri tipidir.
# Immutable: Elemanlarının değerleri değiştirilemez.

print(type('Hmm o zaman x=5 diyebilir miyiz?'))
print(type("5"))
print(type("5 + 10"))

str = "Bugün Kadıköy'e gidiyorum"
print(str)


# Escape Sequence 
print("Bana \"Bugün ne yapıyorsun\" dedi")
print("hey\nnasılsın")
print("hmm \\")


# String'lerde Değer Atama(Variable Assignment)
merhaba = "Merhaba nasılsın bugün?"
print(merhaba)


# String Concatenation
# + operatörü sayısal veri tipleri üzerine etki edince toplama işlemi yapıyor. Ama uygulandığı objeler string ise yapacağı işlem concatenation (birleştirme) olacak. 
# İki string'i art arta birleştirecek.
# En çok karıştırılan durumlardan biri string olarak ifade edilen sayıları + operatörüne sokmak.
print("5" + "4")

# + operatörünün tek yaptığı birleştirmek, stringlerde boşluk(space) 
# olmadığı için ifadenin sonucu boşluksuz çıktı.
print("hey"+"nasılsın?")
print("hey" + " nasılsın?")

# Anısını değer ataması yaparak da yapabilirdik
# Diyelim ki karşılama mesajı yazmak istiyoruz. İsim ve karşılama kısmını ayrı tutacağız.
# Çünkü belki karşılayacağımız kişinin ismi değişecek ve ben kodumda sadece o değeri 
# değiştirerek karşılama mantığını korumaya devam edeyim istiyorum.
mesaj = "Merhaba"
isim = "Berkay"
print(mesaj + " " + isim)
# Merhaba Berkay
# Bu ifadenin değerini de başka bir değişkende tutabilirdik

karsilama = mesaj + " " + isim
print(karsilama)

 
#  Successive Concatenation(Ardışık Birleştirme)
#  * operatörü sayı objeleri için çarpım olarak tanımlanmışken, stringler için ard arda birleştirme işlemi yapıyor.
print(4 * "hey")
print("1" + "0" * 10)


# len()
# string'in kaç karakterden oluştuğunu öğrenebiliriz (boşluklar da karakter olduğu için onlar da sayılıyor)
print(len("4"))                 # --> 1
print(len("42"))                # --> 2
print(len("hey"))               # --> 3
print(len("hey!"))              # --> 4
print(len("hey nasılsın?"))     # --> 13
print(len(" "))                 # --> 1
print(len(""))                  # --> 0


# Stringlerde İndexleme
# Indexing (Elemanlara Erişme)

# Stringlerin non-scalar veri tiplerine örnek olduğunu biliyoruz. Stringler elemanları karakter olan, alt birim olarak karakterler içeren bir veri tipi.
# Stringler karakterler dizisi olduğu için, bu dizideki spesifik konumdaki elemanlara erişmek isteyebiliriz. Mesela string'in ilk karakteri nedir gibi.
# Bir yapının alt elemanına erişmek için yapacağımız işleme indexing deniyor.
        #  Bunu köşeli parantez [] ile sağlayacağız.


# isim diye bir değişken oluşturup, string'e eşitleyip, ilk elemanına(karakterine) erişelim.
isim = "Deniz"
# 1
print(isim[1])                      # --> e
# 2
print("Deniz"[1])                   # --> e
# Python'da indexler 0dan başlıyor. Yani biz ilk elemana ulaşmak istiyorsak [0] ile sorgulamamız lazım.
print(isim[0])                      # --> D

# Son elemanı elde etmek için [-1] yazabiliriz.
print(isim[-1])                     # --> z


# Deniz 5 karakterden oluşuyor. Indexleri 0,1,2,3,4. Eğer ben 4 ten büyük bir index verirsem 
# o indexte bir elemanı olmadığı için hata alırım.

print(len(isim))
print(isim[4])