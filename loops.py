"""
sayi = 1

while sayi <= 10:
    print(sayi)
    sayi += 1
"""
"""
kullanici_girdisi = ""

while kullanici_girdisi !="ÇIK":
    kullanici_girdisi = input("BİR ŞEYLER YAZABİLİRSİNİZ ÇIKMAK İÇİN 'ÇIK' YAZINIZ: ")
    print(f"GİRDİĞİNİZ DEĞER:",kullanici_girdisi)
"""
"""
sifre = ""

while sifre != "1234":
    sifre = input("ŞİFRENİZİ GİRİNİZ")
    
print("ŞİFRENİZ DOĞRULANDI")
"""          
#Bir sayı sor ve sayı 10’dan küçükse tekrar sorsun. 10 ve üzeri bir sayı girilince "teşekkürler" yazsın.
"""tahmin = 0

while tahmin < 10:
    tahmin = int(input ("LÜTFEN SAYI GİRİNZ : "))
print("TEŞEKKÜRLER") 
"""
"""
sifreli_sayi = 7
tahmin = 0

while tahmin != sifreli_sayi:
    tahmin = int(input("LÜTFEN 1-10 ARASINDA BİR SAYI GİRİNİZ:"))
    
    if tahmin < sifreli_sayi:
        print("DAHA BÜYÜK BİR SAYINI GİRİNİZ")
    elif tahmin > sifreli_sayi:
        print("DAHA KÜÇÜK BİR SAYI GİRİNİZ")
  
print("TEBRİKLER BİLDİN")
"""
"""
menu =
TOPLAMA İŞLEMİ İÇİN 1
ÇIKARMA İŞLEMİ İÇİN 2
ÇARPMA İŞLEMİ İÇİN 3
BÖLME İŞLEMİ İÇİN 4
ÇIKIŞ İÇİN 5
LÜTFEN SEÇİMİNİZİ YAPINIZ: 
"""
"""
dongu= 1

while dongu == 1:
    print(menu)
    
    sayi1 = int(input("LÜTFEN 1. SAYINIZI GİRİNİZ: "))
    sayi2 = int(input("LÜTFEN 2. SAYINIZI GİRİNİZ:"))
    secim = int(input("LÜTFEN MENÜDEN İŞLEM SEÇİNİZ:"))
    if secim ==1:
        print("TOPLMA İŞLEM SONUCU: ",sayi1 + sayi2)
    elif secim == 2:
        print("ÇIKARMA İŞLEM SONUCU: ", sayi1 - sayi2)
    elif secim ==3:
        print("ÇARPMA İŞLEM SONUCU:  ",sayi1 * sayi2)
    elif secim==4:
        print("BÖLME İŞLEM SONUCU: ", sayi1 / sayi2)
    elif secim ==5:
        print("ÇIKIŞ YAPILDI...")
        dongu = 0
    else:
        print("HATALI SEÇİM YAPTINIZ LÜTFEN MENÜDEN SEÇİM YAPINIZ")
    """
"""
dovız =1
"""
"""menu = 
------ DÖVİZ ÇEVİRİCİ--------
1. DOLAR'A ÇEVİR (1 USD DOLARI = 39.18 TL)
2.EURO'YA ÇEVİR (1 EURO = 44.97 TL)
3.STERLİN'E ÇEVİR (1 STERLİN = 53.00 TL)
4. ÇIKIŞ (ÇIKMAK İÇİN '4' YAZINIZ)
LÜTFEN SEÇİMİNİZİ YAPINIZ:
"""
"""
while dovız ==1:
    print(menu)
    
    tl = float(input("LÜTFEN TL MİKTARINI GİRİNİZ:"))
    secim = int(input("LÜTFEN MENÜDEN İŞLEM SEÇİNİZ: "))
    if secim ==1:
        print("DOLARA ÇEVİRİLİYOR:" ,tl / 39.18,"DOLAR")
    elif secim ==2:
        print("EURO'YA ÇEVİRİLİYOR:", tl / 44.97, "EURO")
    elif secim==3:
        print("STERLİNE ÇEVRİLİYOR:", tl / 53,00, "STERLİN")
    elif secim ==4:
        print ("ÇIKIŞ YAPILIYOR...")
        print("ÇIKIŞ YAPILDI TEŞEKKÜR EDERİZ")
        dovız = 0
    else:
        print("HATALI SEÇİM")
"""            
#Bilgisayar 1 ile 10 arasında bir sayı tutuyor. Kullanıcı doğru tahmin edene kadar soruyoruz.
"""
import random

sayi = random.randint(1, 10)
tahmin = 0

while tahmin != sayi:
    tahmin = int(input("1 ile 10 arasında bir sayı giriniz: "))
    
    if tahmin < sayi:
        print("daha büyük bir sayı giriniz.")
    elif tahmin > sayi:
        print("daha küçük bir sayı giriniz.")
    else:
        print("tebrikler doğru tahmin ettiniz!")
        print("PROGRAM SONLANDI...")
""" 
 #Kullanıcı "çık" yazana kadar ona sorular soran basit bir sohbet döngüsü.       
