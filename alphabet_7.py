#Kullanıcıdan bir cümle al. Bu cümlede hangi harften kaç tane geçtiğini bul ve ekrana yazdır.
cümle = input("Bir cümle girin: ")

harf_sayilari = {}

for harf in cümle:
    if harf != " ":
        if harf in harf_sayilari:
            harf_sayilari[harf] += 1
        else:
            harf_sayilari[harf] = 1

for harf, sayi in harf_sayilari.items():
    print(f"'{harf}' harfi {sayi} kez geçiyor.")
