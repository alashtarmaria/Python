# Alıştırma 3:

# yasak_harf_var_mi adında bir fonksiyon yaratalım.
# Bu fonksiyon parametre olarak, bir metin ve yasak harfleri içeren bir string alacak.
# Eğer metin içerisinde, bu yasak harflerden herhangi biri varsa, True, hiçbiri yoksa False dönecek.

# dosyayı okuyalım

file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')

def yasak_harf_var_mi(metin, yasak_harfler):
    
    for harf in metin:
        if harf in yasak_harfler:
            return True
    else:
        return False



cumle = 'Bu bir normal metindir.'
yasak = 'ae'
print(yasak_harf_var_mi(cumle, yasak))
# True    

cumle = 'Bu bir normal metindir.'
yasak = 'üö'
print(yasak_harf_var_mi(cumle, yasak))
# False
    