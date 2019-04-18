import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv

sns.set(style="white", context="talk")

with open('airline-safety.csv') as csvData:
    airData = csv.reader(csvData, delimiter=',')
    airline = []
    km = []
    inc84 = []
    fatinc84 = []
    fat84 = []
    inc00 = []
    fatinc00 = []
    fat00 = []
    next(airData)
    for row in airData:
        airline.append(row[0])
        km.append(row[1])
        inc84.append(row[2])
        fatinc84.append(row[3])
        fat84.append(row[4])
        inc00.append(row[5])
        fatinc00.append(row[6])
        fat00.append(row[7])

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(7, 5))

fats = []

for i, j in zip(fat84, fat00):
    fats.append(int(j) - int(i))

# Center the data to make it diverging
x = airline
y = fats
sns.barplot(x=x, y=y, palette="vlag", ax=ax)
ax.axhline(0, color="k", clip_on=False)
ax.set_ylabel("Safety Improvement")

# Finalize the plot
sns.despine(bottom=True)
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=2)

plt.show()