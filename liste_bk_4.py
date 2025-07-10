#Liste İçinde En Büyük ve En Küçük Sayıyı Bulma


liste = [1, 5, 9, 23, 47, 69, 99, 1024, 5789, 24, 19, 47687]

en_buyuk = liste[0]
en_kucuk = liste[0]

for sayi in liste:
    if sayi > en_buyuk:
        en_buyuk = sayi
    if sayi < en_kucuk:
        en_kucuk = sayi

print("En Küçük Sayı:", en_kucuk)
print("En Büyük Sayı:", en_buyuk)
