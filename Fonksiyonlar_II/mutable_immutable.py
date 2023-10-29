### Değiştirebilir x Değiştirilemez (Mutable vs. Immutable)

# Python'da herşey bir nesnedir.
# Ve her nesnenin bir tipi vardır.


# **Immutable**: Bazı tipler atandıkları gibi kalırlar. Yani bir parçası (içinden bir parça) değiştirilemez. (Immutable)
# **Mutable**: Bazı tiplerin ise bir parçasını değiştirebilirsiniz. (Mutable)


# Python'un hazır Tipleri ve bunların Mutable x Immutable durumları:
        # * int : integer -> Immutable
        # * float: float -> Immutable
        # * bool: Boolean-> Immutable
        # * str: String -> Immutable
        # * list: List -> Mutable
        # * tuple: Tuple -> Immutable
        # * dict: Dictionary -> Mutable
        # * set: Set -> Mutable


# Örnek:
# str (metin) veri tipi Immutable bir tiptir -> bir parçası değişemez

metin = 'TALEM'
print(metin)
# ilk elemanı yanlış -> düzeltmek istiyorsunuz
metin[0] = 'K'

# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-68-2f67c8070bc4> in <module>
#       6 
#       7 # ilk elemanı yanlış -> düzeltmek istiyorsunuz
# ----> 8 metin[0] = 'K'

# TypeError: 'str' object does not support item assignment


# **Soru:** Peki bir değiştiremiyorsak, nasıl düzelteceğiz?
# **Cevap:** Tekrar atayacaksınız.

metin = 'KALEM'
print(metin)

print(metin[0])


# **Önemli:** Yeniden atamak Mute (değiştirmek) demek değildir.
metin = 'KİTAP'
print(metin)