"""
mesaj = ""
print("merhaba sohbet etmek istermisiniz ? (çıkmak  için ise çık yazmanız yeterli =))")

while mesaj != "çık":
    mesaj = input ("bir şeyler yazabilirsin:  ")
    
    if mesaj != "çık":
        print ("Bende diyorum ki: ",mesaj.upper())
    else:
        print ("görüşmek üzere...")  
""" 
#Sayı Tahmininde Deneme Sayısını Sınırlayan Oyun
""" 
import random
sayi = random.randint(1,10)

tahmin = 0
hak = 5

print("1 ile 10 arasında bir sayı tuttum. Tahmin etmeye çalış")

while tahmin != sayi and hak > 0:
    tahmin = int (input ("TAHMİNİNİZİ GİRİNİNİZ:   "))
    hak -= 1
    if tahmin < sayi:
        print("DAHA BÜYÜK BİR SAYI GİR ! ")
    elif tahmin > sayi:
        print("DAHA KÜÇÜK BİR SAYI GİR ! ")
    if tahmin != sayi and hak > 0:
        print(f"kalan hakkınız:{hak}")
    
if tahmin == sayi:
    print("TEBRİKLER DOĞRU TAHMİN ETTİNİZ !")
else:
    print("haklarınız bitti. Sayı:", sayi)
"""        

#BASİT ATM DÖNGÜSÜ 
# Kullanıcı para yatırabilir, çekebilir veya bakiyesini görebilir. Çıkmak için 4'e basar.
"""
bakiye = 1000
secim = 0

print("ATM DEN YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ")

while secim != 4:
    print("1. para yatırma ")
    print("2. para çekme")
    print("3. bakiye sorgulama")
    print("4. atm den çıkış")
    secim = int(input("LÜTFEN İŞLEMİNİZİ SEÇİNİZ:"))
    if secim ==1:
        miktar = float(input("YATIRMAK İSTEDĞİNİZ MİKTARI GİRİNİZ: "))
        print("----------------")
        bakiye += miktar
        print(f"{miktar} TL YATIRDINIZ... GÜNCEL BAKİYENİZ: {bakiye} TL")
        print("/////////////////")
    elif secim ==2:
        miktar = float(input("ÇEKMEK İSTEDİĞİNİZ MİKTARI GİRİNİZ:  "))
        bakiye -= miktar
        print(f"{miktar} TL ÇEKTİNİZ... GÜNCEL BAKİYENİZ: {bakiye} TL")
        print("/////////////////")
    elif secim ==3:
        print(f"GÜNCEL BAKİYENİZ: {bakiye} TL")
        print("/////////////////")
    elif secim ==4:
        print("ATM DEN ÇIKIŞ YAPILIYOR...")
        print("TEŞEKKÜR EDERİZ")
    else:
        print("HATALI TUŞA BASTINIZ LÜTFEN MENÜDEN SEÇİM YAPINIZ !!! ")
"""        
        
 #Kullanıcı doğru şifreyi girene kadar tekrar tekrar sor. Doğru girince giriş başarılı desin ve 3 hakkı olacak .       
""" 
parola = "9999"
parola_hakki = 3

while parola_hakki > 0:
    girilen_parola = int(input("lütfen parolanızı giriniz: "))
    
    if girilen_parola == int(parola):
        print("GİRİŞ BAŞARILI ...")
        break
    else:
        parola_hakki -= 1
        print(f"HATALI PAROLA GİRDİNİZ KALAN HAKKINIZ: {parola_hakki}")
if parola_hakki == 0:
    print("PAROLA HAKKINIZ KALMADI LÜTFEN 10 DK SONRA TEKRAR DENEYİNİZ !!! ")
 """ 

# benzinlik sistemi yapalım. Kullanıcı yakıt türünü seçsin, litre miktarını girsin ve toplam tutarı göstersin. Çıkmak için 4'e basar.
""" 
benzin_fiyati = 30.00
dizel_fiyati = 32.00
lpg_fiyati = 28.00
devam ="e"

while devam.lower() == "e":
    print ("1 - BENZİN")
    print ("2 - DİZEL")
    print ("3 - LPG") 
    print ("4 - ÇIKIŞ")
    secim = int (input("LÜTFEN YAKIT TÜRÜNÜ SEÇİNİZ: "))
    
    if secim ==  1:
        litre = float(input("KAÇ LİTRE BENZİN ALMAK İSTİYORSUN:  "))
        toplam_tutar = litre * benzin_fiyati
        print(f"TOPLAM TUTAR: {toplam_tutar} TL")
    elif secim == 2:
        litre = float (input("KAÇ LİTRE DİZEL ALMAK İSTİYORSUN:  "))
        toplam_tutar = litre * dizel_fiyati
        print(f"TOPLAM TUTAR: {toplam_tutar} TL")
    elif secim == 3:
        litre = float(input("KAÇ LİTRE LPG ALMAK İSTİYORSUN:  "))
        toplam_tutar = litre * lpg_fiyati
        print(f"TOPLAM TUTAR: {toplam_tutar} TL")
    elif secim == 4:
        print("ÇIKIŞ YAPILIYOR...")
        devam = "h"
    else:
        print("HATALI SEÇİM YAPTINIZ LÜTFEN MENÜDEN SEÇİM YAPINIZ !!! ")
        
    devam = input("YENİDEN YAKIT ALMAK İSTER MİSİN? (E/H): ")
    if devam.lower() != "e":
        print("TEŞEKKÜR EDERİZ")
        break
 """         
 
 #FOR DÖNGÜSÜ BAŞLANGIÇ 
 # 5 KEZ MERHABA PATRON YAZDIRALIM
 
