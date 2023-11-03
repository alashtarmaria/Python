import random

kelimeler = ["at", "para", "python", "öğrenmek", "video", "sevilay", "öğretmen", "ders"]

def kelime_sec():
    return kelimeler[random.randint(0, len(kelimeler) - 1)]

def kontor_et(kelime, tahmin):
    sonuc = ""
    yeri_hatali = ""
    for i in range(len(kelime)):
        if kelime[i] == tahmin[i]:
            sonuc += kelime[i]
        elif tahmin[i] in kelime:
            if tahmin[i] not in yeri_hatali:
                if tahmin[i] not in sonuc:
                    yeri_hatali += tahmin[i]
            sonuc += "*"
        else:
            sonuc += "*"

    return sonuc, yeri_hatali

def oyuna_basla():
    kelime = kelime_sec()
    sonuc = "*" * len(kelime)
    yeri_hatali = ""
    say = 0
    while True:
        durum = ""
        if yeri_hatali:
            durum = "yeri hatalı harfler : " + yeri_hatali
        say += 1
        print("Son durum = ", say, sonuc, durum)
        mesaj = f"Lütfen {len(kelime)} harfli kelimeyi tahmin et: "
        tahmin = input(mesaj)
        if len(tahmin) != len(kelime):
            print("Verdiğin kelimenin boyu hatalı!")
            say -= 1
            continue
        sonuc, yeri_hatali = kontor_et(kelime, tahmin)
        if sonuc == kelime:
            print("BRAVO! Doğru kelimeyi {} adımda buldun!".format(say))
            break

if __name__ == "__main__":
    oyuna_basla()
