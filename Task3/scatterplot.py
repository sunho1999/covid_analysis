import torch
import pandas as pd
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(precision=2, suppress=True)  #과학적 표기 없애고 소수 2짜리까지 표현


df = pd.read_csv("./owid-covid-data.csv")

df['date'] = pd.to_datetime(df['date'])

new_df = df[['location','date','total_deaths_per_million','total_cases_per_million','people_vaccinated_per_hundred','human_development_index']]

location_maxdate = new_df.groupby('location')['date'].max()

new_df['scatter_y'] = new_df['total_deaths_per_million'] / new_df['total_cases_per_million']


plt.figure(figsize=(14, 5))
plt.scatter(new_df['people_vaccinated_per_hundred'],new_df['scatter_y'],linewidth=0.5,edgecolors='black')

plt.title("correlation")
plt.xlabel("people_vaccinated_per_hundred")
plt.ylabel("total_deaths_per_million/total_cases_per_million")
plt.show()