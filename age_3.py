#Kullanıcıdan Doğum Yılı Alıp Yaş Hesaplama
#Kullanıcının doğum yılını iste, güncel yıla göre yaşını hesapla.

while True:
    suan_ki_yil = 2025
    
    dogum_yili = int(input("DOĞUM YILINIZI GİRİNİZ: "))
    yas = suan_ki_yil - dogum_yili
    if yas < 0:
        print("DOĞUM YILINIZ GEÇERSİZ ! ")
    devam = input("Başka bir yaş hesaplamak ister misiniz? (e/h): ")
    if devam.lower() != "e":
        print("Görüşmek üzere!")
        break
    else:
        print("YAŞINIZ: ", yas)
        
    
