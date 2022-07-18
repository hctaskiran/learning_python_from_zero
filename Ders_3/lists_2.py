diller = ["Python", "JavaScript", "C#", "Java"]

sonuc = diller
# sonuc = type(diller)
# sonuc = diller[0:2]
# sonuc = diller[2:]
# sonuc = diller[2:]
# sonuc = diller[:3]
# sonuc = diller[-1]
# sonuc = diller[-4:-1]
# diller[0] = "HTML"
diller[-1] = "HTML"
sonuc = len(diller)
sonuc = diller + ["Angular", "Vuejs"]

if "Python" in diller:
    print("evet")

for x in diller:
    print(x)

del diller[0]

sonuc = diller

print(sonuc)