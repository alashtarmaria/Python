 ###############################       Turtle graphics   ################################3
# Kaplumbağa Modülü
# Python içinde hazır olarak gelir.
# https://docs.python.org/3/library/turtle.html

#----------------------------------------------------------------------------------------------------------------------------#

# turtle.mainloop() fonksiyonu, açılan pencereye, kullanıcının her hangi bir işlem yapana
# kadar beklemesini söyler. Bu işlem ekranı kapatmaktır.
# Önemli: turtle.mainloop(), kodun son satırı olmak zorunda.

#----------------------------------------------------------------------------------------------------------------------------#

# **Kaplumbağa Metodları:**
# * **turtle.fd(n)** -> forward    -> ileri hareket ettirir. n pixel kadar. 
# * **turtle.bk(n)** -> backward   -> geri hareket ettirir. n pixel kadar.
# * **turtle.lt(d)** -> left turn  -> sola dön. d açısı kadar.
# * **turtle.rt(d)** -> right turn -> sağa dön. d açısı kadar.

#----------------------------------------------------------------------------------------------------------------------------#


# Örnek 1:
# 90 derecelik bir açı çizelim.

#--------------------------------------------#
# çözüm adımları :
         # turtle.fd(100)
         # turtle.lt(90)
         # turtle.fd(100)
#--------------------------------------------#
# turtle modülünü içeri alalım
import turtle
# Şimdi Kaplumbağa yaratan bir fonksiyon yazalım:
def kaplumbaga_yarat():

    # Turtle nesnesi yarat
    tospik = turtle.Turtle()
    print(tospik)

    return tospik

tospik = kaplumbaga_yarat()     # -- > <turtle.Turtle object at 0x00000231A7ECB450>
# bir kaplumbağa al
tospik = kaplumbaga_yarat()
# kaplumbağayı hareket ettir
tospik.fd(100)
tospik.lt(90)
tospik.fd(100)






