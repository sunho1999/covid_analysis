import torch
import pandas as pd
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(precision=2, suppress=True)  #과학적 표기 없애고 소수 2짜리까지 표현


df = pd.read_csv("./owid-covid-data.csv")

df['date'] = pd.to_datetime(df['date'])

date_df = df.set_index(['date'])
per_df = date_df.loc[:,['location','total_cases_per_million','new_cases_per_million','people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred']]

jp_df = per_df[per_df['location'] == 'Japan']
kr_df = per_df[per_df['location'] == 'South Korea']

sr_one = jp_df['total_cases_per_million'] # jp의 total_cases_per_million
sr_two = kr_df['total_cases_per_million'] # kr의 total_cases_per_million

fig = plt.figure(figsize = (20,5))
ax = fig.add_subplot(1,1,1)

ax.plot(sr_one.index,sr_one.values,marker='o',markerfacecolor = 'green',markersize = 1, color = 'olive',linewidth =0.5, label = "Ratio of covid in japan")
ax.plot(sr_two.index,sr_two.values,marker='o',markerfacecolor = 'red',markersize = 1, color = 'magenta',linewidth =0.5, label = "Ratio of covid in Korea")

ax.legend(loc = 'best')
ax.set_title("Ratio of confirmed cases of covid in Korea and Japan")
ax.set_xlabel("date")
ax.set_ylabel("Percentage of confirmed cases by date")

plt.show()