




isim = input("isminizi giriniz: ")
yas = int(input("yaşınızı giriniz: "))
egitim = input("eğitim düzeyiniz: ")

if (yas >= 18):
    if (egitim == "üniversite") or (egitim == "lise"):
        print("ehliyet almaya uygunsun")
    else:
        print("eğitim düzeyi yetersiz")
else:
    print("alamazsın")