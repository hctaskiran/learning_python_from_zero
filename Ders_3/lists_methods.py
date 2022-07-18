sayilar = [1,5,8,9,3,45,77]
harfler = ["a","b","e","s","a","y"]

sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = max(harfler)

sayilar.append(10) # sayı ekleme
sayilar.insert(3,5) # 3 numaralalı indexse 5 ekle
sayilar.insert(-1,50)
sayilar.insert(len(sayilar),150)

sayilar.pop() # sondaki elemanı sil
sayilar.pop(0) # en baştakini siler
sayilar.remove(45)
harfler.remove("y")

sayilar.sort()
harfler.sort()
sayilar.reverse()

sayilar.count(5)
harfler.count("a")
sayilar.index(77) # 77 hangi sırada?
sayilar.clear() # siler

sonuc = sayilar

print(sayilar.index(77))