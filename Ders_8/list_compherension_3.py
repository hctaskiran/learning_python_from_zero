isimler = ["Ahmet","Ali","Çınar","Deniz"]
string = "Hello 33231 World"
yillar = [1983,1999,2008,1956,1986]
derece = [20,5,15,-2,0,6]

# 1- 1-100 arasındaki sayılardan 12 e tam bölünebilen sayı listesi
'''
sonuc = [i for i in range (1,101) if i%3==0 if i%4==0]
'''
# 2- isimler listesindeki her ismi küçük harfe çevirip tersten yazdır
'''
sonuc = [i.lower()[::-1] for i in isimler]
'''
# 3- verilen string içindeki rakamları içeren bir liste
'''
sonuc = [i for i in string if i.isdigit()]
'''
# 4- yıllar dizisindeki her doğum yılı için yaş bilgisi içeren liste oluştur
'''
import datetime

simdi =datetime.datetime.now().year

sonuc = [simdi - yil for yil in yillar]
'''
# 5- dereceler listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma tehlikesi yaz
'''
sonuc = [i if i>0 else "buzlanma tehlikesi" for i in derece]


print(sonuc)
'''








