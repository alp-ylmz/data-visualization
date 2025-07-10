# 2 ADET LİSTE OLACAK KULLANICI HANGİSİNİ SEÇERSE SIRALANMIŞ BİR ŞEKİLDE LİSTE GELECEK
#3 YAZINCA PROGRAMDAN ÇIKACAK 
"""
birinci_liste = [1,3,7,15,25,10,88,65,22]
ikinci_liste = ["A","L","P","E","R"]

def liste1():
    print(sorted(birinci_liste))
    print("1. LİSTE SIRALANDI !!! ")
    
def liste2():
    print(sorted(ikinci_liste))
    print("2. LİSTE SIRALANDI")
    
while True:
    print("İLK LİSTENİZ :",birinci_liste)
    print("İKİNCİ LİSTENİZ: ",ikinci_liste)
    secim=int(input("LÜTFEN SIRALANMASINI İSTEDİĞİNİZ LİSTEYİ SEÇİNİZ (ÇIKMAK İÇİN 3 GİRİNİZ !!! )"))
    if secim == 1:
        liste1()
    elif secim == 2:
        liste2()
    elif secim ==3:
        break
    else:
        print("HATALI TUŞLAMA YAPTINIZ !!! ")
"""

#YAŞ HESAPLAMA FOKSİYONU YAZALIM 
"""
def yas_hesapla(dogum_yili):
    yas= 2025 - dogum_yili
    print(f"YAŞINIZ: {yas}")
    
yas_hesapla(1991)
"""
#Toplama yapan ve sonucu döndüren fonksiyon
"""
def topla(sayi1,sayi2):
    return sayi1 + sayi2
sonuc = topla(5,5)
print("TOPLAM: ",sonuc)
"""
#Bir ürünün fiyatını ve indirim oranını alacağız.
#Fonksiyon, indirimli fiyatı hesaplayıp döndürecek.
#Sonucu dışarıda yazdıracağız.
"""
def indirim_hesapla(fiyat,indirim_orani):
    indirim_miktari = fiyat -(fiyat * (indirim_orani / 100))
    return indirim_miktari 
fiyat = 1000
indirim_orani = 20
sonuc = indirim_hesapla(fiyat,indirim_orani)   
print(f"İNDİRİMLİ FİYAT: {sonuc} TL")
"""

#Yaşı girilen bir kişinin bilet fiyatını hesaplayan bir fonksiyon yaz.
#Kurallar şöyle:
#0-6 yaş: Ücretsiz
#7-17 yaş: %50 indirim
#18-64 yaş: Tam fiyat
#65+ yaş: %30 indirim
"""
def bilet_fiyati_hesapla(yas):
    tam_fiyat = 100

    if yas < 0:
        return "GEÇERSİZ YAŞ GİRİŞİ YAPTINIZ !!!"
    elif yas <= 6:
        return 0
    elif 7 <= yas <= 17:
        return tam_fiyat * 0.5
    elif 18 <= yas <= 64:
        return tam_fiyat
    elif yas >= 65:
        return tam_fiyat * 0.7
"""
# Kaç kişi için işlem yapılacak
"""
kisi_sayisi = int(input("Kaç kişinin biletini hesaplamak istiyorsunuz? "))

for i in range(1, kisi_sayisi + 1):
    yas = int(input(f"{i}. kişinin yaşını girin: "))
    sonuc = bilet_fiyati_hesapla(yas)

    if isinstance(sonuc, str):
        print(f"{i}. KİŞİ → {sonuc}")
    else:
        print(f"{i}. KİŞİ → BİLET FİYATI: {sonuc} TL")
""" 

