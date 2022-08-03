# 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
# "random modülü" için "python random" şeklinde arama yapın
# 100 üzerinden puanlama yapın her soru 20 puan
# hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın

import random

sayi = random.randint(1,10)

hak = 5
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("tahmin: "))

    if sayi == tahmin:
        print(f"{sayac}. seferde bildiniz")
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşağı")

    if hak == 0:
        print(f"hakkınız bitti. Tutulan sayı: {sayi}")






