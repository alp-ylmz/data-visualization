import random

def sayi_tahmin_oyunu():
    
    rastgele_sayi = random.randint(1, 100)
    tahmin = None
    print("1-100 ARASINDA BİR SAYI TUTTUM. =) TAHMİN ET !")
    while tahmin != rastgele_sayi:
        try:
            tahmin = int(input("TAHMİNİNİ YAP BAKALIM : "))
            if tahmin < rastgele_sayi:
                print("DAHA BÜYÜK BİR SAYI YAZ ! ")
            elif tahmin > rastgele_sayi:
                print("DAHA KÜÇÜK BİR SAYI YAZ ! ")
            else:
                print("TEBRİKLER! DOĞRU TAHMİN ETTİN ! ")
        except ValueError:
            print("LÜTFEN GEÇERLİ BİR SAYI GİR ! ")
sayi_tahmin_oyunu()

    