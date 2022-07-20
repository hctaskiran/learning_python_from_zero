# thisdict = { 
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# print(thisdict)

# key - value

# 41 => Kocaeli
# 34 => İstanbul

sehirler = ["Kocaeli", "İstanbul"]
plakalar = [41,34]

# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])

# print(sehirler.index("İstanbul"))
# print(plakalar[sehirler.index("İstanbul")])
# print(plakalar[sehirler.index("Kocaeli")])

# plakalar =  {"Kocaeli": 41, "İstanbul": 34}

# print(plakalar["Kocaeli"])
# print(plakalar["İstanbul"])

# plakalar["Rize"] = 53
# plakalar["İzmir"] = 36
# plakalar["İzmir"] = 35

# print(plakalar)

ogrenciler = {
    100: {
        "ad": "Çınar",
        "soyisim": "Bayıltır",
        "yas": 31,
        "notlar": [70,80,70]
    },
    101: {
        "ad": "Ada",
        "soyisim": "Bayıldı",
        "yas": 18
    }
}

sonuc = ogrenciler[100]
sonuc = ogrenciler[101]["ad"]
sonuc = ogrenciler[100]["notlar"]

sonuc = (ogrenciler[100]["notlar"][0] + ogrenciler[100]["notlar"][1] + ogrenciler[100]["notlar"][2]) / 3

print(sonuc)

