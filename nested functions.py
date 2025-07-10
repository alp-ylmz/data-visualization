"""
def selamla():
    def isim_söyle():
        print("ALPER")
    print("Merhaba!")
selamla()
"""
"""
def hesaplama(a, b):
    def topla():
        return a + b
    
    def carp():
        return a*b
    
    print ("TOPLAM", topla())
    print ("ÇARPIM", carp())
hesaplama(6,6)
"""
"""
def hesaplama (a,b):
    def cikar():
        return a - b
    def böl():
        return a/b
    
    print("ÇIKARMA", cikar())
    print("BÖLME", böl()),
hesaplama(10,5) 
"""
"""
def fatura_hesapla(tutar):
    def kdv_ekle():
        return tutar * 1.20
    
    def indirim_uygula(kdvli_tutar):
        return kdvli_tutar * 0.90
    
    kdvli_fiyat = kdv_ekle()
    indirimli_fiyat = indirim_uygula(kdvli_fiyat)
    
    print("FATURA TUTARI",tutar)
    print("KDV'li Fiyat", kdvli_fiyat)
    print("İndirimli Fiyat", indirimli_fiyat)
fatura_hesapla(100)
"""    
"""  
def siparis_hesapla(fiyat):
    def ekstra_ekle():
        return fiyat + 15
    
    def indirim_uygula(ekstra_fiyat):
        return ekstra_fiyat * 0.95
    
    ekstra_fiyat = ekstra_ekle()
    indirimli_fiyat = indirim_uygula(ekstra_fiyat)
    print("SİPARİŞ TUTARI", fiyat)
    print("Ekstra Ücretli Fiyat", ekstra_fiyat) 
    print("İndirimli Fiyat", indirimli_fiyat)
siparis_hesapla(100)
"""    
"""   
def sekil_kare(func):
    def yaz():
        return "##############\n" + func() + "\n###############"
    return yaz 
    
def sekil_yildiz(func):
    def yaz():
        return "**********\n" + func() + "\n**********"
    return yaz

@sekil_kare
@sekil_yildiz
def test():
    return"ALPER"
print(test())
"""   

""" 
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n -2)
terim = 10

if terim < 0:
    print("LÜTFEN POZİTİF DEĞER GİRİN")
else:
    print("FİBONACCI SERİSİ: ")
    for i in range(terim):
        print(fibonacci(i), end="")
""" 
""" 
def say(n):
    if n == 0:
        return
    say(n-1)
    print(n)
say(10)
""" 


#LAMBDA KULLANIMI
"""
kare = lambda x: x * x
print(kare(5))
"""
"""
topla = lambda a, b: a + b
print(topla(5,10))
"""
"""
uzun_mu = lambda kelime: len(kelime) > 5
print(uzun_mu("ALPER"))
print(uzun_mu("ALPER YILMAZ"))
"""
"""
isimler = ["ALİ","AYŞE","MEHMET","ZEYNEP","ALPER",]
isimler_sirali = sorted(isimler, key=lambda x: len(x))
print(isimler_sirali)
"""
"""
sayi = lambda tek_mi: "TEK" if tek_mi % 2 != 0 else "ÇİFT"
print(sayi(5))
"""
"""
#DÜZ FONKSİYON KULLANIMI
def indirim(fiyat):
    return fiyat * 0.8
#LAMVBDA KULLANIMI
indirimli_fiyat = lambda fiyat: fiyat * 0.8
print(indirim(100))
print(indirimli_fiyat(100))
"""
"""
#ARKADAŞ GRUBUNUN YAŞLARINI 1 YIL ARTIRMAK İSTİYORSUN 
# MAP KULLANIMI
yaslar = [15, 25, 20,]
yeni_yaslar = list(map(lambda x: x + 1, yaslar))
print(yeni_yaslar)
"""
"""
#Partiye sadece 18 yaşından büyükleri davet etmek istiyorsun
# FİLTER KULLANIMI
yaslar = [15,18,20,16,19]
buyukler = list(filter(lambda x: x >= 18 , yaslar))
print(buyukler)
"""
"""
#Bir sınıftaki öğrencilerin isimlerini, kısa olandan uzun olana sıralamak istiyorsun
isimler = ["ALİ","AYŞE","MEHMET","ZEYNEP","ALPER"]
siralanmis = sorted(isimler, key=lambda x: len(x))
print(siralanmis)
"""
"""
#Diyelim ki bir oyun oynuyorsun ve karakterlerin güç puanlarını artırmak istiyorsun (herkese +10 puan):

puanlar = [50,85,70,55]
yeni_puanlar = list(map(lambda x: x + 10, puanlar))
print(yeni_puanlar)
"""
"""
#Market sepetinde bir sürü ürün var, ama sadece indirimdeki ürünleri (örneğin, fiyatı 20 TL'den düşük olanları) almak istiyorsun.
sepet = [("SÜT",15),("EKMEK",18),("YUMURTA",45),("ÇAY",55)]
indirimdekiler = list(filter(lambda x : x[1] < 20 , sepet))
print("İNDİRİMDEKİLER",indirimdekiler)
"""
"""

#Bir sınıfta öğrencilerin sınav notları var. Sadece 60 ve üstü not alanları seçelim (geçenleri bulalım).
notlar = [45,67,25,80,37,29,90,55,18,100]
gecenler = list(filter(lambda x : x >= 60 ,notlar))
print(gecenler)
"""
"""
#Market sepetindeki ürünleri ucuzdan pahalıya sıralayalım.

sepet = [("SÜT",115),("EKMEK",12),("YUMURTA",65),("ÇAY",222)]
sirali_fis = sorted(sepet, key=lambda x : x[1])
print("SIRALI FİŞ",sirali_fis)
"""
"""
#Sınıftaki öğrencileri sınav notlarına göre yüksekten düşüğe sıralayalım.
ogrenci_notlari = [("ALİ",85),("AYŞE",90),("MEHMET",75),("ZEYNEP",95)]
not_siralama = sorted(ogrenci_notlari, key=lambda x: x[1], reverse=True)
print("ÖĞRENCİ NOT SIRALAMASI", not_siralama)
"""
"""
#OYUN KARAEKTERLERİNİ İSİM UZUNLUĞUNA GÖRE SIRALAYALIM
karekterler = [("SAVAŞÇI",100), ("BÜYÜCÜ",80),("OKÇU",90),("SUİKASTÇİ",70)]
düzenli_karakterler = sorted(karekterler, key=lambda x: len(x[0]))
print("KARAKTER SIRALAMASI", düzenli_karakterler)
"""

