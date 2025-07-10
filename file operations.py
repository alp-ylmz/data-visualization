r"""
dosya_yolu = r"D:\ALP-SOFT-DEV\keep\test_dosyasi.txt"
"""
"""
with open (dosya_yolu,'w') as dosya:
    dosya.write("İLK YAZI BAŞARI İLE YAZILDI.\n")
"""
"""    
with open(dosya_yolu, 'a') as dosya:
    dosya.write("BU YAZI .a MODU İLE EKLENDİ. \n")
"""    
"""    
try:
    with open (dosya_yolu, "x")as dosya:
        dosya.write("BU YAZI .x MODU İLE EKLENDİ. \n")
except FileExistsError:
    print("DOSYA ZATEN VAR. .x MODU KULLANILAMADI. !!!")
"""    
"""
with open(dosya_yolu,'r')as dosya:
    icerik = dosya.read()
    print("DOSYA İÇERİĞİ\n",{icerik})
"""
"""
with open(dosya_yolu,'r+') as dosya:
    ıcerik = dosya.read()
    print("DOSYA ÖNCEKİ İÇERİĞİ:\
        n", ıcerik)
    dosya.seek(0)#DOSYA BAŞIBA DÖNÜYOR
    dosya.write("DOSYA İÇERİĞİ GÜNCELLENDİ r+ İLE")
"""
r"""
dosya_yolu = r"D:\ALP-SOFT-DEV\keep\test_dosyasi.txt"

with open(dosya_yolu,'w') as dosya:
    print("MARKET FİŞİ OLUŞTURULUYOR...")
    print("ÜRÜN GİRİŞİ YAP BİTİNCE 'B' TUŞUNA BAS")
    while True:
        urun = input("ÜRÜN ADI:  ")
        if urun.lower() == 'b':
            break
        fiyat = float(input("FİYATI:  (TL) "))
        satir = f"{urun} - {fiyat} TL"
        dosya.write(satir)
print("FİŞ BAŞARI İLE {dosya_yolu} KONUMUNA YAZILDI...")
"""
r"""
dosya_yolu = r"D:\ALP-SOFT-DEV\keep\test_dosyasi.txt"
toplam =0
with open(dosya_yolu,'a') as dosya:
    print("ÜRÜN EKLEME MODUNA HOŞGELDİN BİTİNCE 'B' TUŞUNA BAS")
    while True:
        urun = input ("ÜRÜN ADI: ")
        if urun.lower() == 'b':
            break
        fiyat = float(input("FİYATI: (TL)"))
        toplam += fiyat
        dosya.write(f"{urun} - {fiyat} TL\n")
    dosya.write(f"TOPLAM TUTAR: {toplam} TL\n")
print(f"FİŞ BAŞARI İLE {dosya_yolu} KONUMUNA EKLENDİ... \n")
"""

#read() – Dosyanın Tamamını Okumak
r"""
dosya_yolu = r"D:\ALP-SOFT-DEV\keep\fis.txt"

try:
    with open(dosya_yolu, 'r+') as dosya:
        print(dosya.read())
        dosya.write("EKMEK - 7 TL \n ")
        dosya.write("ZEYTİN - 25 TL \n ")
        dosya.write("YUMURTA - 30 TL \n ")
        
    print(f"DOSYA BAŞARIYLA OLUŞTURULDU VE YAZILDI: ")
except FileExistsError:
    print("DOSYA ZATEN VAR .X MODU KULLANILAMADI. !!! ")
"""   
r"""  
dosya_yolu = r"D:\ALP-SOFT-DEV\keep\yeni_fis.txt"

with open(dosya_yolu,'w')as dosya:
    dosya.write("BU İŞİ... \n")
    dosya.write("BAŞARACAĞINA .... \n")
    dosya.write("EMİNİM ... \n")
print(f"YENİ FİŞ DOSYASI OLUŞTURULDU: {dosya_yolu}")



with open(dosya_yolu,'r') as dosya:
    satirlar = dosya.readlines()
print("\n FİŞ SATIRLARI \n ")
for satir in satirlar:
    print(satir.strip())  # strip() ile satır sonu karakterlerini kaldırıyoruz
"""    
r""" 
dosya_yolu = r"D:\ALP-SOFT-DEV\keep\yeni_fis.txt"

with open (dosya_yolu,'r') as dosya:
    print("BAŞLANGIÇ KONUMU: ",dosya.tell())
    
    icerik = dosya.read(10)
    print("OKUNAN İÇERİK: ", icerik)
    
    print("OKUNAN SONRASI KONUM: ", dosya.tell())
    
    dosya.seek(0)#imle.yi başa alıyoruz
    print("SEEK SONRASI KONUM: ",dosya.tell())
    
    icerik2 = dosya.read(5)
    print("YENİ OKUNAN İÇERİK: ", icerik2)
""" 
r""" 
dosya_yolu = r"D:\ALP-SOFT-DEV\keep\yeni_fis.txt"
with open(dosya_yolu,'w') as dosya:
    dosya.write("MUZ - 10 TL DEN SATIŞA SUNULUYOR\n")
    dosya.write("ELMA - 15 TL DEN SATIŞA SUNULUYOR\n")
    dosya.write("ARMUT - 20 TL DEN SATIŞA SUNULUYOR\n")
    
with open(dosya_yolu,'r+') as dosya:
    print("Başlangıç konumu:", dosya.tell())  # 0
    
    icerik = dosya.read(10)  # İlk 10 karakteri oku
    print("Okunan içerik:", icerik)
    
    print("Okuma sonrası konum:", dosya.tell())  # 10
    
    dosya.seek(0)  # İmleci başa al
    print("Seek sonrası konum:", dosya.tell())  # 0
    
    icerik2 = dosya.read(5)
    print("Yeni okunan içerik:", icerik2)
""" 

dosya_yolu = r"D:\ALP-SOFT-DEV\keep\yeni_fis.txt"
fiyatlar = []
urunler = []

with open(dosya_yolu,'w') as dosya:
    print("ÜRÜN GİRİŞİ YENİ ÇIKMAK İÇİN 'B' TUŞUNA BAS")
    while True:
        urun = input("ÜRÜN ADI: ")
        if urun.lower() == 'b':
            break
        try:
            fiyat = float(input("FİYATI : (TL)"))
            print("ÇIKMAK İÇİN 'B' TUŞUNA BASABİLİRSİNİZ !!! ")
        except ValueError:
            print("LÜTFEN GEÇERLİ BİR FİYAT GİRİNİZ !!! ")
            continue
        dosya.write(f"{urun} - {fiyat} TL \n")
        urunler.append(urun)
        fiyatlar.append(fiyat)
        toplam = sum(fiyatlar)
print(f"TOPLAM TURAR: {toplam} TL' DİR")
for u in urunler:
    print(f"ALDIN ÜRÜN LİSTESİ BUNLAR {u}")
print(f"FİŞ DOSYASI BAŞARIYLA OLUŞTURULDU: {dosya_yolu}")
      
      
