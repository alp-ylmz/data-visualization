import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("personel.csv", sep=';', encoding="utf-8")

"""
yazilim = df[df["DEPARTMAN"] == "YAZILIM"]
ortalama_maas = yazilim['MAAŞ'].mean()
print(f"ORTALAMA MAAŞ: {ortalama_maas:.2f} TL")
"""

grup = df.groupby("DEPARTMAN")["MAAŞ"].mean()

#GRAFİK ÇİZİMİ
grup.plot(kind='bar', color='skyblue')
plt.title("Departmanlara Göre Ortalama Maaş")
plt.ylabel("MAAŞ (TL)")
plt.xlabel("DEPARTMAN")
plt.tight_layout()
plt.show()