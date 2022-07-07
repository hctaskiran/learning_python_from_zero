# renkler = ["Siyah","Beyaz","Sarı","Mavi","Yeşil"]
# # print(type(renkler))

# # print(len(renkler))

# # print(renkler[1])
# # print(renkler[0])
# # print(renkler[2:])
# # print(renkler[1:4])
# # print(renkler[::2])

# print(renkler)
# renkler.append("Gri") # sona eklerken
# print(renkler)

# renkler.insert(2,"Gri") # araya veya başa eklerken
# print(renkler)

# renkler.remove("Sarı")
# print(renkler)

# # renkler2 = ["Turuncu", "Pembe"]
# # renkler.append(renkler2) # listenin kendisini ekler, içindekiler tek tek eklenmez
# # print(renkler)

# # renkler.extend(renkler2) # elemanları ekler
# # print(renkler)

# silinen = renkler.pop() # en sondaki elemanı silme
# print(silinen)

# # renkler.reverse() # terse çevirir. çevirdikten sonra değişken, sonraki komutlarda çevrilmiş biçimde kalır
# # print(renkler)

# # renkler.sort() # alfabetik sıralama veya büyükten küçüğe
# # print(renkler)

# # renkler.sort(reverse= True) # tersten alfabetik sıralama
# # print(renkler)

# liste2 = sorted(renkler) # liste sırası bozulmadan sıralama
# print(liste2)
# print(renkler)

renkler = ["Siyah","Beyaz","Sarı","Mavi","Yeşil"]
sayılar = [1,2,39,4,3,7,8]
print(min(renkler)) # eğer metin varsa alfabetik olarak en küçük olanı seçer
print(min(sayılar))
print(max(renkler))
print(max(sayılar))

print(sum(sayılar)) # toplamı

for i in renkler: # içindekileri tek tek yazma
    print(i)

print(list(enumerate(renkler))) # sayı ile sıralama yapar
print(list(enumerate(renkler,start=3))) # sıralamaya hangi kelimeden başlaması gerektiğini seçme

print("Siyah" in renkler)
print("Gri" in renkler)

stringrenkler = ",".join(renkler) # birleştirme / bağlama. nokta işaretinin arasına virgül koyarak düzenli sıralama yapılabilir
print(stringrenkler)

renkler2 = stringrenkler.split(",")
print(renkler2)
