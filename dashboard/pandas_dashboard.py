# Gerekli kütüphaneleri içe aktar
import pandas as pd
import matplotlib.pyplot as plt
# CSV dosyasını oku (daha önce oluşturduğun)
df = pd.read_csv("personel.csv", sep=";", encoding="utf-8")
# Departmanlara göre ortalama maaş hesapla
gruplu = df.groupby("DEPARTMAN")["MAAŞ"].mean()
# Ortalama maaşı çubuk grafikle göster
gruplu.plot(kind="bar", color="orange")
# Grafiğe başlık ve etiketleri ekle
plt.title("Departmanlara Göre Ortalama Maaş")
plt.xlabel("Departman")
plt.ylabel("Maaş (TL)")
# Görseli düzgün hizala ve ekrana göster
plt.tight_layout()
plt.show()
