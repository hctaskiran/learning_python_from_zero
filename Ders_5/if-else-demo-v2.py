#  bir aracın yakıt tipine göre belirtilen mesafede ne kadar yaktığını hesaplayın



fBenzin = 7.87
fDizel = 5.78

ortYakıtTuketimi = float(input("100 km'de yakılan yakıt litresi: "))
gYol = float(input("Kaç km yol gidiyorsunuz?: "))
yakit = input("Hangi yakıt türü?: ")

tYakitTuketimi = gYol * (ortYakıtTuketimi / 100)
tYakitUcreti = fBenzin * tYakitTuketimi

if (yakit == "benzin"):
    tYakitUcreti = fBenzin * tYakitTuketimi
if (yakit == "dizel"):
    tYakitUcreti = fDizel * tYakitTuketimi
else:
    print("yanlış yakıt türü girdiniz")

print(tYakitUcreti)