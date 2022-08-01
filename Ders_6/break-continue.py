name = "Haktan Can taşkıran"

# for harf in name:
#     if (harf == "n"):
#         break
#     print(harf)

# i = 0
# while (i < 5):
#     i += 1
#     if (i == 3):
#         continue
#     print(i)

# print("döngü bitti")

# 1 ve 100 arasındaki çift sayıların toplamı

i = 1
toplam = 0

while (i <= 100 ):
    if (i %2 == 1):
        continue
    toplam += i
    i += 1
    

print(f"toplam: {toplam}")