"""  
for i in range(5):
    print("MERHABA PATRON")
"""      

#1 DEN 20 YE KADAR OLAN ÇİFT SAYILARI YAZDIRALIM
""" 
for i in range (1,21):
    if i % 2 ==0:
        print(f"{i}")
"""         
#Kullanıcının girdiği 5 sayıyı toplayan program
"""
toplam = 0
for i in range(5):
    sayi = int (input(f"{i+1}, sayıyı giriniz: "))
    toplam += sayi
print(f"GİRDİĞİNİZ SAYILARIN TOPLAMI: {toplam}")
"""
"""
isim = input("LÜTFEN İSMİNİZİ GİRİNİZ:  ")
for harf in isim:
    print({harf})
"""
"""
for i in range(1,11):
    print(f"{i} SAYININ KARESİ",{i**2})
"""
"""
toplam = 0
for i in range(4):
    sayi = int(input(f"{i+1}. SAYINIZI GİRİN: " ))
    toplam += sayi
ortalama = toplam /4
print("SAYILARININ ORTALAMASI: ",ortalama)   
"""
"""
isim = input("İSMİNİZİ GİRİNİZ: ")

ters_isim =""

for harf in isim:
    ters_isim = harf + ters_isim
print("TERS YAZILIŞI: " ,ters_isim)
"""
#FİYAT LİSTESİ VE TOPLAM TUTAR HESAPLAMA 
"""
toplam_tutar = 0

urun_sayisi = int(input("KAÇ ÜRÜN ALDINIZ: "))      

for i in range(urun_sayisi):
    fiyat = float(input(f"{i+1}.ÜRÜNÜN FİYATINI GİRİNİZ: "))
    toplam_tutar += fiyat
print(f"TOPLAM ÖDEMENİZ GEREKEN TUTAR: {toplam_tutar} TL")
"""

#ÜRÜN İSİMLİ FİŞ YAZDIRMA PROGRAMI
"""
toplam_tutar = 0
urunler = []

urun_sayisi = int(input("Kaç ürün aldınız? "))

for i in range(urun_sayisi):
    isim = input(f"{i+1}. ürünün adını girin: ")
    fiyat = float(input(f"{isim} ürününün fiyatı: "))
    
    urunler.append((isim, fiyat))  # ürünleri listeye kaydet
    toplam_tutar += fiyat          # toplamı güncelle

print("\n----- ALIŞVERİŞ FİŞİ -----")
for isim, fiyat in urunler:
    print(f"{isim}: {fiyat} TL")

print("----------------------------")
print(f"TOPLAM: {toplam_tutar} TL")
"""
#Mağaza kasasındaki görevli 9999 şifreli kasayı açmaya çalışıyor. Doğru girerse açılır, yoksa 3 hakkı var.
"""
dogru_sifre = "9999"
hak = 3

for i in range(hak):
    sifre = input("Kasayı açmak için şifreyi girin: ")
    if sifre == dogru_sifre:
        print("✅ Kasa açıldı!")
        break
    else:
        print(f"❌ Yanlış şifre! Kalan hakkınız: {hak - i - 1}")
else:
    print("🚫 Kasa kilitlendi. Yönetici çağrılıyor...")
"""
"""
gunler = ["PAZARTESİ","SALI","ÇARŞAMBA","PERŞEMBE","CUMA","CUMARTESİ","PAZAR"]

for gun in gunler:
    if gun == "PAZAR":
        print(f"{gun}:DİNLENME GÜNÜ (ATLANIYOR...)")
        continue
    print(f"{gun}: GÖREV YAPILDI.")
"""    
#İÇ İÇE DÖNGÜ SINIF VE ÖĞRENCİ LİSTESİ
""" 
for sinif in range (1,3):
    print(f"\n {sinif}. SINIF")
    for ogrenci in range(1,4):
        print(f"- {ogrenci}. ÖĞRENCİ")
""" 
#SAAT VE DAKİKA GÖSTERİMİ
"""
for saat in range(1,2):
    for dakika in range (0,75,15):
        print(f"{saat}. SAAT - {dakika}. DAKİKA")        
"""
#ÇARPIM TABLOSU
"""
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i * j}")
    print("-" * 50 )
"""
#  Sinema salonunda 3 sıra var ve her sırada 5 koltuk bulunuyor. Her koltuğu numaralandıralım:
"""
for sira in range(1,4):
    for koltuk in range(1,6):
        print(f"SIRA {sira} - KOLTUK {koltuk}")
    print("-" *20)
"""
