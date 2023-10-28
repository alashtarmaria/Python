#-------------------------------------------------------------------------------------------------#
# Fonksiyonlar 1. Sınıf Vatandaştır
# Python'da Fonksiyonlar 1. Sınıf Vatandaştır.
# Yani, Fonksiyonlar da Değişkenler gibi :
                      # 1 atanabilirler
                      # 2 parametre olarak geçilebilir
                      # 3 yeniden değer atanabilir

#--------------------------------------#
# Örnek :
def kup(num):
    out = num**3
    return out
    
print(kup(5))    


# Şimdi yukarıdaki fonksiyonumuzu bir değişkene atayalım
q = kup

# şimdi q'nun tipini görelim
print(type(q))

# şimdi q'yu çağıralım
print(q(5))   

#########################################################################
# q da çağrılınca, birebir kup fonksiyonu ile aynı şeyi yaptı.
# Çünkü, zaten q, kup fonksiyonu demektir.
# Sadece yeni bir ad verdik fonksiyona.
# Buna alising yani yeniden adlandırma denir.
###########################################################################


#--------------------------------------#
# Örnek :
def selamla(metin):
    print(metin)
    

selamla("Selam Sana Python")    
selamla("Merhaba Dünya")


# Şimdi yukarıdaki fonksiyonumuzu bir değişkene atayalım
hello = selamla

hello("Hello World")
hello("Hi there")