#Bir öğrencinin notlarını alıp ortalama hesaplayan ve sonucu döndüren bir fonksiyon yaz.
""" 
def not_ortalamasi(sinav1, sinav2, sinav3):
    ortalama = (sinav1 + sinav2 + sinav3) / 3
    if ortalama >= 50:
        return f"Ortalama: {ortalama} - GEÇTİ ! "
    else:
        return f"Ortalama: {ortalama} - KALDI ! "
sonuc = not_ortalamasi(70,80,90)
print(sonuc)
""" 
#Bir öğrencini notlarını kendi girecek ortalama hesaplayıp ve sonucu döndüren bir fonksiyon yaz.
"""
def not_hesapla(s1,s2,s3):
    ortalama = (s1 + s2 + s3) / 3
    if ortalama >= 50:
        return f"Ortalama: {ortalama} - GEÇTİ ! "
    else:
        return f"ORtalama: {ortalama} - KALDI ! "
    
sinav1 = float(input("1. SINAV NOTUNUZU GİRİNİZ: "))
sinav2 = float(input("2. SINAV NOTUNUZU GİRİNİZ: "))
sinav3 = float(input("3. SINAV NOTUNUZU GİRİNİZ: "))

sonuc = not_hesapla(sinav1, sinav2, sinav3)
print(sonuc)
"""

#Akaryakıt (Benzinlik) Satış Sistemi
"""
def yakit_fiyati_hesapla(yakit_turu, litre):
    yakit_turu = yakit_turu.lower()
    
    if yakit_turu == "benzin":
        fiyat = 35
    elif yakit_turu == "motorin":
        fiyat = 32
    elif yakit_turu == "lpg":
        fiyat = 17
    else:
        return "Geçersiz yakıt türü!"

    toplam = fiyat * litre
    return f"{yakit_turu.upper()} - {litre} LİTRE için TOPLAM: {toplam} TL"

# --- KULLANICIDAN GİRİŞ AL ---
print("⛽ YAKIT SATIŞ SİSTEMİ")
print("Yakıt türleri: benzin, motorin, lpg")

yakit = input("Yakıt türünü girin: ")
litre = float(input("Kaç litre almak istiyorsunuz? "))

# --- FONKSİYONU ÇAĞIR VE SONUCU YAZDIR ---
sonuc = yakit_fiyati_hesapla(yakit, litre)
print("🧾", sonuc)
"""

"""        
def otopark_ucreti(saat):
    if saat <= 0:
        return "Geçersiz saat girişi!"
    elif saat <= 1:
        return f"{saat} saatlik park ücreti: 20 TL"
    elif saat <= 5:
        ek_ucret = (saat - 1) * 10
        toplam = 20 + ek_ucret
        return f"{saat} saatlik park ücreti: {toplam} TL"
    else:
        ilk_5_saat_ucret = 20 + (4 * 10)  # 20 + 40 = 60 TL
        ek_saat = saat - 5
        toplam = ilk_5_saat_ucret + (ek_saat * 5)
        return f"{saat} saatlik park ücreti: {toplam} TL"

# --- KULLANICIDAN GİRİŞ AL ---
print("🅿️ OTOPARK SİSTEMİNE HOŞ GELDİNİZ")
plaka = input("Araç plakası giriniz: ")

try:
    saat = float(input("Kaç saat park ettiniz?: "))
    sonuc = otopark_ucreti(saat)
    print(f"🚗 PLAKA: {plaka} → {sonuc}")
except ValueError:
    print("Lütfen geçerli bir sayı girin.")
"""
"""
#Kullanıcıdan ürün adı ve fiyatı alıyoruz
#Başka ürün var mı?” diye soruyoruz
#En sonunda toplam tutarı gösteriyoruz

def urun_ekle(urun_adi, fiyat, sepet):
    sepet.append((urun_adi, fiyat))
    return sepet

sepet = []
print("🛒 MARKETE HOŞGELDİNİZ =) ")

while True:
    urun = input("ÜRÜN ADI:  ")
    try:
        fiyat = float(input("FİYATI:  (TL) " ))
        urun_ekle(urun, fiyat, sepet)
    except ValueError:
        print("LÜTFEN GEÇERLİ BİR FİYAT GİRİNİZ !!! ")
        continue
    devam  = input ("BAŞKA ÜRÜN VAR MI? (E/H): ").lower()
    if devam != "e":
        break
    
    print("\n🛍️ SEPETİNİZDEKİ ÜRÜNLER: ")
    toplam = 0
    for urun_adi, fiyat in sepet:
      print(f" - {urun_adi}: {fiyat} TL")
      toplam += fiyat
      
    print(f"\nTOPLAM TUTAR: {toplam} TL")
"""    
    