#Basit Hesap Makinesi
#Toplama, çıkarma, çarpma, bölme işlemlerini yapabilen konsol uygulaması.

while True:
    sayi1 = float(input("BİRİNCİ SAYIYI GİRİNİZ: "))
    sayi2 = float(input("İKİNCİ SAYIYI GİRİNİZ: "))

    islem = input("YAPMAK İSTEDİĞİİNİZ İŞLEMİ SEÇİNİZ (+,-,*,/,**) ÇIKMAK İÇİN ** KOYUNUZ :  ")
    if islem == "**":
        print("HESAP MAKİNESİNDEN ÇIKIŞ YAPIYORSUNUZ...")
        break
    
    if islem == "+":
        sonuc = sayi1 + sayi2
        print("SONUÇ : ", sonuc)
    elif islem == "-":
        sonuc = sayi1 - sayi2
        print("SONUÇ : ", sonuc)
    elif islem == "*":
        sonuc = sayi1 * sayi2
        print("SONUÇ : ", sonuc)
    elif islem == "/":
        if sayi2 != 0:
            sonuc = sayi1 / sayi2
            print("SONUÇ : ",sonuc)
    else:
        print("GEÇERSİZ İŞLEM SEÇİMİ YAPTINIZ ! ")
        