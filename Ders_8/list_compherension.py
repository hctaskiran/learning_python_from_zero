from logging.config import listen


sayilar = []
liste = [10,4,7,9,70]


for i in liste:
    i *= 2
    sayilar.append(i)

# [ expression for item in list ]
# sayilar = [i*i for i in range(10)]
# sayilar = [i*2 for i in liste]

isim = "Ahmet"
isimler = ["Ahmet","Ali","Çınar","Deniz"]

sonuc = [c.upper() for c in isim]
sonuc = [str(sayi) for sayi in liste]
sonuc = [i.lower() for i in isimler]

print(sonuc)