#------------------------------------------------------------------------#
# Parametre sayısı önceden bilinmiyorsa: *args
#--------------------------------------------#
# Bazen, bir fonksiyonun hangi argumanları (parametreleri) alacağı önceden bilinmez.
# Bu durumda, `*args` şeklinde parametre alır.
# Parametre sayısı önceden bilinmeyen fonksiyon
# *args

#---------------------------------------------------------------#
# Örnek :
# jenerik toplama fonksiyonu
def toplam(*args):
    
    print("args:", args)


toplam(5, 8)
toplam(5, 8, 48, 17, 3)
#---------------------------------------------------------------#
import math
# jenerik toplama fonksiyonu
def toplam(*args):
    
    # print("args:", args)
    return sum(args)


s1 = toplam(5, 8)  
print(s1)


s2 = toplam(5, 8, 48, 17, 3)  
print(s2)

#---------------------------------------------------------------#

def parametreleri_yaz(*args):
    
    for a in args:
        print(a)
    

parametreleri_yaz("A", "B", 45, True, "Python")    