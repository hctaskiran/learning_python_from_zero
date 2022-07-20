

opelObj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020,
}

# sonuc = opelObj["marka"]

# for x in opelObj:
#     print(x)

# for x in opelObj:
#     print(opelObj[x])

# for x in opelObj.values():
#     print(x)

# for x,y in opelObj.items():
#     print(x,y)

# sonuc = "marka" in opelObj

# opelObj["renk"] = "kırmızı"
# opelObj.pop("renk")
# opelObj.popitem()
# del opelObj
# opelObj.clear()

obj = opelObj.copy()
obj["marka"] = "mazda"
obj["model"] = "RX7"

opelObj.update({
    "marka": "bmw",
    "model": "520d",
    "renk": "kırmızı"
})

# print(sonuc)
print(opelObj)
print(obj)


