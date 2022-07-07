print("Merhaba Dünya!")
print('Merhaba')
# print('Ali'nin evi)
print("Ali'nin evi")
print('Ali\'nin evi')
print("Merhaba\nDünya") # alt alta yazar
print("Merhaba\tDünya") # tab tuşu etkisi
print("Merhaba\t\t\tDünya")

mesaj = "Merhaba Dünya"
print(mesaj)

mesaj1 = "Merhaba"
mesaj2 = "Dünya"
print (mesaj1 + " " + mesaj2)

print(mesaj1[0]) # değişken içerisinden spesifik harfi yazma
print(mesaj1[1])
print(mesaj1[-2]) # sondan bir önceki harf
print(mesaj1[0:4]) # 1 ve 4. ve arasındaki harfleri yazma
print(mesaj1[1:4])
print(mesaj1[::2]) # birer harf atlaya atlaya yazma
print(mesaj1[::3]) # ikişer harf atlaya atlaya yazma
print(mesaj1[::-1]) # eldeki metni tersten yazdırma

print(mesaj1.upper())
print(mesaj1)

mesaj1 = mesaj1.upper()
print(mesaj1)
mesaj1 = mesaj1.lower()
print(mesaj1)
mesaj1 = mesaj1.capitalize()
print(mesaj1)

print(mesaj1.startswith("Me"))
print(mesaj1.endswith("a"))
print(len(mesaj1 + mesaj2))
print("Merhaba" + " " + mesaj2)

print("Merhaba" * 10)

isim = "Haktan"
yaş = "21"
print("{} , {} yaşındadır".format(isim, yaş))

isim2 = "Aleyna"
mesaj3 ="merhaba"
print("{} {} dedi...".format(isim2, mesaj3))
print(f"{isim2} {mesaj3} dedi.")