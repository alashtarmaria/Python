def haftanin_gunu():
    sayi =  tamsayi_al("Lütfen gün numarası giriniz (1-7 arasında): ")
    gun = ""
    if sayi < 1 or sayi > 7:
        return haftanin_gunu()
    else :
        if sayi == 1:
            gun = "Pazartesi"
        elif sayi == 2 :
            gun = "Salı" 
        elif sayi == 3:
            gun = "Çaşamba"   
        elif sayi == 4 :
            gun = "Perşembe"   
        elif sayi == 5:
            gun = "Cuma"   
        elif sayi == 6:
            gun = "Cumartesi"   
        else:
            gun = "Pazar" 
    return gun       



haftanin_gunu()