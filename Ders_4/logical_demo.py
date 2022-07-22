# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz. 
'''
sayi = int(input("sayi: "))
sonuc = (sayi > 50) and (sayi < 100)
print(f"{sayi} 50 ile 100 arasındadır: {sonuc}")
'''
# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.
'''
sayi = int(input("sayi: "))
sonuc  = (sayi > 0) and (sayi % 2 == 1)
print(f"{sayi} pozitif tek sayıdır: {sonuc}")
'''
# 3-  username ve parola bilgileri ile giriş kontrolü.
'''
_username = "hctaskiran"
_password = "12312"

username = input("kullanıcı adı: ")
password = input("şifre: ")

sonuc = (username == _username) and (password == _password)
print("girilen username ve parola doğru: ", sonuc)
'''
# 4- girilen 3 sayıyı büyüklük olarak karşılaştırınız. 
'''
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

sonuc = (x>y) and (x>z) 
print("x en büyük sayı: ", sonuc)
sonuc = (y>x) and (y>z)
print("y en büyük sayı: ", sonuc)
sonuc = (z>x) and (z>y)
print("z en büyük sayı: ", sonuc)
'''
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
    # Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı
    # a-) Ortalama 50 olsa bile final en az 50 olmalı
    # b-) Finalden 70 alındığında ortalamanın önemi olmasın
'''
vize1 = float(input("vize1: "))
vize2 = float(input("vize2: "))
final = float(input("final: "))

ortalama = (((vize1 + vize2) / 2) * 0.4) + (final * 0.6)
sonuc1 = ortalama >= 50
sonuc2 = (ortalama >= 50) and (final >= 50)
sonuc3 = (ortalama >= 50) or (final >= 70)

print(f"öğrencinin not ortalaması: {ortalama} ve geçme durumu: {sonuc2}")
'''
# 6- Kişinin ad kilo ve boy bilgilerini alıp kilo endeksini hesaplayınız.
    # Formül: (Kilo / Boy uzunluğunun karesi)
    # Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
    # 0-18.4 Zayıf
    # 18.5-24.9 Normalde
    # 25.0-29.9 Fazla kilolu
    # 30.0-34.9 Obez
'''
ad = input("isim: ")
kilo = float(input("kilo: "))
boy = float(input("boy: "))

formul = kilo / (boy ** 2)

zayif = (formul >= 0) and (formul <= 18.4)
normal = (formul >= 18.5) and (formul <= 24.9)
kilolu = (formul >= 25) and (formul <= 29.9)
obez = (formul >= 30.0) and (formul <= 34.9)

print(f"{ad} kilo indeksiniz: {formul} ve kilo değerlendirmeniz: {zayif}")
print(f"{ad} kilo indeksiniz: {formul} ve kilo değerlendirmeniz: {normal}")
print(f"{ad} kilo indeksiniz: {formul} ve kilo değerlendirmeniz: {kilolu}")
print(f"{ad} kilo indeksiniz: {formul} ve kilo değerlendirmeniz: {obez}")
'''





