# Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içerinsinde saklayınız
# ** ürün sayısını kullanıcıya sorun
# ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun 
# ** ürün ekleme işlemi bittiğinde ürünleri ekrana while ile listeleyin

i = 0
adet = int(input("kaç adet ürün eklemek istiyorsunuz?: "))
urunler = []

while (i<adet):
    urunAdi = input("ürün adı: ")
    fiyat = input("ürün fiyatı: ")
    urunler.append({
        'urunAdi': urunAdi,
        'fiyat': fiyat
    })
    i += 1
    print(urunler)

# for urun in urunler:
#     print(f"ürün afı {urunler['urunAdi']} ürün fiyatı {urunler['fiyat']}")

a = 0
while (a<len(urunler)):
    print(f"ürün afı {urunler[a]['urunAdi']} ürün fiyatı {urunler[a]['fiyat']}")
    a += 1
