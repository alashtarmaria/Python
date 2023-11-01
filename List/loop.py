# Liste Üzerinde Dönme

peynirler = ['Ezine', 'Hellim', 'Tulum']
print(peynirler)


# liste üzerinde dönme
for peynir in peynirler:
    print(peynir)



# for ile dönerken index -> enumerate()
# enumerate -> numaralandır
for index, peynir in enumerate(peynirler):
    print("{0} : {1}".format(index, peynir))


# Liste içinde dönerken elemanları değiştirebilirsiniz:
sayilar = [1, 2, 3, 4, 5]
print(sayilar)  

# tekil eleman değiştirir
for sayi in sayilar:
    sayi = sayi * 10
    print(sayi)
    


# listenin kendisini değiştirmek için -> index
# listeyi index ile update et
for index, sayi in enumerate(sayilar):
    # elimizdeki elemanın kopyasını güncelle
    sayi = sayi * 10
    
    # listenin o andaki index'ini update et
    sayilar[index] = sayi

print(sayilar)  



# Her bir peynirin sonuna 'Peyniri' kelimesi ekleyelim
for i, peynir in enumerate(peynirler):
    peynirler[i] = peynir + ' Peyniri'

print(peynirler)   
        