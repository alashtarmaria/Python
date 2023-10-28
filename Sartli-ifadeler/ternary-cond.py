#---------------------------------------------------------------------------------------------------------------------------#
# Ternary Conditionals

# Ternary Conditionals aslında daha önce yapamadığımız bir şeyi yapabilmemize olanak sağlamayacak. if-else mantığını tek satırda kullanıp döndürülecek, 
# sonucu ona göre belirlememizi sağlayacak.

# Diyelim ki belirli bir durumu test edip, x değişkeninin değerini bu testin sonucuna göre belirlemek istiyorum. 
# Soruya cevabım "y" olursa değeri 2'ye, yoksa 0'a eşitleyeceğim.


#---------------------------------------------------------#
# cevap olarak "y" (yes) veya "n"(no) vereceğiz
cevap = input("x in değeri 2 olsun mu? y/n : ")
if cevap == "Y": 
    x = 2
else:
    x = 0

print(x)

#---------------------------------------------------------#
# tek sarırda yazalım 

cevap = input("x in değeri 2 olsun mu? y/n  ")
x = 2 if cevap=="y" else 0
print(x)


#---------------------------------------------------------#
