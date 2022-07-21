#  1- Girilen 2 sayıdan hangisi büyüktür?
'''
sayi1 = int(input("sayi 1: "))
sayi2 = int(input("sayi 2: "))
sonuc = sayi1 > sayi2

print(f"{sayi1} {sayi2} den büyüktür: {sonuc}")
'''
#  2- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
'''
sayi = int(input("sayi: "))
sonuc = (sayi % 2 == 0)

print(f"{sayi} çift sayıdır: {sonuc}")
'''
#  3- Girilen bir sayının negatif pozitif durumunu yazdırın.
'''
sayi = int(input("sayı: "))
sonuc = (sayi > 0)

print(f"Girilen sayı pozitif: {sonuc}")
'''
#  4- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama yapınız.
#       Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
'''
vize1 = float(input("vize 1: "))
vize2 = float(input("vize 2: "))
final = float(input("final: "))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz {ortalama >= 50}")
'''
#  5- Parola ve email bilgisini isteyip doğruluğunu komtrol ediniz.
#       email: hctaskiran@gmail.com / parola: 33231
'''
_email = "hctaskiran@gmail.com"
_parola = "33231"

email = input("email: ")
parola = input("parola: ")

isEmail = (email.lower().strip() == _email)
isParola = (parola.strip() == _parola)

print(f"email doğruluğu: {isEmail} ve parola doğruluğu: {isParola}")
'''