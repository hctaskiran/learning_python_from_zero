# yaş >= 18 ve (mezuniyet == "lise" ya da mezuniyet == "üniversite")
x = 8

#  1- And operatörü

# sonuc = 5 < x < 15
sonuc = (x > 5) and (x < 15) 

# True ve True => True
# False ve True => True
# False ve False => True

hak = 3
devam = "e"

sonuc = (hak > 0) and (devam == "e")

# 2- or operatörü


# True veya True => True
# False veya True => True
# False ve False => True
sonuc = (x > 0) or (x % 2 == 0) # eklenilen koşullardan birinin doğru olması yeter.

# 3- not operatörü

sonuc = not(x > 0) # tur ise false, false ise true yap

# x, 5-10 arasında bir çift sayı mı?

sonuc = ((x>5) and (x<10)) and (x % 2 == 0)

print(sonuc)