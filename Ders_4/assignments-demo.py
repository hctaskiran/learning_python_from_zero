a, b, c = 2, 5, 10

#   1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a, b, c toplamı farkı nedir?
'''
x = int(input("x: "))
y = int(input("y: "))

sonuc = (x * y) - (a + b + c)

'''
#   2- c'nin b'ye kalansız bölümünü hesaplayınız.
'''
sonuc = c // b
'''
#   3- (a, b, c) toplamının mod 3'ü nedir?
'''
sonuc = (a+b+c) % 3
'''
#   4- b'nin a. kuvvetini hesaplayınız.
'''
sonuc = (b**a)
'''
#   sayılar = 1, 5, 7, 10, 3
#   5- a, *b, c = sayılar işlemine göre c'nin küpü kaçtır?
'''
sayılar = 1, 5, 7, 10, 3
a, *b, c = sayılar

print(a,b,c)
'''
#   6- a, *b, c = sayılar işlemine göre b'nin değerleri toplamı kaçır?
'''
sayılar = 1, 5, 7, 10, 3
a, *b, c = sayılar

print(b[0] + b[1] + b[2])
'''