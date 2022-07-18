# 1- "Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"
# 2- Kaç elemanlı?
# 3- İlk ve son eleman?
# 4- S5'i S9 ile değiştir.
# 5- S6 listenin elemanı mı?
# 6- -3 indexindeki değer?
# 7- Listenin ilk 2 elemanı?
# 8- Son 2 eleman yerine S9 ve S10 ekle.

# 1. soru
samsungTelefon = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"] 

# 2. soru
sonuc = len(samsungTelefon) 

# 3. soru
sonuc = samsungTelefon[0] 
sonuc = samsungTelefon[-1]

# 4. soru
sonuc = samsungTelefon[0] = "Samsung S9"

# 5. soru
if "Samsung S6" in samsungTelefon:
    print("evet")

# 6. soru
sonuc = samsungTelefon[-3]

# 7. soru
sonuc = samsungTelefon[0:2]

# 8. soru
samsungTelefon[-2:] = ["Samsung S9", "Samsung S10"]
sonuc = samsungTelefon

# 9. soru
sonuc = samsungTelefon + ["Iphone X","Iphone XR"]

# 10. soru
del samsungTelefon[-1]
sonuc = samsungTelefon

# 11. soru
sonuc = samsungTelefon[::-1]

# 12. soru
ogrenciA = ["Yiğit", "Bilgi", 2010,[70,60,70]]
ogrenciB = ["Sena", "Turan", 1999,[80,80,70]]
ogrenciC = ["Ahmet", "Turan", 1998,[80,70,90]]

ogrenciler = [ogrenciA, ogrenciB, ogrenciC]

for ogrenci in ogrenciler:
    print(f"{ogrenci[0]} {ogrenci[1]}")

# 13. soru
for x in samsungTelefon:
    print(x)

print(sonuc)