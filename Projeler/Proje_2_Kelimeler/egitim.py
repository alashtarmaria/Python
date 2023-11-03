# open() fonksiyonu ile bir dosya açalım -> file nesnesi verir

# file = open('C:\\Users\\Marya\\Desktop\\python\\Projeler\\Proje_2_Kelimeler\\kelimeler.txt')
file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')

# ilk satırını okuyalım
print(file.readline())
#'Lorem\n'

# ikinci satırı okuyalım
print(file.readline())
#'ipsum\n' 

#  Buradaki özel karakterler:    
    #     \n : yeni satır (new line)
    # \r : enter tuşu (carriage return)


# şimdi tek satırı alıp bir değişkene atayalım
satir = file.readline()
print(satir)
#'dolor\n'

# şimdi satir değişkenini ayıralım -> split()
# split() fonksiyonu, default'ta boşluk karakteri ailesinden ayırma yapar (space, \n, \r, \t ...)
# bu karakterlerden parçalar.
# geriye bir dizi -> list

satir.split()
#['dolor']

# spilt() örneği :
# ['örnek']
d = '\nörnek\t\r'.split()
print(d)

print("##########################################")
# Şimdi gereken parçaları öğrendiğimize göre, ilk 20 kelimeyi okuyalım:

file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')

for index, line in enumerate(file):
    if index <= 20:
        print(line)
# Sonuc :
# Lorem

# ipsum

# dolor

# sit

# amet

# consectetur

# adipiscing

# elit

# Nulla

# sodales

# orci

# sed

# nisl

# tempor

# tristique

# Donec

# commodo

# non

# leo

# quis

# fermentum        
print("##########################################")

file = open(r'C:\Users\Marya\Desktop\python\Projeler\Proje_2_Kelimeler\kelimeler.txt')
for index, line in enumerate(file):
    if index <= 20:
        line = line.split()
        print(line)
    else :
        break    


# ['Lorem']
# ['ipsum']
# ['dolor']
# ['sit']
# ['amet']
# ['consectetur']
# ['adipiscing']
# ['elit']
# ['Nulla']
# ['sodales']
# ['orci']
# ['sed']
# ['nisl']
# ['tempor']
# ['tristique']
# ['Donec']
# ['commodo']
# ['non']
# ['leo']
# ['quis']
# ['fermentum']
