from logging.config import listen


# for item in liste:
#     if (koşul):
#         expression

# [expression for item in liste if koşul]

sayilar = [1,5,8,9,15,44]
sonuc = []

for sayi in sayilar:
    if (sayi%2==0):
        sonuc.append(sayi)

sonuc = [sayi for sayi in sayilar if sayi%2== 0]
sonuc = [sayi if sayi%2==0 else "tek sayı" for sayi in sayilar]

fiyatlar = [1000,3000,5000,0,4000]
vergi = []

for fiyat in fiyatlar:
    if (fiyat > 0):
        vergi.append(fiyat*1.18)

vergi = [fiyat*1.18 for fiyat in fiyatlar if fiyat > 0]
vergi = [fiyat *1.18 if fiyat > 0 else "vergi hesaplanmadı" for fiyat in fiyatlar]

sonuc = []
for x in range(3):
    for y in range(3):
        sonuc.append((x,y))

sonuc = [(x,y) for x in range(3) for y in range(3)]

print(sonuc)
