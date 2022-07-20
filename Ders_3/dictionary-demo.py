# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan alacağınız bilgilerle dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gönderin.

urunler = {
    '100': {'ad': 'iphone 8', 'fiyat': '8000'},
    '102': {'ad': 'iphone xr', 'fiyat': '9000'}, 
    '104 ': {'ad': 'iphone 11', 'fiyat': '10000'}
    }

# id = input("id: ")
# ad = input("ad: ")
# fiyat = input("fiyat: ")

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat,
# }

# id = input("id: ")
# ad = input("ad: ")
# fiyat = input("fiyat: ")

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat,
# }

# id = input("id: ")
# ad = input("ad: ")
# fiyat = input("fiyat: ")

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat,
# }

id = input("aramak istediğiniz ürünün id: ")
urun = urunler[id]

print(f'id: {id} ürün adı: {urun["ad"]} ürün fiyat: {urun["fiyat"]}')

# print(urunler)