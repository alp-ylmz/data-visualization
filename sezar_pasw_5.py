#5. Basit Metin Şifreleme (Sezar Şifreleme)

def sezar_sifrele(metin, kaydirma):
    sifreli_metin = ""

    for harf in metin:
        # Eğer harf küçük harf a-z aralığında ise
        if 'a' <= harf <= 'z':
            # Karakter kodunu al, kaydır, 26 harf aralığında döndür
            yeni_kod = (ord(harf) - ord('a') + kaydirma) % 26 + ord('a')
            sifreli_metin += chr(yeni_kod)
        # Eğer büyük harf A-Z aralığında ise
        elif 'A' <= harf <= 'Z':
            yeni_kod = (ord(harf) - ord('A') + kaydirma) % 26 + ord('A')
            sifreli_metin += chr(yeni_kod)
        else:
            # Harf değilse (boşluk, noktalama vb.) olduğu gibi ekle
            sifreli_metin += harf

    return sifreli_metin


# Kullanıcıdan veri alma
metin = input("Şifrelenecek metni girin: ")
kaydirma = int(input("Kaç harf kaydırılsın? "))

# Şifreleme işlemi
sonuc = sezar_sifrele(metin, kaydirma)

print("Şifrelenmiş metin:", sonuc)



