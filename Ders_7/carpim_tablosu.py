# 1- Çarpım tablosu
'''
for i in range(1,11):
    print("******************")
    for k in range(1,11):
        print("{} x {} = {}".format(i,k,i*k))
'''
# 2- Girilen bir sayının asal olup olmadığını kontrol ediniz.
sayi = int(input("sayi: "))

asalmi = True

if (sayi==1):
    asalmi = False

for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print("sayi asaldır")
else:
    print("sayi asal değil")
    