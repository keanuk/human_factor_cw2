import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

airData = pd.read_csv('airline-safety.csv')
airData = airData.sort_values('avail_seat_km_per_week', ascending=False)

airData['total_fatalities'] = airData['fatalities_85_99'] + airData['fatalities_00_14']
airData['total_fatal_incidents'] = airData['fatal_accidents_85_99'] + airData['fatal_accidents_00_14']
airData['total_incidents'] = airData['incidents_85_99'] + airData['incidents_00_14']

airData['fatal_incs_85_99_ask'] = airData['fatal_accidents_85_99'] / (airData['avail_seat_km_per_week'] / 1000000000)
airData['fatal_incs_00_14_ask'] = airData['fatal_accidents_00_14'] / (airData['avail_seat_km_per_week'] / 1000000000)
airData['incs_85_99_ask'] = airData['incidents_85_99'] / (airData['avail_seat_km_per_week'] / 1000000000)
airData['incs_00_14_ask'] = airData['incidents_00_14'] / (airData['avail_seat_km_per_week'] / 1000000000)
airData['fatalities_85_99_ask'] = airData['fatalities_85_99'] / (airData['avail_seat_km_per_week'] / 1000000000)
airData['fatalities_00_14_ask'] = airData['fatalities_00_14'] / (airData['avail_seat_km_per_week'] / 1000000000)

sns.set(style="whitegrid", context="poster", font_scale=1.25)
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(35, 18))

sns.regplot(x='avail_seat_km_per_week', y='incidents_85_99', data=airData.sort_values('avail_seat_km_per_week', ascending=False)[0:30], label="1985-1999", color="#359aff", ax=ax1, ci=None)
sns.regplot(x='avail_seat_km_per_week', y='incidents_00_14', data=airData.sort_values('avail_seat_km_per_week', ascending=False)[0:30], label="2000-2014", color="#f8548d", ax=ax1, ci=None)

sns.regplot(x='avail_seat_km_per_week', y='fatal_accidents_85_99', data=airData.sort_values('avail_seat_km_per_week', ascending=False)[0:30], label="1985-1999", color="#359aff", ax=ax2, ci=None)
sns.regplot(x='avail_seat_km_per_week', y='fatal_accidents_00_14', data=airData.sort_values('avail_seat_km_per_week', ascending=False)[0:30], label="2000-2014", color="#f8548d", ax=ax2, ci=None)

sns.regplot(x='avail_seat_km_per_week', y='fatalities_85_99', data=airData.sort_values('avail_seat_km_per_week', ascending=False)[0:30], label="1985-1999", color="#359aff", ax=ax3, ci=None)
sns.regplot(x='avail_seat_km_per_week', y='fatalities_00_14', data=airData.sort_values('avail_seat_km_per_week', ascending=False)[0:30], label="2000-2014", color="#f8548d", ax=ax3, ci=None)

ax1.set(ylabel="Incidents", xlabel="Airline Available Seat Kilometers", title="Incidents per Trillion Airline ASK")
ax1.legend(ncol=2, loc="upper right", frameon=True)
ax2.set(ylabel="Fatal Accidents", xlabel="Airline Available Seat Kilometers", title="Fatal Accidents per Trillion Airline ASK")
ax2.legend(ncol=2, loc="upper right", frameon=True)
ax3.set(ylabel="Fatalities", xlabel="Airline Available Seat Kilometers", title="Fatalities per Trillion Airline ASK")
ax3.legend(ncol=2, loc="upper right", frameon=True)
sns.despine(left=True, bottom=True)

plt.show()