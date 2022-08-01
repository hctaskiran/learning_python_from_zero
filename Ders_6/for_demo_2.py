
urunler = [
    {"name": "iphone 8", "price":"4000"},
    {"name": "iphone 8 plus", "price":"5000"},
    {"name": "iphone x", "price":"6000"},
    {"name": "iphone xr", "price":"7000"},
    {"name": "iphone 11", "price":"8000"},
    {"name": "samsung s10", "price":"6000"},
]

# 1- tüm ürün bilgilerini listeleyiniz
'''
for urun in urunler:
    print(f"ürün adı: {urun['name']} ve ürün fiyatı: {urun['price']}")
'''
# 2- ürünlerin fiyatlarının toplamları
'''
toplam = 0
for urun in urunler:
    toplam = toplam + int(urun["price"])
print(f"ürün toplamları: {toplam} TL")
'''
# 3- ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz
'''
for urun in urunler:
    if (int(urun["price"]) <= 6000):
        print (f"ürün adı: {urun['name']} ve ürün fiyatı {urun['price']}")
'''
# 4- kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz
'''
kelime = input("arama istediğiniz ürün: ")

for urun in urunler:
    if (urun["name"].find(kelime.lower()) > -1):
        print(urun["name"])
'''
