#DEĞİŞKENLER İLE İLGİLİ ALIŞTIRMALAR
# Ad, soyad ve yaş bilgilerini saklayan değişkenler oluşturalım
"""
Ad="ALPER"
Soyad= "YILMAZ"
Yas=35

print("Ad: ", Ad)
print("Soyad: ", Soyad)
print("Yaş: ", Yas)
"""
# İki sayı tanımlayalım ve dört işlem yapalım
"""
Sayi1 = 150
Sayi2 = 15

Toplam = Sayi1 + Sayi2
Çıkarma = Sayi1 - Sayi2
Çarpma = Sayi1 * Sayi2
Bölme = Sayi1 / Sayi2

print("Toplam: ", Toplam)
print("Çıkarma: ", Çıkarma)
print("Çarpma: ", Çarpma)
print("Bölme: ", Bölme)
"""
# Kullanıcıdan giriş alıp sayıya çevirelim (input her zaman string döndürür)
"""
Dogum_yili = input ("Doğum Tarihinizi Giriniz: ")
Yas = 2025 - int (Dogum_yili)
print("Yaşınız: ", Yas)
"""

# Bir alışveriş listesi oluşturalım
"""Alisveris_Listesi = ["Yumurta","Süt","Ekmek","Peynir","Zeytin"]"""
# Listeyi yazdıralım
"""print("Alışveriş Listeniz: ",Alisveris_Listesi)"""
# Listeye yeni ürün ekleyelim
"""Alisveris_Listesi.append("Domates")
print("Güncellenmiş Alışveriş Listeniz: ", Alisveris_Listesi)"""
# Kişi bilgilerini sözlükte saklayalım SÖZLÜK KULLANIMI
"""Kisi_Bilgileri ={
    "Ad" : "ALPER",
    "Soyad" : "YILMAZ",
    "Yas" : 35,
    "Meslek" : "Yazılım Geliştirici"   
}
print("Kişi Bilgileri: ", Kisi_Bilgileri)"""


"""
isim = input("ADINIZI GİRİNİZ: ")
yas = input("YAŞINIZI GİRİNİZ: ")
meslek = input("MESLEPĞİNİZİ GİRİNİZ: ")

print(f"Adınız: {isim}, Yaşınız:{yas},Mesleğiniz: {meslek}")
# Kullanıcıdan alınan bilgileri sözlükte saklayalım
Kisi_Bilgileri = {
    "Ad": isim,
    "Yaş": yas,
    "meslek": meslek   
}
print("Kişi Bilgileri: ", Kisi_Bilgileri)"""

#Bir öğrencinin adı, notu ve geçip geçmediği bilgilerini değişkenlerle tanımla ve ekrana yazdır.

"""ogrenci_adi = "Ahmet"
ogrenci_notu = 85
gecti_mi = ogrenci_notu >= 50

print(f"Öğrenci Adı : {ogrenci_adi}")
print(f"Öğreci Notu : {ogrenci_notu}")
print("Geçti mi?", gecti_mi)"""

# Bir ürünün adı, fiyatı ve stok durumu bilgilerini değişkenlerle tanımla ve ekrana yazdır.
"""urun_adi = "PlayStation 5"
urun_fiyati = 4999.99
stok_durumu = True
print("Ürün Adı: ",urun_adi)
print("Ürün Fiyatı: ",urun_fiyati)
print("Stok Durumu:",stok_durumu)
print(f"Ürün Adı: {urun_adi}, Fiyatı: {urun_fiyati}, Stok Durumu: {stok_durumu}")"""
# Bir kitabın adı, yazarı ve sayfa sayısı bilgilerini değişkenlerle tanımla ve ekrana yazdır.
kitap_adi = "SEFİLLER"
yazar = "Victor Hugo"
sayfa_sayisi = 1234
print("Kitap Adı:",kitap_adi)
print("Yazar:",yazar)
print("Sayfa Sayısı : ",sayfa_sayisi)
