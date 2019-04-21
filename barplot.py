import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import csv

# plt.rcParams["axes.labelsize"] = 30
# sns.set(font_scale=10)
# sns.set_context("paper", rc={"axes.labelsize":72})

airData = pd.read_csv('airline-safety.csv')
airData = airData.sort_values('avail_seat_km_per_week', ascending=False)
# print(airData)
airData['total_fatalities'] = airData['fatalities_85_99'] + airData['fatalities_00_14']

sns.set(style="whitegrid")
f, ax = plt.subplots(figsize=(25, 18))

sns.set_color_codes("pastel")
sns.barplot(x='total_fatalities', y='airline', data=airData[0:19].sort_values('total_fatalities', ascending=False), label="2000-2014", color="#aed7ff", ax=ax)
sns.set_color_codes("muted")
sns.barplot(x='fatalities_85_99', y='airline', data=airData[0:19].sort_values('total_fatalities', ascending=False), label="1984-1999", color="#4aa5ff", ax=ax)

sns.set(style="white", context="talk", font_scale=2)
ax.set(xlim=(0, 600), ylabel="Airlines", xlabel="Fatalities")
ax.legend(ncol=2, loc="lower right", frameon=True)
sns.despine(left=True, bottom=True)

plt.show()