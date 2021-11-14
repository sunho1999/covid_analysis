import torch
import pandas as pd
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(precision=2, suppress=True)  #과학적 표기 없애고 소수 2짜리까지 표현


df = pd.read_csv("./owid-covid-data.csv")

df['date'] = pd.to_datetime(df['date'])

new_df = df[['location','date','total_deaths_per_million','total_cases_per_million','people_vaccinated_per_hundred','human_development_index']]
print(new_df)