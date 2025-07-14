from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
slice = [120, 80, 30, 20]
labels = ["Sixty", "Forty", 'Extral','Extra2']
colors = ['blue','red','yellow','green']


plt.pie(slice, labels=labels, colors=colors, 
        wedgeprops={"edgecolor": "black"})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()