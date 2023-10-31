# Soru 1:
# Verilen bir metnin tüm kelimelerinin baş harflerini büyük, diğer harflerini ise 
# küçük yapan bir fonksiyon yazın.
# Çözüm 1:

# Uzun Yol
# def sadece_bas_harfler_buyuk(metin):
    
#     # önce hepsini küçük yap
#     kucuk_metin = metin.lower()
    
#     # sonra sadece baş harfleri büyük yap
#     bas_hafr_buyuk_metin = kucuk_metin.title()
    
#     return bas_hafr_buyuk_metin
    
    
# Kısa Yol
def sadece_bas_harfler_buyuk(metin):
    # chain
    return metin.lower().title()
    

duzgun_metin = sadece_bas_harfler_buyuk('makine öĞRENMEsi gÜZELdiR.')
print(duzgun_metin)    



# Soru 2:
# Parametre olarak bir metin, bir de harf alan bir fonksiyon yazın.
# Fonksiyonunuz verilen metnin içinde, verilen harften kaç tane olduğunu geri dönsün.
# Not: Hazır bir python string metodu kullanın ve kodunuz tek satır olsun.
# ipucu: https://docs.python.org/3/library/stdtypes.html#string-methods
# Çözüm 2:
def harf_say(metin, harf):
    return metin.count(harf)

metin = input('lütfen bir metin girin : ')
harf = input('lütfen bir harf girin : ')
print(harf_say(metin, harf) )


# Soru 3 :
# Kullanıcıdan bir cümle isteyin.
# Bu cümle içindeki her bir harfin kaç sefer geçtiğini alt alta print edin.
# Boşluk karakterini yazmayın.
# İpucu: Soru 2'de yazdığınız fonksiyonu kullanın

# Örnek çıktı:
#    'a' harfi 5 sefer geçiyor
#    'd' harfi 1 sefer geçiyor
#    's' harfi 2 sefer geçiyor
# Çözüm 3:
def harfleri_say():
    
    cumle = input("Lütfen bir cümle giriniz: ")
    
    yazilan_harfler = ""
    
    # döngü içinde harfleri tek tek gezelim
    for harf in cumle:
        
        # boşluk mu? -> continue
        if harf == ' ':
            continue
        
        # Bu harf boşluk karakteri değildir kaç defa var
        adet = harf_say(cumle, harf)
        
        # yazdıralım
        # daha önce yazdırıldı belki 
        # eğer yazdırıldı ise -> tekrar yazma
        if not harf in yazilan_harfler:
            print("{0} harfi {1} defa geçiyor".format(harf, adet))
            yazilan_harfler += harf


harfleri_say()


# Soru 7:
# Metnimiz 'Pazartesi Salı Çarşamba' olsun.
# Bu metin üzerinde dilimleme (slicing) kullanarak aşağıdaki sorulara cevap veriniz:
# * Sondan 2. karakter ile sondan 6. karakter arasını bulunuz
# * Sondan 2. karakter (dahil) ile sondan 6. karakter arasını bulunuz
# * 10. index'li karakteri gösteren negatif index'i bulunuz (pozitif ve negatif index'ler toplamı dizinin uzunluğunu verir)
# * Son karakter hariç tüm karakterleri bulunuz
# * İlk ve Son karakter hariç, tüm karakterleri bulunuz
# Çözüm 7:
metin = 'Pazartesi Salı Çarşamba'


# Sondan 2. karakter ile sondan 6. karakter arasını bulunuz
metin[-6:-2]

# Sondan 2. karakter (dahil) ile sondan 6. karakter arasını bulunuz
metin[-6:-1]


###############3
# 10. index'li karakteri gösteren negatif index'i bulunuz
# pozitif ve negatif index'ler toplamı dizinin uzunluğunu verir
uzunluk = len(metin)
print("uzunluk:", uzunluk)

# 10. index'teki
print("10. indexteki karakter:", metin[10])

# negatif index değeri
negatif_index = uzunluk - 10

# index'ler mutlak değer -> negatif yap
negatif_index = -negatif_index

