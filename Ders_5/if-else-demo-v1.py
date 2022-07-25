'''
sayi = int(input("sayi: "))

if (sayi>50) and (sayi<100):
    print(f"{sayi} 50 ile 100 arasındadır.")
else:
    print(f"{sayi} 50 ve 100 arasında değil")
'''
#   #   #   #   #   #   #   #   #   #
'''
sayi = int(input("sayi: "))
if (sayi > 0) and (sayi % 2 == 1):
    print(f"{sayi} pozitif ve tek sayıdır.")
else:
    print(f"{sayi} negatif veya tek sayı değil")
'''
#   #   #   #   #   #   #   #   #   #
'''
_username = "hctaskiran"
_password = "12321"

gUsername = input("Kullanıcı adı: ")
gPassword = input("Parola: ")

if (gUsername == _username) and (gPassword == _password):
    print("Kullanıcı adı ve şifre doğru")
else:
    print("Kullanıcı adı veya şifre yanlış")
'''
#   #   #   #   #   #   #   #   #   #
'''
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if (x>y) and (x>z):
    print("x hepsinden büyük")
else:
    print("x en büyük değil")

if (y>x) and (y>z):
    print("y hepsinden büyük")
else:
    print("y hepsinden büyük değil")

if (z>y) and (z>x):
    print("z hepsinden büyük")
else:
    print("z hepsinden büyük değil")
'''
#   #   #   #   #   #   #   #   #   #
