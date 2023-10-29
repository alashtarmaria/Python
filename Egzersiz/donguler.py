# Örnek :
# koduyla ilgili aşağıdakilerden hangisi doğrudur?
sonuc=1

for i in range(4):

    sonuc*=3

print(sonuc)
# for döngüsünde yer alan i, her iterasyonda 3 ile çarpılır.
# i döngü içerisinde hesaba katılmaz. --> doğru cevap





i=0
while(i<10):
    if(i==3 or i==5):
        continue
    print("i: ",i)
    i=i+1
