import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

airData = pd.read_csv('airline-safety.csv')
airData = airData.sort_values('avail_seat_km_per_week', ascending=False)

airData['total_fatalities'] = airData['fatalities_85_99'] + airData['fatalities_00_14']
airData['total_fatal_incidents'] = airData['fatal_accidents_85_99'] + airData['fatal_accidents_00_14']
airData['total_incidents'] = airData['incidents_85_99'] + airData['incidents_00_14']

airData['fatalities_85_99_ask'] = airData['fatalities_85_99'] / (airData['avail_seat_km_per_week'] / 1000000000)
airData['fatalities_00_14_ask'] = airData['fatalities_00_14'] / (airData['avail_seat_km_per_week'] / 1000000000)

airData['airline'] = airData['airline'].str.replace("*", "")

sns.set(style="whitegrid", context="poster", font_scale=1.25)
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(25, 18), sharey=False)

sns.barplot(x='fatalities_85_99_ask', y='airline', data=airData.sort_values('avail_seat_km_per_week', ascending=False)[0:30], label="Fatalities", color="#359aff", ax=ax1)
sns.barplot(x='fatalities_00_14_ask', y='airline', data=airData.sort_values('avail_seat_km_per_week', ascending=False)[0:30], label="Fatalities", color="#f8548d", ax=ax2)

ax1.set(xlim=(0, 700), ylabel="Airlines", xlabel="Fatalities (per One Trillion Available Seat Kilometers)", title="Airline Fatalities 1985-1999")
ax2.set(xlim=(0, 700), ylabel="", xlabel="Fatalities (per One Trillion Available Seat Kilometers)", title="Airline Fatalities 2000-2014")
ax1.axvline(airData.sort_values('avail_seat_km_per_week', ascending=False)['fatalities_85_99_ask'][0:30].mean(), ls='--', label='Mean: ' + str(round(airData.sort_values('avail_seat_km_per_week', ascending=False)['fatalities_85_99_ask'][0:30].mean())))
ax2.axvline(airData.sort_values('avail_seat_km_per_week', ascending=False)['fatalities_00_14_ask'][0:30].mean(), ls='--', label='Mean: ' + str(round(airData.sort_values('avail_seat_km_per_week', ascending=False)['fatalities_00_14_ask'][0:30].mean())))
ax1.legend(ncol=2, loc="upper right", frameon=True)
ax2.legend(ncol=2, loc="upper right", frameon=True)
sns.despine(left=True, bottom=True)

plt.show()