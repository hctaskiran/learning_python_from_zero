markalar = ["opel","bmw","mercedes"]

# index = 0
# for marka in markalar:
#     print(f"{index}-{marka[index]}")
#     index += 1


obj1 = enumerate(markalar)

print(type(obj1))
print(list(obj1))

for index,value in enumerate(markalar,10):
    print(f"{index+1}-{value}")

liste1 = [1,2,3,4,5]
liste2 = ["a","b","c","d","e"]
liste3 = [100,200,300,400,500]

print(list(zip(liste1,liste2,liste3)))

for item in zip (liste1,liste2):
    print(item)

# for a,b,c in zip(liste1,liste2):
#     print(a,b,c)