# negatif index'teki karakteri yaz
print('{}. indexteki karakter: {}'.format(negatif_index, metin[negatif_index]))

# Şimdi 10. index'teki karakter ile negatif_index'teki karakter eşit mi?
if metin[10] == metin[negatif_index]:
    print("{} ile {} indexteki karakterler eşit".format(10, negatif_index))
else:
    print("{} ile {} indexteki karakterler eşit değil".format(10, negatif_index))
#############################33

# Son karakter hariç tüm karakterleri bulunuz
metin[:-1]

# İlk ve Son karakter hariç, tüm karakterleri bulunuz
metin[1:-1]



# Soru 8:
# Aşağıdaki şekilde bir fonksiyon yazınız:
# Kullanıcıdan bir email adresi isteyiniz.
# Bu mail adresini, index yapısı kullanarak kullanıcı adı ve domain adı olarak ayırınız.
# Not: Kullanıcı adı ve domain adı '@' karakteri ile ayrılır. Eğer email adresi '@' karakteri içermiyorsa, kullanıcıya 'Uygunsuz email formatı' mesajı dönünüz.
# Çözüm 8:
def email_ayir():
    
    email = input("Lütfen bir email giriniz: ")
    
    # '@' karakterinin index'ini bulalım
    bolme_noktasi = email.find('@')
    
    # find() -> bulamazsa -1 döner
    if bolme_noktasi == -1:
        print("Uygunsuz email formatı")
    else:
        print("Kullanıcı Adı:", email[:bolme_noktasi])
        print("Domain Adı:", email[bolme_noktasi+1:])

email_ayir()    



# Soru 9:
# Aşağıdaki şekilde bir fonksiyon yazınız:
# Kullanıcıdan bir cümle istesin ve cümlenin tersten yazılmış olarak dönsün.
# Çözüm 9:
def ters_cevir():
    
    cumle = input('Lütfen bir cümle giriniz: ')
    
    return cumle[::-1]

print(ters_cevir())



# Soru 10:
# Aşağıdaki şekilde bir fonksiyon yazınız:
# Kullanıcıdan bir cümle içindeki her bir karakteri alfabeden sıradaki karakter ile değiştirsin.

# Yapılacaklar:

# İç içe fonksiyonlar kullanın.
# İçeride harf_kucuk_mu() ve harf_buyuk_mu() şeklinde harfin küçük ya da büyük olduğunu veren fonksiyonlar olsun.
# İlgili alfabe ve bir harf alıp, o alfabede o harften sonra gelen harfi bulan, siradaki_harf() fonksiyonu olsun.
# Alfabeler:
# alfabe_kucuk = 'abcçdefgğhıijklmnoöprsştuüvyz'
# alfabe_buyuk = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
# Metinden ilgili harfi almak için index kullanın.
# Beklenen Sonuç:
# AraBaCı  ->  BsbCbÇi

# Çözüm 10:
def siradaki_harfle_degistir():
    
    cumle = input('Lütfen bir cümle giriniz: ')
    
    alfabe_kucuk = 'abcçdefgğhıijklmnoöprsştuüvyz'
    alfabe_buyuk = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    
    yeni_cumle = ""
    
    # İç Fonksiyonları tanımla
    def harf_kucuk_mu(harf):
        return harf in alfabe_kucuk
    
    def harf_buyuk_mu(harf):
        return harf in alfabe_buyuk
    
    def siradaki_harf(alfabe, harf):
        index = alfabe.find(harf)
        return alfabe[index+1]
    
    # cümle içindeki harfler üzerinde döngü
    for harf in cumle:
        # harf küçük mü, büyük mü?
        if harf_kucuk_mu(harf):
            yeni_harf = siradaki_harf(alfabe_kucuk, harf)
        elif harf_buyuk_mu(harf):
            yeni_harf = siradaki_harf(alfabe_buyuk, harf)
        # harf küçük ya da büyük harf değilse, o zaman kendisini döneriz
        else:
            yeni_harf = harf
        
        # yeni harfi yeni_cumle
        yeni_cumle += yeni_harf
        
    return yeni_cumle
    